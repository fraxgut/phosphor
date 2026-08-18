<!--
i18n/la/README.md
@fraxgut
CC-BY-SA-4.0
Latin documentation for the Phosphor palette
-->

<div align="center">

<img src="../../assets/flags/spqr.svg" alt="" height="14"> **Latina** · <img src="../../assets/flags/burgundy.svg" alt="" height="14"> **[Español](../es/README.md)** · <img src="../../assets/flags/england.svg" alt="" height="14"> **[English](../en/README.md)**

<img src="../../assets/phosphorus.svg" alt="" width="72" height="72">

# Phosphor

**Tabula colorum ad terminale, cum scala neutra calida et inclinatione viridi**

</div>

---

Septendecim varietates ut schemata Base16 et Base24 eduntur: tabula plena, et
unum Tint unumque Mono pro singulis octo familiis chromaticis. Omnis color in
OKLCH describitur, et `src/phosphor.yaml` cetera generat.

## Tabula colorum

Tabula canonica 32 colores continet: octo neutros, et octo familias chromaticas,
quarum quaeque tonum obscurum, medium et clarum habet.

<!-- palette:start -->
| sedes | hex | munus | okL | okC | okH | ad base00 | ad base01 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| base00 | <img src="../../assets/swatch/000000.svg" width="14" height="14" alt=""> `#000000` | fundus | 0.000 | 0.000 | — | — | 1.07:1 |
| base01 | <img src="../../assets/swatch/0C0C0B.svg" width="14" height="14" alt=""> `#0C0C0B` | tabulae status | 0.154 | 0.002 | 106.6° | 1.07:1 | — |
| base02 | <img src="../../assets/swatch/242321.svg" width="14" height="14" alt=""> `#242321` | electio | 0.256 | 0.004 | 84.6° | 1.34:1 | 1.25:1 |
| base03 | <img src="../../assets/swatch/43423E.svg" width="14" height="14" alt=""> `#43423E` | commentarii | 0.379 | 0.007 | 95.2° | 2.09:1 | 1.95:1 |
| base04 | <img src="../../assets/swatch/6A6862.svg" width="14" height="14" alt=""> `#6A6862` | prospectus obscurus | 0.517 | 0.010 | 91.6° | 3.77:1 | 3.51:1 |
| base05 | <img src="../../assets/swatch/96948B.svg" width="14" height="14" alt=""> `#96948B` | prospectus | 0.666 | 0.013 | 96.5° | 6.91:1 | 6.44:1 |
| base06 | <img src="../../assets/swatch/C8C4B8.svg" width="14" height="14" alt=""> `#C8C4B8` | prospectus clarus | 0.820 | 0.017 | 91.6° | 12.04:1 | 11.22:1 |
| base07 | <img src="../../assets/swatch/FFFAEB.svg" width="14" height="14" alt=""> `#FFFAEB` | clarissimus | 0.985 | 0.020 | 91.6° | 20.13:1 | 18.76:1 |

| familia | obscurus | medius | clarus | okL | okC | okH | ad base01 |
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

## Ratio

### Nucleus viridis

Tres tincturae fixae sunt et identitatem schematis sustinent: flavus in OKLCH
76,3°, viridis citreus in 128,6°, et viridis vernus in 152,9° quem schema
cyaneum appellat. Nomen ex sede ANSI venit quam color implet; color autem
viridis vernus est, atque de industria.

Ideo duo accentus intra 24° inter se in fascia viridi sedent, et rota hiatum
94° servat ubi cyaneus esset. Illa densitas signum tabulae est. Schema ad
viride inclinat, scala neutra ad calidum: haec duo simul Phosphor sunt.

### Quinque tincturae reliquae

Rubrum, aurantium, caeruleum, violaceum et magenta investigatio cum finibus
collocat. Investigatio distantiam minimam inter duos quoslibet accentus auget,
et unamquamque tincturam intra fasciam nominis sui tenet, ut omnis familia
nomen suum servet.

Distantia minima inter duos accentus **0,082 ΔE** est, inter viridem et
cyaneum. Uterque fixus est, ideo illud numerus fastigium est quod ancorae
ponunt.

### Claritas sensibilis

Omnis color in OKLCH describitur, ubi mutatio numeri claritatis mutationi
claritatis quae videtur respondet. Accentus 0,20 claritatis OKLab complectuntur,
quod eos et inter se et a scala neutra post ipsos distinctos servat.

Toni obscurus et clarus a tono medio 0,12 minus et 0,09 plus in eadem claritate
absunt. Toni clari dimidium ANSI clarum implent quod Base24 definit.

### Discrimen

Accentus colores syntaxis sunt, ideo fundamentum ratio 3:1 est quam WCAG
litteris magnis et partibus interfaciei statuit. Instrumentum generandi illud
fundamentum ut finem tractat: claritatem cuiuslibet coloris qui infra sedet
attollit. Quinque ex octo accentibus etiam 4,5:1 superant, et illi quinque
textum currentem ferunt.

## Tint

Tint omnes tincturas partem viae ad unum finem vertit, ita ut totum schema ad
unam familiam inclinet neque varietatem amittat.

