<!--
i18n/en/README.md
@guterion
CC-BY-SA-4.0
English documentation for the Phosphor palette
-->

<div align="center">

<img src="../../assets/flags/spqr.svg" alt="" height="14"> **[Latina](../la/README.md)** · <img src="../../assets/flags/burgundy.svg" alt="" height="14"> **[Español](../es/README.md)** · <img src="../../assets/flags/england.svg" alt="" height="14"> **English**

<img src="../../assets/phosphorus.svg" alt="" width="72" height="72">

# Phosphor

**A terminal colour palette with a warm neutral ramp and a green lean**

</div>

---

Seventeen variants ship as Base16 and Base24 schemes: the full palette, a Tint
and a Mono for each of the eight chromatic families. Every colour is designed
in OKLCH, and `src/phosphor.yaml` generates the rest.

## The palette

The canonical palette holds 32 colours: eight neutrals, and eight chromatic
families with a dim, a normal and a bright tone each.

<!-- palette:start -->
| slot | hex | role | okL | okC | okH | on base00 | on base01 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| base00 | <img src="../../assets/swatch/000000.svg" width="14" height="14" alt=""> `#000000` | background | 0.000 | 0.000 | — | — | 1.07:1 |
| base01 | <img src="../../assets/swatch/0C0C0B.svg" width="14" height="14" alt=""> `#0C0C0B` | status bars | 0.154 | 0.002 | 106.6° | 1.07:1 | — |
| base02 | <img src="../../assets/swatch/242321.svg" width="14" height="14" alt=""> `#242321` | selection | 0.256 | 0.004 | 84.6° | 1.34:1 | 1.25:1 |
| base03 | <img src="../../assets/swatch/43423E.svg" width="14" height="14" alt=""> `#43423E` | comments | 0.379 | 0.007 | 95.2° | 2.09:1 | 1.95:1 |
| base04 | <img src="../../assets/swatch/6A6862.svg" width="14" height="14" alt=""> `#6A6862` | dark foreground | 0.517 | 0.010 | 91.6° | 3.77:1 | 3.51:1 |
| base05 | <img src="../../assets/swatch/96948B.svg" width="14" height="14" alt=""> `#96948B` | foreground | 0.666 | 0.013 | 96.5° | 6.91:1 | 6.44:1 |
| base06 | <img src="../../assets/swatch/C8C4B8.svg" width="14" height="14" alt=""> `#C8C4B8` | light foreground | 0.820 | 0.017 | 91.6° | 12.04:1 | 11.22:1 |
| base07 | <img src="../../assets/swatch/FFFAEB.svg" width="14" height="14" alt=""> `#FFFAEB` | lightest | 0.985 | 0.020 | 91.6° | 20.13:1 | 18.76:1 |

| family | dim | normal | bright | okL | okC | okH | on base01 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| red | <img src="../../assets/swatch/A80215.svg" width="14" height="14" alt=""> `#A80215` | <img src="../../assets/swatch/DF212A.svg" width="14" height="14" alt=""> `#DF212A` | <img src="../../assets/swatch/FF4C49.svg" width="14" height="14" alt=""> `#FF4C49` | 0.580 | 0.220 | 26.0° | 4.09:1 |
| orange | <img src="../../assets/swatch/9A3D01.svg" width="14" height="14" alt=""> `#9A3D01` | <img src="../../assets/swatch/D05502.svg" width="14" height="14" alt=""> `#D05502` | <img src="../../assets/swatch/F07232.svg" width="14" height="14" alt=""> `#F07232` | 0.601 | 0.172 | 44.6° | 4.64:1 |
| yellow | <img src="../../assets/swatch/9B6902.svg" width="14" height="14" alt=""> `#9B6902` | <img src="../../assets/swatch/C98A04.svg" width="14" height="14" alt=""> `#C98A04` | <img src="../../assets/swatch/E7A739.svg" width="14" height="14" alt=""> `#E7A739` | 0.679 | 0.142 | 76.3° | 6.64:1 |
| green | <img src="../../assets/swatch/669603.svg" width="14" height="14" alt=""> `#669603` | <img src="../../assets/swatch/83BE05.svg" width="14" height="14" alt=""> `#83BE05` | <img src="../../assets/swatch/9DDB3C.svg" width="14" height="14" alt=""> `#9DDB3C` | 0.733 | 0.192 | 128.6° | 8.70:1 |
| cyan | <img src="../../assets/swatch/039750.svg" width="14" height="14" alt=""> `#039750` | <img src="../../assets/swatch/06C268.svg" width="14" height="14" alt=""> `#06C268` | <img src="../../assets/swatch/44E084.svg" width="14" height="14" alt=""> `#44E084` | 0.714 | 0.183 | 152.9° | 8.32:1 |
| blue | <img src="../../assets/swatch/0263A4.svg" width="14" height="14" alt=""> `#0263A4` | <img src="../../assets/swatch/1687D9.svg" width="14" height="14" alt=""> `#1687D9` | <img src="../../assets/swatch/3EA4F8.svg" width="14" height="14" alt=""> `#3EA4F8` | 0.607 | 0.155 | 247.5° | 5.13:1 |
| violet | <img src="../../assets/swatch/6E02CD.svg" width="14" height="14" alt=""> `#6E02CD` | <img src="../../assets/swatch/9041F9.svg" width="14" height="14" alt=""> `#9041F9` | <img src="../../assets/swatch/A573FF.svg" width="14" height="14" alt=""> `#A573FF` | 0.580 | 0.253 | 297.3° | 4.02:1 |
| magenta | <img src="../../assets/swatch/A20265.svg" width="14" height="14" alt=""> `#A20265` | <img src="../../assets/swatch/D5268A.svg" width="14" height="14" alt=""> `#D5268A` | <img src="../../assets/swatch/F64AA6.svg" width="14" height="14" alt=""> `#F64AA6` | 0.587 | 0.222 | 352.0° | 4.17:1 |
<!-- palette:end -->

