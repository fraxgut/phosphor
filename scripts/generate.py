#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""
generate.py
@fraxgut
CC-BY-SA-4.0
Generate every Phosphor scheme and export from src/phosphor.yaml.

Run it with `uv run scripts/generate.py`. It writes schemes/ and dist/,
and it never reads them. Running it twice without editing the source
leaves the working tree clean.
"""

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from phosphor_colour import (  # noqa: E402
    contrast, delta_e_ok, hex_to_oklch, max_chroma, oklch_to_hex,
)

SRC = ROOT / "src" / "phosphor.yaml"
BANNER = "Generated from src/phosphor.yaml. Do not edit manually."

FAMILIES = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "magenta"]
TONES = ["dim", "normal", "bright"]


# --- TONE CONSTRUCTION ---
# One normal colour expands into three tones by moving in OKLab
# lightness. The chroma follows whatever the hue and lightness can hold
# inside sRGB.
def tones(L, C, H, cfg):
    out = {}
    for tone, dL in (("dim", cfg["dim"]), ("normal", 0.0), ("bright", cfg["bright"])):
        Lt = min(cfg["ceiling"], max(cfg["floor"], L + dL))
        out[tone] = oklch_to_hex((Lt, min(C, max_chroma(Lt, H) * 0.995), H))
    return out


def lift_to_contrast(L, C, H, bg, target):
    """Raise lightness until the colour clears the contrast floor.

    Chroma follows the gamut at the new lightness. A colour that already
    clears the floor is returned unchanged.
    """
    if contrast(oklch_to_hex((L, C, H)), bg) >= target:
        return L, C
    lo, hi = L, 1.0
    for _ in range(30):
        mid = (lo + hi) / 2
        if contrast(oklch_to_hex((mid, min(C, max_chroma(mid, H) * 0.995), H)), bg) < target:
            lo = mid
        else:
            hi = mid
    return hi, min(C, max_chroma(hi, H) * 0.995)


def in_arc(H, lo, hi):
    return lo <= H <= hi if lo <= hi else H >= lo or H <= hi


def separation(state):
    """The smallest OKLab distance between any two accents."""
    return min(delta_e_ok(oklch_to_hex(tuple(state[a])), oklch_to_hex(tuple(state[b])))
               for i, a in enumerate(FAMILIES) for b in FAMILIES[i + 1:])


# --- TINT ---
# Every hue rotates part of the way towards one target. Rotation alone
# pushes together the pairs that were already close, so a second pass
# redistributes the lightness of the slots that moved. The ceiling on
# that pass is what keeps a rotated warm slot reading as a brown rather
# than as a second yellow.
def tint(base, target, amount, d):
    raw = {}
    for n in FAMILIES:
        L, C, H = base[n]
        delta = (H - target + 540) % 360 - 180
        Ht = (target + delta * (1 - amount)) % 360
        raw[n] = [L, min(C, max_chroma(L, Ht) * 0.995), Ht]

    lo_off, hi_off = d["tint"]["lightness_search"]
    band = d["tint"]["brown_band"]
    movable = [n for n in FAMILIES
               if abs((raw[n][2] - target + 540) % 360 - 180) > 1.0]
    for _ in range(4):
        moved = False
        for n in movable:
            L0 = raw[n][0]
            ceil = d["tint"]["brown_ceiling"] if band[0] <= raw[n][2] <= band[1] else 0.78
            lo, hi = max(0.50, L0 + lo_off), min(ceil, L0 + hi_off)
            if hi <= lo:
                continue
            best_L, best_s = raw[n][0], separation(raw)
            steps = int((hi - lo) / 0.005) + 1
            for i in range(steps):
                trial = {k: list(v) for k, v in raw.items()}
                trial[n][0] = lo + i * 0.005
                trial[n][1] = min(trial[n][1],
                                  max_chroma(trial[n][0], trial[n][2]) * 0.995)
                sc = separation(trial)
                if sc > best_s + 1e-6:
                    best_L, best_s, moved = trial[n][0], sc, True
            raw[n][0] = best_L
            raw[n][1] = min(raw[n][1], max_chroma(best_L, raw[n][2]) * 0.995)
        if not moved:
            break
    return raw


def kin_ok(fam, L, C, H, d):
    lo, hi = d["kinship"][fam]
    return in_arc(H, lo, hi) or (L < d["muted"]["lightness"]
                                 and C < d["muted"]["chroma"])


def tint_strength(base, target, d, floor):
    """The strongest Tint that keeps kinship and keeps the families apart.

    The strength is derived rather than chosen: it is the point where one
    of the two rules stops the rotation.
    """
    lo, hi = 0.0, 1.0
    for _ in range(24):
        mid = (lo + hi) / 2
        raw = tint(base, target, mid, d)
        ok = all(kin_ok(n, *raw[n], d) for n in FAMILIES) and separation(raw) >= floor
        lo, hi = (mid, hi) if ok else (lo, mid)
    return lo


# --- MONO ---
# One hue across every chromatic slot, within a drift budget. The
# families separate by lightness and chroma alone.
def mono(target, centre, d):
    m = d["mono"]
    centre = max(centre, m["lightness_floor"])
    out = {}
    for fam, (dL, c_frac, drift) in m["address"].items():
        H = (target + max(-m["hue_drift"], min(m["hue_drift"], drift))) % 360
        L = centre + dL * m["lightness_scale"]
        out[fam] = [L, max_chroma(L, H) * 0.995 * c_frac, H]
    return out


def mono_neutrals(neutral, hue):
    """Tint the ramp with a trace of the variant hue that grows with light."""
    out = []
    for i, h in enumerate(neutral):
        L = hex_to_oklch(h)[0]
        C = min(0.09 * (i / 7) ** 1.4, max_chroma(L, hue) * 0.995)
        out.append(oklch_to_hex((L, C, hue)))
    return out


# --- PREVIEW ASSETS ---
# The swatches ship as two local SVG files rather than as one remote
# image per cell. A reader with no network still sees the palette, and
# the repository carries no dependency on an image host.
SW, GAP, PAD, LABEL = 96, 3, 14, 22


def svg_text(x, y, s, fill, size=10, weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" '
            f'font-family="ui-monospace,SFMono-Regular,Menlo,monospace">{s}</text>')


def ink(h):
    """A label colour that stays readable on the swatch behind it."""
    from phosphor_colour import hex_to_rgb, relative_luminance
    return "#000000" if relative_luminance(hex_to_rgb(h)) > 0.16 else "#FFFAEB"


def palette_svg(variant):
    """The full palette: the neutral ramp, then the families by tone."""
    neutral, fam = variant["neutral"], variant["families"]
    w = PAD * 2 + 8 * SW + 7 * GAP
    rows = len(TONES) + 1
    h = PAD * 2 + LABEL * (rows + 1) + rows * 54 + rows * GAP + 18
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" role="img" aria-label="{variant["name"]} palette">',
           f'<rect width="{w}" height="{h}" fill="{neutral[0]}"/>']
    y = PAD + 14
    out.append(svg_text(PAD, y, variant["name"].upper(), neutral[6], 13, 700))
    y += 12
    out.append(svg_text(PAD, y, "neutral ramp", neutral[4], 9))
    y += 8
    for i, hexv in enumerate(neutral):
        x = PAD + i * (SW + GAP)
        out.append(f'<rect x="{x}" y="{y}" width="{SW}" height="54" fill="{hexv}"/>')
        out.append(svg_text(x + 6, y + 46, hexv, ink(hexv), 9, 600))
        out.append(svg_text(x + 6, y + 14, f"base0{i}", ink(hexv), 9))
    y += 54 + GAP + LABEL
    for tone in TONES:
        out.append(svg_text(PAD, y - 6, tone, neutral[4], 9))
        for i, name in enumerate(FAMILIES):
            hexv = fam[name][tone]
            x = PAD + i * (SW + GAP)
            out.append(f'<rect x="{x}" y="{y}" width="{SW}" height="54" fill="{hexv}"/>')
            out.append(svg_text(x + 6, y + 46, hexv, ink(hexv), 9, 600))
            if tone == "normal":
                out.append(svg_text(x + 6, y + 14, name, ink(hexv), 9))
        y += 54 + GAP + LABEL
    out.append("</svg>")
    return "\n".join(out)


def variants_svg(variants):
    """Every variant as one row of eight normal tones."""
    cell, rh, name_w = 74, 26, 190
    w = PAD * 2 + name_w + 8 * cell + 7 * GAP
    h = PAD * 2 + len(variants) * (rh + GAP)
    bg = variants[0]["neutral"][0]
    fg, mut = variants[0]["neutral"][6], variants[0]["neutral"][4]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" role="img" aria-label="Phosphor variants">',
           f'<rect width="{w}" height="{h}" fill="{bg}"/>']
    y = PAD
    for v in variants:
        out.append(svg_text(PAD, y + 17, v["name"], fg if v["tier"] == "full" else mut, 10,
                            700 if v["tier"] == "full" else 400))
        for i, name in enumerate(FAMILIES):
            x = PAD + name_w + i * (cell + GAP)
            out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{rh}" '
                       f'fill="{v["families"][name]["normal"]}"/>')
        y += rh + GAP
    out.append("</svg>")
    return "\n".join(out)


# --- SWATCHES AND DOCUMENTATION TABLES ---
# Every colour in the documentation tables gets a small local SVG square,
# so a table shows the colour beside its hex the way a palette should.
# The files are named by hex and shared across every table that uses the
# colour.
def write_swatches(colours):
    out = ROOT / "assets" / "swatch"
    out.mkdir(parents=True, exist_ok=True)
    for h in sorted(colours):
        (out / f"{h.lstrip('#')}.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16">'
            f'<rect width="16" height="16" rx="3" fill="{h}"/></svg>\n')
    return len(colours)


# The table headings, in each language the documentation carries.
WORDS = {
    "en": {"slot": "slot", "hex": "hex", "contrast": "contrast on base00",
           "family": "family", "dim": "dim", "normal": "normal",
           "bright": "bright", "acontrast": "contrast on base01",
           "variant": "variant", "strength": "strength", "scheme": "scheme"},
    "es": {"slot": "ranura", "hex": "hex", "contrast": "contraste sobre base00",
           "family": "familia", "dim": "tenue", "normal": "normal",
           "bright": "vivo", "acontrast": "contraste sobre base01",
           "variant": "variante", "strength": "intensidad", "scheme": "esquema"},
    "la": {"slot": "sedes", "hex": "hex", "contrast": "discrimen ad base00",
           "family": "familia", "dim": "obscurus", "normal": "medius",
           "bright": "clarus", "acontrast": "discrimen ad base01",
           "variant": "varietas", "strength": "vis", "scheme": "schema"},
}


def sw(h, depth):
    """An inline swatch image, with the path written from the file's depth."""
    up = "../" * depth
    return (f'<img src="{up}assets/swatch/{h.lstrip("#")}.svg" width="14" '
            f'height="14" alt=""> `{h}`')


