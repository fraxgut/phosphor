# Phosphor

A terminal colour palette built on a warm neutral ramp and eight saturated
chromatic families, with a green lean. It ships as Base16 and Base24 schemes,
in seventeen variants.

![The Phosphor palette](assets/palette.svg)

Phosphor was named Frankifuscus through version 1. See
[CHANGELOG.md](CHANGELOG.md) for what changed and why.

## Variants

One full palette, eight Tint variants and eight Mono variants. A Tint leans the
whole scheme towards one hue. A Mono holds one hue across every chromatic slot
and separates the families by lightness alone.

![The seventeen Phosphor variants](assets/variants.svg)

## Palette

### Neutral ramp

The ramp runs from true black to a warm ivory. Its steps in OKLab lightness
hold close to even, and the warm cast is what separates Phosphor from a
grey-based scheme. The ramp is unchanged from version 1.

| slot | hex | okL | contrast on base00 |
| --- | --- | --- | --- |
| base00 | `#000000` | 0.000 | — |
| base01 | `#0C0C0B` | 0.154 | 1.07:1 |
| base02 | `#242321` | 0.256 | 1.34:1 |
| base03 | `#43423E` | 0.379 | 2.09:1 |
| base04 | `#6A6862` | 0.517 | 3.77:1 |
| base05 | `#96948B` | 0.666 | 6.91:1 |
| base06 | `#C8C4B8` | 0.820 | 12.04:1 |
| base07 | `#FFFAEB` | 0.985 | 20.13:1 |

### Chromatic families

Eight families, each with a dim, a normal and a bright tone. The tones are
designed in OKLab lightness, at −0.12 and +0.09 from the normal tone. The
contrast column measures the normal tone against base01.

| family | dim | normal | bright | okL | okC | okH | contrast |
| --- | --- | --- | --- | --- | --- | --- | --- |
| red | `#A80215` | `#DF212A` | `#FF4C49` | 0.580 | 0.220 | 26.0° | 4.09:1 |
| orange | `#9A3D01` | `#D05502` | `#F07232` | 0.601 | 0.172 | 44.6° | 4.64:1 |
| yellow | `#9B6902` | `#C98A04` | `#E7A739` | 0.679 | 0.142 | 76.3° | 6.64:1 |
| green | `#669603` | `#83BE05` | `#9DDB3C` | 0.733 | 0.192 | 128.6° | 8.70:1 |
| cyan | `#039750` | `#06C268` | `#44E084` | 0.714 | 0.183 | 152.9° | 8.32:1 |
| blue | `#0263A4` | `#1687D9` | `#3EA4F8` | 0.607 | 0.155 | 247.5° | 5.13:1 |
| violet | `#6E02CD` | `#9041F9` | `#A573FF` | 0.580 | 0.253 | 297.3° | 4.02:1 |
| magenta | `#A20265` | `#D5268A` | `#F64AA6` | 0.587 | 0.222 | 352.0° | 4.17:1 |

## Design notes

### Three hues are fixed

The yellow, the green and the cyan hold their version 1 hue angle exactly. They
carry the identity of the scheme, and every generated variant works around
them.

The colour named cyan measures at OKLCH 153°, which is a spring green rather
than a cyan. The name is inherited and the colour is deliberate. Two accents
therefore sit within 24° of each other in the green band, and the wheel carries
a 94° gap where a cyan would go. That density is the theme, not a defect.

### The other five hues are placed by search

The red, orange, blue, violet and magenta were positioned by a constrained
search that maximises the smallest distance between any two accents, with each
hue confined to the band its name occupies. The search moves them very little:
the red holds its version 1 angle, the blue and violet do not rotate at all,
and the largest rotation is the magenta at 13.5°.

The smallest distance between two accents is **0.082 ΔE**, between green and
cyan. Both are fixed, so no arrangement of the free hues can raise it. That
figure is the price of the anchors and it is stated rather than hidden.

### Lightness is corrected, hue is preserved

Version 1 was built by holding HSL saturation and lightness constant and
turning the hue dial: every accent measured S = 83.8 %, L = 46.1 %. HSL
lightness is not perceptually uniform, so those identical figures produced
accents that ranged from 2.65:1 to 11.30:1 in real contrast, and a green
brighter than the base06 foreground.

Version 2 compresses the OKLab lightness spread from 0.32 to 0.20 and keeps the
order version 1 established. The violet rises from OKLab lightness 0.485 to
0.580, which takes it from 2.65:1 to 4.02:1 while holding its full chroma.

### Contrast

Accents are syntax colours rather than body text, so the floor is the 3:1 that
WCAG sets for large text and for interface components. The generator treats it
as a constraint and raises the lightness of any colour that misses it. Five of
the eight accents also clear 4.5:1 and are usable as body text.

## Tint

A Tint rotates every hue part of the way towards one target, so the scheme
leans without surrendering its variety.