## Design

### The green core

Three hues are fixed and carry the identity of the scheme: the yellow at
OKLCH 76.3°, the lime green at 128.6°, and the spring green at 152.9° that the
scheme calls cyan. The name is inherited from the ANSI slot the colour fills;
the colour is a spring green and it is deliberate.

Two accents therefore sit within 24° of each other in the green band, and the
wheel carries a 94° gap where a cyan would go. The scheme leans green; the
neutral ramp leans warm.

### The other five hues

Red, orange, blue, violet and magenta are placed by a constrained search. The
search maximises the smallest distance between any two accents, and it holds
each hue inside the band its name occupies, so every family keeps its name.

The smallest distance between two accents is **0.082 ΔE**, between green and
cyan. Both are fixed, so that figure is the ceiling the anchors set.

### Perceptual lightness

Every colour is designed in OKLCH, where a change in the lightness number
matches a change in the lightness a reader sees. The accents span 0.20 of OKLab
lightness, which keeps them distinct from each other and keeps each of them
distinct from the neutral ramp behind it.

The dim and bright tones sit at −0.12 and +0.09 from the normal tone in that
same lightness. The bright tones fill the bright ANSI half that Base24 defines.

### Contrast

Accents are syntax colours, so the floor is the 3:1 ratio that WCAG sets for
large text and for interface components. The generator holds that floor as a
constraint: it raises the lightness of any colour that sits below it. Five of
the eight accents also clear 4.5:1, and those five carry body text.

## Tint

A Tint rotates every hue part of the way towards one target, so the whole
scheme leans towards one family while keeping its variety.

A rotated slot may change identity, and the new colour must be a relative of
the one it replaced. The red slot accepts a brown, an orange or a purple. The
green slot accepts a yellow-green, a cyan or a blue. `src/phosphor.yaml`
records the arc each family may occupy, and `scripts/validate.py` holds every
variant to it.

The strength of a Tint is derived. It is the largest rotation that keeps all
eight slots related to their origin, and keeps the families at least three
quarters as far apart as the full palette holds them. Each variant therefore
reaches its own strength, and the rule that stops it differs:

| variant | strength | stopped by |
| --- | --- | --- |
| Tint Green | 0.639 | separation floor |
| Tint Yellow | 0.595 | violet leaves its arc |
| Tint Orange | 0.519 | green leaves its arc |
| Tint Blue | 0.460 | yellow leaves its arc |
| Tint Red | 0.425 | green leaves its arc |
| Tint Magenta | 0.319 | green leaves its arc |
| Tint Cyan | 0.279 | separation floor |
| Tint Violet | 0.261 | yellow leaves its arc |

Rotation moves the hues closer together, so a second pass spreads the lightness
of the slots that moved. Lightness carries the separation that hue gives up.

## Mono

A Mono variant holds one hue across every chromatic slot, within a drift of
±10°, and separates the semantic families by OKLab lightness and chroma alone.
Mono Green takes the hue of `#47D813`.

