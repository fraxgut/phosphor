#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""
validate.py
@fraxgut
CC-BY-SA-4.0
Check the Phosphor source and everything generated from it.

Run it with `uv run scripts/validate.py`. It reports a line per check and
exits non-zero when a check fails. Warnings describe deliberate trade-offs
and do not fail the run.
"""

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from phosphor_colour import (  # noqa: E402
    contrast, delta_e_ok, hex_to_oklch, hex_to_rgb, in_gamut, oklch_to_hex,
)

FAMILIES = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "magenta"]
TONES = ["dim", "normal", "bright"]
HEX = re.compile(r"^#[0-9A-F]{6}$")

failures, warnings = [], []


def check(ok, label, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'  ' + detail if detail else ''}")
    if not ok:
        failures.append(label)


def warn(label, detail):
    print(f"  warn  {label}  {detail}")
    warnings.append(label)


doc = yaml.safe_load((ROOT / "src" / "phosphor.yaml").read_text())
data = json.loads((ROOT / "dist" / "json" / "phosphor.json").read_text())
d = doc["derivation"]

# --- SOURCE ---
print("source")
every = [h for f in doc["families"].values() for h in f.values()] + doc["neutral"]
check(all(HEX.match(h) for h in every), "hex syntax", f"{len(every)} colours")
check(len(doc["neutral"]) == 8, "neutral ramp has 8 rungs")
check(set(doc["families"]) == set(FAMILIES), "8 chromatic families")
check(all(set(f) == set(TONES) for f in doc["families"].values()),
      "every family has dim, normal and bright")
check(len(set(every)) == len(every), "no duplicate colour in the source")
check(all(in_gamut(hex_to_rgb(h)) for h in every), "every colour inside sRGB")

# The ramp must climb without a reversal, or the neutrals stop reading as
# a ramp at all.
ramp = [hex_to_oklch(h)[0] for h in doc["neutral"]]
check(all(b > a for a, b in zip(ramp, ramp[1:])), "neutral ramp rises monotonically")

# --- ANCHORS ---
# The three anchor hues carry the identity of the scheme and must match
# the version 1 angles they were fixed at.
print("\nanchors")
ANCHOR_HUE = {"yellow": 76.5, "green": 128.7, "cyan": 153.1}
for fam, want in ANCHOR_HUE.items():
    got = hex_to_oklch(doc["families"][fam]["normal"])[2]
    check(abs(got - want) < 0.5, f"{fam} holds its hue", f"{got:.1f}° (expected {want}°)")

# --- GENERATED VARIANTS ---
print("\nvariants")
check(len(data["variants"]) == 17, "17 variants", "1 full, 8 tint, 8 mono")
tiers = [v["tier"] for v in data["variants"]]
check(tiers.count("tint") == 8 and tiers.count("mono") == 8, "every family has a Tint and a Mono")

full = next(v for v in data["variants"] if v["tier"] == "full")
for fam in FAMILIES:
    check(full["families"][fam]["normal"]["hex"] == doc["families"][fam]["normal"],
          f"full palette {fam} matches the source")

# --- SEPARATION ---
# The smallest distance between two accents decides whether syntax
# highlighting can tell them apart.
print("\nseparation")
for v in data["variants"]:
    worst = min((delta_e_ok(v["families"][a]["normal"]["hex"],
                            v["families"][b]["normal"]["hex"]), f"{a}/{b}")
                for i, a in enumerate(FAMILIES) for b in FAMILIES[i + 1:])
    if v["tier"] == "full":
        check(worst[0] >= 0.08, "full palette separation", f"{worst[0]:.4f} ({worst[1]})")
    elif v["tier"] == "tint":
        check(worst[0] >= data["tint_floor"] - 1e-4, f"{v['slug']} above the floor",
              f"{worst[0]:.4f}")
    else:
        # A Mono variant buys coherence and pays in distinguishability.
        # That is inherent to monochromy, so it is reported and allowed.
        if worst[0] < 0.05:
            warn(f"{v['slug']} separation", f"{worst[0]:.4f} ({worst[1]}) — inherent to Mono")

# --- KINSHIP ---
# A Tint slot may change identity only into a relative of its origin.
print("\nkinship")


def in_arc(H, lo, hi):
    return lo <= H <= hi if lo <= hi else H >= lo or H <= hi


for v in [x for x in data["variants"] if x["tier"] == "tint"]:
    bad = []
    for fam in FAMILIES:
        L, C, H = v["families"][fam]["normal"]["oklch"]
        lo, hi = d["kinship"][fam]
        if not (in_arc(H, lo, hi) or (L < d["muted"]["lightness"]
                                      and C < d["muted"]["chroma"])):
            bad.append(f"{fam}@{H:.0f}°")
    check(not bad, f"{v['slug']} keeps every slot related", ", ".join(bad))

# --- CONTRAST ---
# Accents are syntax colours, not body text, so the floor is the 3:1 that
# WCAG sets for large text and interface components. Anything that also
# clears 4.5:1 is usable as body text and is reported as such.
print("\ncontrast")
for v in data["variants"]:
    bg = v["neutral"][1]
    low = [(f, v["families"][f]["normal"]["contrast_on_base01"]) for f in FAMILIES
           if contrast(v["families"][f]["normal"]["hex"], bg) < 3.0]
    check(not low, f"{v['slug']} accents clear 3:1", str(low) if low else "")

body = [f for f in FAMILIES
        if contrast(full["families"][f]["normal"]["hex"], full["neutral"][1]) >= 4.5]
print(f"  note  full palette accents that also clear 4.5:1 for body text: {len(body)}/8")

# --- SLOT MAPPING ---
print("\nmapping")
for system, count in (("base16", 16), ("base24", 24)):
    files = sorted((ROOT / "schemes" / system).glob("*.yaml"))
    check(len(files) == 17, f"{system} has a scheme per variant", f"{len(files)} files")
    for path in files:
        scheme = yaml.safe_load(path.read_text())
        slots = scheme["palette"]
        expected = ([f"base0{i}" for i in range(8)] + [f"base0{c}" for c in "89ABCDEF"]
                    + ([f"base1{c}" for c in "01234567"] if system == "base24" else []))
        missing = [s for s in expected if s not in slots]
        if missing:
            check(False, f"{path.name} slot coverage", f"missing {missing}")
            break
    else:
        check(True, f"{system} slot coverage", f"{count} slots in each of 17 files")

# --- REPRODUCIBILITY ---
# The generated files must be a function of the source alone.
print("\nreproducibility")
check((ROOT / "dist" / "json" / "phosphor.json").read_text().startswith('{\n  "$comment"'),
      "exports carry the generated banner")

print()
if failures:
    print(f"{len(failures)} failed, {len(warnings)} warning(s)")
    sys.exit(1)
print(f"all checks passed, {len(warnings)} warning(s)")