def palette_tables(variant, lang, depth):
    """The neutral ramp and the chromatic families as Markdown tables."""
    w = WORDS[lang]
    neutral, fam = variant["neutral"], variant["families"]
    out = [f'| {w["slot"]} | {w["hex"]} | okL | {w["contrast"]} |',
           "| --- | --- | --- | --- |"]
    for i, h in enumerate(neutral):
        L = hex_to_oklch(h)[0]
        c = "—" if i == 0 else f"{contrast(h, neutral[0]):.2f}:1"
        out.append(f'| base0{i} | {sw(h, depth)} | {L:.3f} | {c} |')
    out += ["", f'| {w["family"]} | {w["dim"]} | {w["normal"]} | {w["bright"]} '
                f'| okL | okC | okH | {w["acontrast"]} |',
            "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for n in FAMILIES:
        L, C, H = hex_to_oklch(fam[n]["normal"])
        out.append(f'| {n} | {sw(fam[n]["dim"], depth)} | {sw(fam[n]["normal"], depth)} '
                   f'| {sw(fam[n]["bright"], depth)} | {L:.3f} | {C:.3f} | {H:.1f}° '
                   f'| {contrast(fam[n]["normal"], neutral[1]):.2f}:1 |')
    return "\n".join(out)


def variant_table(variants, lang, depth):
    """Every variant, with its strength where one was derived."""
    w = WORDS[lang]
    out = [f'| {w["variant"]} | {w["scheme"]} | {w["strength"]} |',
           "| --- | --- | --- |"]
    for v in variants:
        strength = f'{v["strength"]:.3f}' if "strength" in v else "—"
        out.append(f'| {v["name"]} | `{v["slug"]}` | {strength} |')
    return "\n".join(out)


def inject(path, blocks):
    """Replace the content between each pair of generated markers."""
    if not path.exists():
        return False
    text = path.read_text()
    for key, body in blocks.items():
        start, end = f"<!-- {key}:start -->", f"<!-- {key}:end -->"
        if start not in text or end not in text:
            continue
        head = text[:text.index(start) + len(start)]
        tail = text[text.index(end):]
        text = f"{head}\n{body}\n{tail}"
    path.write_text(text)
    return True


# --- SCHEME WRITERS ---
def scheme_yaml(name, slug, author, system, palette):
    lines = [f"# {BANNER}",
             f'system: "{system}"',
             f'name: "{name}"',
             f'author: "{author}"',
             f'slug: "{slug}"',
             'variant: "dark"',
             "palette:"]
    lines += [f'  {k}: "{v}"' for k, v in palette.items()]
    return "\n".join(lines) + "\n"


def base16_palette(neutral, fam, mapping):
    p = {f"base0{i}": neutral[i] for i in range(8)}
    for slot, ref in mapping["base16"].items():
        family, tone = ref.split(".")
        p[slot] = fam[family][tone]
    return p


def base24_palette(neutral, fam, mapping):
    p = base16_palette(neutral, fam, mapping)
    for slot, ref in mapping["base24"].items():
        if ref.startswith("neutral."):
            p[slot] = neutral[int(ref.split(".")[1])]
        else:
            family, tone = ref.split(".")
            p[slot] = fam[family][tone]
    return p


def floored(lch, bg, d):
    """Apply the contrast floor to one colour."""
    L, C, H = lch
    L, C = lift_to_contrast(L, C, H, bg, d["contrast_floor"])
    return L, C, H


def main():
    doc = yaml.safe_load(SRC.read_text())
    meta, neutral = doc["meta"], doc["neutral"]
    fam_src, d, mapping = doc["families"], doc["derivation"], doc["mapping"]
    tcfg = d["tones"]

    base = {n: hex_to_oklch(fam_src[n]["normal"]) for n in FAMILIES}
    full_sep = separation({n: list(base[n]) for n in FAMILIES})
    floor = full_sep * d["tint"]["separation_floor_ratio"]

    variants = [{
        "name": meta["name"], "slug": meta["slug"], "tier": "full",
        "neutral": neutral,
        "families": {n: dict(fam_src[n]) for n in FAMILIES},
    }]

    # --- TINT VARIANTS ---
    for fam in FAMILIES:
        target = base[fam][2]
        amount = tint_strength(base, target, d, floor)
        raw = tint(base, target, amount, d)
        variants.append({
            "name": f"{meta['name']} Tint {fam.title()}",
            "slug": f"{meta['slug']}-tint-{fam}",
            "tier": "tint", "strength": round(amount, 3),
            "neutral": neutral,
            "families": {n: tones(*floored(raw[n], neutral[1], d), tcfg)
                         for n in FAMILIES},
        })

    # --- MONO VARIANTS ---
    anchor_L, _, anchor_H = hex_to_oklch(d["mono"]["green_anchor"])
    for fam in FAMILIES:
        target = anchor_H if fam == "green" else base[fam][2]
        centre = anchor_L if fam == "green" else base[fam][0]
        raw = mono(target, centre, d)
        mneutral = mono_neutrals(neutral, target)
        variants.append({
            "name": f"{meta['name']} Mono {fam.title()}",
            "slug": f"{meta['slug']}-mono-{fam}",
            "tier": "mono",
            "neutral": mneutral,
            "families": {n: tones(*floored(raw[n], mneutral[1], d), tcfg)
                         for n in FAMILIES},
        })

    # --- WRITE SCHEMES ---
    written = 0
    for v in variants:
        for system, builder in (("base16", base16_palette), ("base24", base24_palette)):
            path = ROOT / "schemes" / system / f"{v['slug']}.yaml"
            path.write_text(scheme_yaml(
                v["name"], v["slug"], meta["author"], system,
                builder(v["neutral"], v["families"], mapping)))
            written += 1

    # --- WRITE EXPORTS ---
    # One JSON document carries the whole system, including the measured
    # figures, so that a consumer never has to recompute them.
    payload = {"$comment": BANNER, "meta": meta,
               "full_separation": round(full_sep, 4),
               "tint_floor": round(floor, 4), "variants": []}
    for v in variants:
        entry = {k: v[k] for k in ("name", "slug", "tier") if k in v}
        if "strength" in v:
            entry["strength"] = v["strength"]
        entry["neutral"] = v["neutral"]
        entry["families"] = {
            n: {t: {"hex": v["families"][n][t],
                    "oklch": [round(x, 4) for x in hex_to_oklch(v["families"][n][t])],
                    "contrast_on_base01": round(contrast(v["families"][n][t],
                                                         v["neutral"][1]), 2)}
                for t in TONES}
            for n in FAMILIES}
        payload["variants"].append(entry)
    (ROOT / "dist" / "json" / "phosphor.json").write_text(
        json.dumps(payload, indent=2) + "\n")

    # The stylesheet carries the full palette as custom properties, and
    # each variant under a data attribute so a page can switch at runtime.
    css = [f"/* {BANNER} */", ""]
    for v in variants:
        sel = ":root" if v["tier"] == "full" else f':root[data-phosphor="{v["slug"]}"]'
        css.append(f"/* {v['name']} */")
        css.append(f"{sel} {{")
        css += [f"  --ph-base0{i}: {h};" for i, h in enumerate(v["neutral"])]
        css += [f"  --ph-{n}-{t}: {v['families'][n][t]};"
                for n in FAMILIES for t in TONES]
        css.append("}")
        css.append("")
    (ROOT / "dist" / "css" / "phosphor.css").write_text("\n".join(css))

    # Swatches for every colour the documentation tables show.
    docs_colours = {h for h in variants[0]["neutral"]}
    docs_colours |= {variants[0]["families"][n][t] for n in FAMILIES for t in TONES}
    write_swatches(docs_colours)

    injected = 0
    for lang in WORDS:
        blocks = {"palette": palette_tables(variants[0], lang, 2),
                  "variants": variant_table(variants, lang, 2)}
        if inject(ROOT / "i18n" / lang / "README.md", blocks):
            injected += 1
    if inject(ROOT / "README.md", {"palette": palette_tables(variants[0], "en", 0),
                                   "variants": variant_table(variants, "en", 0)}):
        injected += 1

    (ROOT / "assets" / "palette.svg").write_text(palette_svg(variants[0]) + "\n")
    (ROOT / "assets" / "variants.svg").write_text(variants_svg(variants) + "\n")

    print(f"{len(variants)} variants, {written} scheme files, 2 exports, "
          f"{len(docs_colours)} swatches, {injected} documents")
    print(f"full palette separation {full_sep:.4f}, tint floor {floor:.4f}")
    for v in variants:
        if v["tier"] == "tint":
            print(f"  {v['slug']:<24} strength {v['strength']:.3f}")


if __name__ == "__main__":
    main()
