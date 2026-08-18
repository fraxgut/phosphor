# Changelog

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2.0.0

The project is now named **Phosphor**. It was named Frankifuscus through
version 1, and the green monochrome scheme that shipped as
`Frankifuscus Phosphor Mono` is now `Phosphor Mono Green`.

### The palette is the source of truth

Version 1 kept its colours in a Base16 YAML block inside `README.md`. The
canonical palette now lives in `src/phosphor.yaml`, and the Base16 and Base24
schemes are generated from it. Base16 became a compatibility export rather than
the definition.

The published YAML also used the legacy scheme format, with `scheme:` and
`slug:` keys and hex values written without a leading hash. The generated
schemes use the current format: `system`, `name`, `author`, `variant` and
`palette`, with `#RRGGBB` values.

### Colours

The neutral ramp is unchanged. Measured in OKLab it climbs from black to ivory
in steps that hold close to even, and it carries the warm cast that gives the
scheme its character.

The eight chromatic accents were corrected in OKLab lightness while keeping
their hue. Version 1 held HSL saturation and lightness constant at 83.8 % and
46.1 % for every accent, which is not perceptually uniform: the accents ranged
from 2.65:1 to 11.30:1 in real contrast against base01.

| family | 1.0 | 2.0 | ΔE | change |
| --- | --- | --- | --- | --- |
| red | `#D81323` | `#DF212A` | 0.020 | lightness only |
| orange | `#D84413` | `#D05502` | 0.034 | hue 36.4° → 44.6° |
| yellow | `#D89613` | `#C98A04` | 0.041 | lightness only, hue held |
| green | `#96D813` | `#83BE05` | 0.076 | lightness only, hue held |
| cyan | `#13D876` | `#06C268` | 0.062 | lightness only, hue held |
| blue | `#1386D8` | `#1687D9` | 0.003 | unchanged in practice |
| violet | `#7513D8` | `#9041F9` | 0.094 | lightness 0.485 → 0.580 |
| magenta | `#D81365` | `#D5268A` | 0.054 | hue 5.5° → 352.0° |

The violet is the largest correction and the one that mattered most: at 2.65:1
it was the only accent below the 3:1 floor for interface colour. It now reaches
4.02:1 and keeps its full chroma, because sRGB had the headroom.

The yellow, green and cyan hold their version 1 hue exactly. They are the
anchors of the scheme.

### Tones replace the ±25 % tables

Version 1 documented each colour with `Darken(25%)` and `Lighten(25%)` columns,
produced by mixing the RGB channels towards black or white. Those tables are
retired. Each family now carries a dim, a normal and a bright tone, designed in
OKLab lightness at −0.12 and +0.09 from the normal tone. The canonical palette
is 8 neutrals plus 8 families × 3 tones.

The bright tones fill the bright ANSI slots that Base24 defines, which the ±25 %
values were never intended for.

### Variants

Version 1 shipped one monochrome variant. Version 2 ships sixteen: a Tint and a
Mono for each of the eight families.

The Mono definition changed. `Frankifuscus Phosphor Mono` travelled 74.5° of
hue, from yellow-green through to cyan, while its accents crowded into 0.08 of
lightness: they changed colour and not brightness, which is the opposite of what
a monochrome variant should do. A Mono variant now holds one hue within ±10° and
separates the families by lightness and chroma. `#47D813` keeps its hue and
defines Mono Green.

Tint is new. It rotates every hue part of the way towards one target. Its
strength is derived from two rules rather than chosen: each slot must stay
related to the colour it replaced, and the families must stay at least three
quarters as far apart as the full palette holds them.

### Tooling

`scripts/generate.py` writes every scheme, export and preview from the source.
`scripts/validate.py` checks hex syntax, duplicates, sRGB gamut, the neutral
ramp, the anchor hues, accent separation, the kinship rule, the contrast floor
and slot coverage. `scripts/phosphor_colour.py` holds the sRGB, HSL, OKLab and
OKLCH conversions with no third-party dependency.

Generation is deterministic: running it twice without editing the source leaves
the working tree clean.

## 1.0.0

Frankifuscus, and Frankifuscus Phosphor Mono. Two Base16 schemes documented in
`README.md`, with palette tables, ±25 % variation tables and a YAML block each.
The version 1 values are preserved in this file and in the repository history.