A rotated slot may change identity. The red slot accepts a brown, an orange or
a purple, because each is a relative of the colour that was there. It does not
accept a yellow or a green, which have nothing to do with red. The green slot
accepts yellow-green, cyan and blue, and refuses orange and red for the same
reason. `src/phosphor.yaml` records the arc each family may occupy, and
`scripts/validate.py` checks every variant against it.

The strength of a Tint is derived, never chosen. It is the largest rotation
that keeps all eight slots related to their origin and keeps the families at
least three quarters as far apart as the full palette holds them. Each variant
therefore has its own strength, and the constraint that stops it differs.

| variant | slug | strength | stopped by |
| --- | --- | --- | --- |
| Phosphor Tint Green | `phosphor-tint-green` | 0.639 | separation floor |
| Phosphor Tint Yellow | `phosphor-tint-yellow` | 0.595 | violet loses kinship |
| Phosphor Tint Orange | `phosphor-tint-orange` | 0.519 | green loses kinship |
| Phosphor Tint Blue | `phosphor-tint-blue` | 0.460 | yellow loses kinship |
| Phosphor Tint Red | `phosphor-tint-red` | 0.425 | green loses kinship |
| Phosphor Tint Magenta | `phosphor-tint-magenta` | 0.319 | green loses kinship |
| Phosphor Tint Cyan | `phosphor-tint-cyan` | 0.279 | separation floor |
| Phosphor Tint Violet | `phosphor-tint-violet` | 0.261 | yellow loses kinship |

Rotation alone pushes together the pairs that were already close, so a second
pass redistributes the lightness of the slots that moved. Without it, red and
orange arrive 0.036 ΔE apart in Tint Green as two near-identical browns.

## Mono

A Mono variant holds one hue across every chromatic slot, within a drift budget
of ±10°, and separates the semantic families by OKLab lightness and chroma
alone. Mono Green reproduces the hue of `#47D813`, the colour most closely
associated with the project.

Eight roles inside one hue sit closer together than eight roles spread around
the wheel: the closest pair in a Mono variant measures about 0.031 ΔE against
0.082 in the full palette. A Mono buys coherence and pays in
distinguishability. That is inherent to monochromy rather than a fault in the
construction, and `scripts/validate.py` reports it as a warning.

## Standards

Phosphor's canonical palette is `src/phosphor.yaml`. Base16 and Base24 are
compatibility representations generated from it.

- **Base24** carries eighteen slots, base00 to base17, including the bright
  ANSI colours. The dim, normal and bright model maps onto it without loss.
- **Base16** carries sixteen. Two slots take a colour the specification names
  differently: base0E holds violet where the specification expects magenta, and
  base0F holds magenta where it expects a dark red or brown. The mapping is
  written down in `src/phosphor.yaml` under `mapping`.

## Formats

| path | contents |
| --- | --- |
| `src/phosphor.yaml` | the canonical palette and every derivation rule |
| `schemes/base16/` | 17 Base16 schemes |
| `schemes/base24/` | 17 Base24 schemes |
| `dist/json/phosphor.json` | every variant with OKLCH and contrast figures |
| `dist/css/phosphor.css` | custom properties, one block per variant |
| `assets/` | the SVG previews in this file |

Application themes come from the [tinted-theming][tt] builder rather than from
this repository. Point it at a scheme file here and it produces the theme for
Alacritty, Kitty, WezTerm, Neovim, tmux and the rest, from templates that their
maintainers keep current.

[tt]: https://github.com/tinted-theming/home

## Usage

Copy a scheme from `schemes/base24/` into the tool that consumes Base24
schemes, or take the hex values straight from `dist/json/phosphor.json`.

For a web page, link the stylesheet and set the variant on the root element:

```html
<link rel="stylesheet" href="dist/css/phosphor.css">
<html data-phosphor="phosphor-tint-green">
```

The full palette is defined on bare `:root`, so a page that sets no attribute
gets Phosphor itself.

## Building

The generator and the validator need [uv][uv]. Both scripts declare their own
dependencies, so no environment setup is required.

```sh
uv run scripts/generate.py    # rewrite schemes/, dist/ and assets/
uv run scripts/validate.py    # check the source and everything generated
```

`src/phosphor.yaml` is the only file a person edits. Everything under
`schemes/`, `dist/` and `assets/` is generated, and running the generator twice
without editing the source leaves the working tree clean.

The validator checks hex syntax, duplicate colours, sRGB gamut, the monotonic
neutral ramp, the anchor hues, the accent separation of every variant, the
kinship rule for every Tint, the contrast floor, and slot coverage in all 34
scheme files.

[uv]: https://docs.astral.sh/uv/

## Contributing

Open an issue before a colour change, and include the measurement that
motivates it: the OKLCH figures, the contrast, and the separation from the
neighbouring accents. A change that improves a number while making the palette
look worse is not an improvement.

Pull requests that edit a generated file are closed in favour of the equivalent
edit to `src/phosphor.yaml`.

## Licence

[CC-BY-SA-4.0](LICENCE), by [@fraxgut](https://github.com/fraxgut).
