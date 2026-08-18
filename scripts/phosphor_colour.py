"""
phosphor_colour.py
@fraxgut
CC-BY-SA-4.0
Colour-space conversions and metrics for the Phosphor palette work.

The module holds sRGB, HSL, OKLab and OKLCH conversions, a gamut mapper
that reduces chroma until the colour fits in sRGB, and the WCAG contrast
metric. It has no third-party dependencies.
"""

from functools import lru_cache
from math import atan2, cos, degrees, radians, sin, sqrt

# --- sRGB TRANSFER FUNCTIONS ---
# The sRGB electro-optical transfer function and its inverse. All linear
# values in this module are scene-linear sRGB in the range 0 to 1.


def srgb_to_linear(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c: float) -> float:
    return c * 12.92 if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def hex_to_rgb(h: str) -> tuple:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple) -> str:
    return "#" + "".join(f"{round(max(0.0, min(1.0, c)) * 255):02X}" for c in rgb)


# --- OKLAB AND OKLCH ---
# The matrices come from Björn Ottosson's definition of OKLab. OKLCH is
# the cylindrical form of OKLab: L stays, C is the chroma radius and H is
# the hue angle in degrees.


def rgb_to_oklab(rgb: tuple) -> tuple:
    r, g, b = (srgb_to_linear(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (v ** (1 / 3) if v >= 0 else -((-v) ** (1 / 3)) for v in (l, m, s))
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def oklab_to_rgb(lab: tuple) -> tuple:
    L, a, b = lab
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = (v**3 for v in (l_, m_, s_))
    lin = (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )
    return tuple(linear_to_srgb(c) for c in lin)


def oklab_to_oklch(lab: tuple) -> tuple:
    L, a, b = lab
    return (L, sqrt(a * a + b * b), degrees(atan2(b, a)) % 360)


def oklch_to_oklab(lch: tuple) -> tuple:
    L, C, H = lch
    return (L, C * cos(radians(H)), C * sin(radians(H)))


def hex_to_oklch(h: str) -> tuple:
    return oklab_to_oklch(rgb_to_oklab(hex_to_rgb(h)))


# --- GAMUT MAPPING ---
# A requested OKLCH triple frequently falls outside sRGB. The mapper keeps
# L and H, and reduces C by bisection until the colour fits. This follows
# the approach of CSS Color 4, which prefers a chroma loss over a hue or
# lightness shift.

_EPS = 1e-4


def in_gamut(rgb: tuple) -> bool:
    return all(-_EPS <= c <= 1 + _EPS for c in rgb)


def oklch_to_rgb(lch: tuple, clip: bool = True) -> tuple:
    rgb = oklab_to_rgb(oklch_to_oklab(lch))
    if in_gamut(rgb) or not clip:
        return tuple(min(1.0, max(0.0, c)) for c in rgb)
    L, C, H = lch
    lo, hi = 0.0, C
    for _ in range(40):
        mid = (lo + hi) / 2
        if in_gamut(oklab_to_rgb(oklch_to_oklab((L, mid, H)))):
            lo = mid
        else:
            hi = mid
    rgb = oklab_to_rgb(oklch_to_oklab((L, lo, H)))
    return tuple(min(1.0, max(0.0, c)) for c in rgb)


def oklch_to_hex(lch: tuple) -> str:
    return rgb_to_hex(oklch_to_rgb(lch))


@lru_cache(maxsize=None)
def max_chroma(L: float, H: float) -> float:
    """Return the largest chroma that keeps (L, H) inside sRGB.

    The search runs inside every generator loop, so the results are
    cached. The function is pure, and the cache is what makes a full
    generation take seconds rather than a minute.
    """
    lo, hi = 0.0, 0.45
    for _ in range(40):
        mid = (lo + hi) / 2
        if in_gamut(oklab_to_rgb(oklch_to_oklab((L, mid, H)))):
            lo = mid
        else:
            hi = mid
    return lo


# --- LEGACY METRICS ---
# HSL describes how the version 1 palette was built. The relative
# luminance and the contrast ratio come from WCAG 2.


def rgb_to_hsl(rgb: tuple) -> tuple:
    r, g, b = rgb
    mx, mn = max(rgb), min(rgb)
    l = (mx + mn) / 2
    if mx == mn:
        return (0.0, 0.0, l * 100)
    d = mx - mn
    s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
    if mx == r:
        h = ((g - b) / d) % 6
    elif mx == g:
        h = (b - r) / d + 2
    else:
        h = (r - g) / d + 4
    return (h * 60 % 360, s * 100, l * 100)


def relative_luminance(rgb: tuple) -> float:
    r, g, b = (srgb_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(hex_a: str, hex_b: str) -> float:
    la = relative_luminance(hex_to_rgb(hex_a))
    lb = relative_luminance(hex_to_rgb(hex_b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def delta_e_ok(hex_a: str, hex_b: str) -> float:
    """Euclidean distance in OKLab, the native difference metric there."""
    a, b = rgb_to_oklab(hex_to_rgb(hex_a)), rgb_to_oklab(hex_to_rgb(hex_b))
    return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def hue_name(H: float) -> str:
    """Report the approximate colour name of an OKLCH hue angle."""
    bands = [
        (25, "pink-red"), (45, "red"), (70, "orange"), (100, "yellow"),
        (130, "yellow-green"), (160, "green"), (190, "spring green"),
        (220, "cyan"), (250, "azure"), (290, "blue"), (320, "violet"),
        (350, "magenta"), (360, "pink-red"),
    ]
    for limit, name in bands:
        if H < limit:
            return name
    return "pink-red"


# --- SELF-CHECK ---
# Run this file directly to verify the conversions against known anchors.
# The chain sRGB → OKLab → OKLCH → sRGB has enough steps that a transposed
# matrix coefficient stays invisible until a colour comes out wrong.
if __name__ == "__main__":
    # White sits at OKLab lightness 1, black at 0, mid grey near 0.5989.
    assert abs(rgb_to_oklab(hex_to_rgb("#FFFFFF"))[0] - 1.0) < 1e-6
    assert abs(rgb_to_oklab(hex_to_rgb("#000000"))[0]) < 1e-9
    assert abs(rgb_to_oklab(hex_to_rgb("#808080"))[0] - 0.5989) < 1e-3

    # A round trip through OKLCH returns the colour it started from.
    for h in ("#DF212A", "#83BE05", "#9041F9", "#0C0C0B", "#FFFAEB"):
        assert oklch_to_hex(hex_to_oklch(h)) == h, h

    # WCAG anchors: black on white is 21:1, and #777777 on white is 4.478:1.
    assert abs(contrast("#FFFFFF", "#000000") - 21.0) < 1e-6
    assert abs(contrast("#777777", "#FFFFFF") - 4.478) < 1e-3

    # The gamut mapper keeps lightness and hue, and gives up chroma. The
    # request below asks for more chroma than sRGB holds at that hue.
    L, C, H = hex_to_oklch(oklch_to_hex((0.60, 0.40, 297.0)))
    assert abs(L - 0.60) < 1e-2 and abs(H - 297.0) < 1.0 and C < 0.40

    # Hue names read from the angle, not from the slot the colour fills.
    assert hue_name(hex_to_oklch("#06C268")[2]) == "green"
    assert hue_name(hex_to_oklch("#DF212A")[2]) == "red"

    print("phosphor_colour: all checks passed")
