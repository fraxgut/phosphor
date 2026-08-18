<!--
CHANGELOG.md
@fraxgut
CC-BY-SA-4.0
Release history for the Phosphor palette
-->

# Changelog

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2.0.0

**Phosphor**, a terminal palette of 32 canonical colours: a warm neutral ramp
of eight, and eight chromatic families with a dim, a normal and a bright tone
each.

### Palette

Every colour is designed in OKLCH. Three hues are fixed and carry the identity
of the scheme: the yellow at 76.3°, the lime green at 128.6°, and the spring
green at 152.9° that the scheme calls cyan. The other five sit where a
constrained search puts them, each inside the band its name occupies, so that
the smallest distance between two accents is as large as the anchors allow. It
measures 0.082 ΔE, between green and cyan.

Accents hold a floor of 3:1 against base01, the ratio WCAG sets for large text
and interface components. Five of the eight also clear 4.5:1 and carry body
text.

### Variants

Seventeen: the full palette, eight Tint variants and eight Mono variants.

A Tint rotates every hue part of the way towards one target. Its strength is
derived from two rules rather than chosen — each slot stays a relative of the
colour it replaced, and the families stay at least three quarters as far apart
as the full palette holds them — so each variant reaches its own figure,
between 0.261 and 0.639.

A Mono holds one hue across every chromatic slot within a drift of ±10°, and
separates the families by lightness and chroma. Mono Green takes the hue of
`#47D813`.

### Standards

`src/phosphor.yaml` is the canonical palette, and the Base16 and Base24 schemes
are generated from it. Base24 carries the three tones without loss. The Base16
mapping is recorded in the source, because two of its slots hold a colour the
specification names differently.

### Tooling

`scripts/generate.py` writes every scheme, export, preview and documentation
table from the source. `scripts/validate.py` checks hex syntax, duplicates,
sRGB gamut, the rising neutral ramp, the anchor hues, accent separation, the
kinship arcs, the contrast floor and slot coverage. `scripts/phosphor_colour.py`
holds the sRGB, HSL, OKLab and OKLCH conversions with no third-party
dependency.

Generation is deterministic: running it twice without an edit leaves the
working tree clean.

### Documentation

English, Spanish and Latin, under `i18n/`. The palette tables in each language
are generated, so the colours and the figures cannot drift between them.

## 1.0.0

Two Base16 schemes, documented in `README.md` with palette tables and a YAML
block each.