Eight roles inside one hue sit closer together than eight roles spread around
the wheel: the closest pair in a Mono variant measures about 0.031 ΔE, against
0.082 in the full palette. A Mono buys coherence and pays in distinguishability.
That belongs to monochromy itself, and `scripts/validate.py` reports it.

## Variants

<!-- variants:start -->
| variant | scheme | strength |
| --- | --- | --- |
| Phosphor | `phosphor` | — |
| Phosphor Tint Red | `phosphor-tint-red` | 0.425 |
| Phosphor Tint Orange | `phosphor-tint-orange` | 0.519 |
| Phosphor Tint Yellow | `phosphor-tint-yellow` | 0.595 |
| Phosphor Tint Green | `phosphor-tint-green` | 0.639 |
| Phosphor Tint Cyan | `phosphor-tint-cyan` | 0.279 |
| Phosphor Tint Blue | `phosphor-tint-blue` | 0.460 |
| Phosphor Tint Violet | `phosphor-tint-violet` | 0.261 |
| Phosphor Tint Magenta | `phosphor-tint-magenta` | 0.319 |
| Phosphor Mono Red | `phosphor-mono-red` | — |
| Phosphor Mono Orange | `phosphor-mono-orange` | — |
| Phosphor Mono Yellow | `phosphor-mono-yellow` | — |
| Phosphor Mono Green | `phosphor-mono-green` | — |
| Phosphor Mono Cyan | `phosphor-mono-cyan` | — |
| Phosphor Mono Blue | `phosphor-mono-blue` | — |
| Phosphor Mono Violet | `phosphor-mono-violet` | — |
| Phosphor Mono Magenta | `phosphor-mono-magenta` | — |
<!-- variants:end -->

## Standards

`src/phosphor.yaml` is the canonical palette. Base16 and Base24 are
compatibility representations generated from it.

**Base24** carries eighteen slots, base00 to base17, and includes the bright
ANSI colours. The three tones map onto it directly.

**Base16** carries sixteen. Two of them hold a colour the specification names
differently: base0E holds violet where the specification says magenta, and
base0F holds magenta where it says dark red or brown. Phosphor keeps eight
chromatic families, and Base16 has room for six plus an orange, so the mapping
is written down in `src/phosphor.yaml` under `mapping`.

## Formats

| path | contents |
| --- | --- |
| `src/phosphor.yaml` | the canonical palette and every derivation rule |
| `schemes/base16/` | 17 Base16 schemes |
| `schemes/base24/` | 17 Base24 schemes |
| `dist/json/phosphor.json` | every variant, with OKLCH and contrast figures |
| `dist/css/phosphor.css` | custom properties, one block per variant |
| `assets/` | the palette images and the swatches |

Application themes come from the [tinted-theming][tt] builder. Point it at a
scheme file here, and it produces the theme for Alacritty, Kitty, WezTerm,
Neovim, tmux and the others, from templates their maintainers keep current.

[tt]: https://github.com/tinted-theming/home

## Use

Copy a scheme from `schemes/base24/` into the tool that reads Base24 schemes,
or take the hex values from `dist/json/phosphor.json`.

For a web page, link the stylesheet and name the variant on the root element:

```html
<link rel="stylesheet" href="dist/css/phosphor.css">
<html data-phosphor="phosphor-tint-green">
```

The full palette is defined on bare `:root`, so a page that names no variant
gets Phosphor itself.

## Build

The scripts need [uv][uv]. Each one declares its own dependencies, so the
environment needs no preparation.

```sh
uv run scripts/generate.py    # rewrite schemes/, dist/, assets/ and the tables
uv run scripts/validate.py    # check the source and everything generated
```

`src/phosphor.yaml` is the only file a person edits. Generation is
deterministic: run it twice without an edit, and the working tree stays clean.

The validator checks the hex syntax, the duplicate colours, the sRGB gamut, the
rising neutral ramp, the anchor hues, the accent separation of every variant,
the kinship arcs of every Tint, the contrast floor, and the slot coverage in
all 34 scheme files.

[uv]: https://docs.astral.sh/uv/

## Contribute

Open an issue before you propose a colour, and bring the measurements: the
OKLCH figures, the contrast on base01, and the distance to the neighbouring
accents. The measurements rank the options and show where one of them fails.
The eye picks the winner.

[CONTRIBUTING.md](../../CONTRIBUTING.md) holds the constraints a proposal works
inside, the commit conventions and the translation rules.

## Licence

[CC-BY-SA-4.0 or later](../../LICENCE.md), by
[@guterion](https://github.com/guterion).