Sedes versa identitatem mutare potest, et color novus cognatus esse debet eius
quem substituit. Sedes rubra fuscum, aurantium aut purpureum admittit. Sedes
viridis viridem flavescentem, cyaneum aut caeruleum admittit. `src/phosphor.yaml`
arcum quem quaeque familia occupare potest servat, et `scripts/validate.py`
omnes varietates ei subicit.

Vis unius Tint deducta est. Est conversio maxima quae octo sedes cum origine sua
cognatas servat, et familias saltem tribus quadrantibus distantiae quam tabula
plena obtinet separatas tenet. Ideo quaeque varietas vim suam attingit, et
regula quae eam sistit variat:

| varietas | vis | sistitur ab |
| --- | --- | --- |
| Tint Green | 0,639 | fundamento distantiae |
| Tint Yellow | 0,595 | violaceo arcum relinquente |
| Tint Orange | 0,519 | viridi arcum relinquente |
| Tint Blue | 0,460 | flavo arcum relinquente |
| Tint Red | 0,425 | viridi arcum relinquente |
| Tint Magenta | 0,319 | viridi arcum relinquente |
| Tint Cyan | 0,279 | fundamento distantiae |
| Tint Violet | 0,261 | flavo arcum relinquente |

Conversio tincturas inter se propius adducit, ideo altera vice claritas sedium
quae motae sunt distribuitur. Claritas distantiam quam tinctura cedit suscipit.

## Mono

Varietas Mono unam tincturam in omnibus sedibus chromaticis tenet, intra errorem
±10°, et familias significantes sola claritate et chromate OKLab separat. Mono
Green tincturam coloris `#47D813` sumit.

Octo munera intra unam tincturam propius sedent quam octo munera per rotam
sparsa: par proximum varietatis Mono circiter 0,031 ΔE metitur, contra 0,082
tabulae plenae. Mono concordiam emit et distinctione solvit. Hoc ad monochromiam
ipsam pertinet, et `scripts/validate.py` id nuntiat.

## Varietates

<!-- variants:start -->
| varietas | schema | vis |
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

## Normae

`src/phosphor.yaml` tabula canonica est. Base16 et Base24 repraesentationes
congruentiae sunt, ex ea generatae.

**Base24** duodeviginti sedes fert, a base00 usque ad base17, et colores ANSI
claros includit. Tres toni ei directe respondent.

**Base16** sedecim fert. Duae ex eis colorem servant quem norma aliter nominat:
base0E violaceum servat ubi norma magenta dicit, et base0F magenta servat ubi
rubrum obscurum aut fuscum dicit. Phosphor octo familias chromaticas tenet, et
Base16 sex cum aurantio capit, ideo respondentia in `src/phosphor.yaml` sub
`mapping` scripta est.

## Formae

| via | contenta |
| --- | --- |
| `src/phosphor.yaml` | tabula canonica et omnes regulae deducendi |
| `schemes/base16/` | 17 schemata Base16 |
| `schemes/base24/` | 17 schemata Base24 |
| `dist/json/phosphor.json` | quaeque varietas, cum numeris OKLCH et discriminis |
| `dist/css/phosphor.css` | proprietates propriae, unus locus pro varietate |
| `assets/` | imagines tabulae et exempla colorum |

Themata programmatum ex instrumento [tinted-theming][tt] veniunt. Id ad plicam
schematis huius loci dirige, et thema pro Alacritty, Kitty, WezTerm, Neovim,
tmux et ceteris efficit, ex exemplaribus quae curatores eorum recentia servant.

[tt]: https://github.com/tinted-theming/home

## Usus

Schema ex `schemes/base24/` in instrumentum quod schemata Base24 legit
transcribe, aut valores sedecimales ex `dist/json/phosphor.json` sume.

Pro pagina interretiali, folium stilorum necte et varietatem in elemento radicis
nomina:

```html
<link rel="stylesheet" href="dist/css/phosphor.css">
<html data-phosphor="phosphor-tint-green">
```

Tabula plena in `:root` nudo definitur, ideo pagina quae nullam varietatem
nominat Phosphor ipsum accipit.

## Aedificatio

Programmata [uv][uv] requirunt. Utrumque necessaria sua declarat, ideo ambitus
praeparatione non eget.

```sh
uv run scripts/generate.py    # schemes/, dist/, assets/ et tabulas rescribit
uv run scripts/validate.py    # fontem et omnia generata probat
```

`src/phosphor.yaml` sola plica est quam homo mutat. Generatio certa est:
bis eam curre sine mutatione, et arbor operis munda manet.

Probator syntaxin sedecimalem, colores geminatos, gamutum sRGB, ascensum scalae
neutrae, tincturas ancorarum, distantiam accentuum cuiusque varietatis, arcus
cognationis cuiusque Tint, fundamentum discriminis, et sedes impletas in omnibus
34 plicis schematum examinat.

[uv]: https://docs.astral.sh/uv/

## Conferre

Quaestionem aperi antequam colorem proponas, et mensuras adde: numeros OKLCH,
discrimen ad base01, et distantiam ad accentus vicinos. Mensurae optiones
ordinant et ostendunt ubi una cadat. Oculus victorem eligit.

[CONTRIBUTING.md](../../CONTRIBUTING.md) fines intra quos propositum laborat,
consuetudines commissionum et regulas translationis continet.

## Licentia

[CC-BY-SA-4.0 aut posterior](../../LICENCE.md), ab
[@fraxgut](https://github.com/fraxgut).
