<!--
CONTRIBUTING.md
@fraxgut
CC-BY-SA-4.0
Contribution rules, commit conventions and translation synchronisation
-->

# Contributing

English is the infrastructure language of this repository. Directory names,
file names, commit messages and source comments are in English. Inside
`i18n/`, each language is equal.

## One file has the colours

`src/phosphor.yaml` is the canonical palette. It is the only file that a
person edits. The generator writes `schemes/`, `dist/`, `assets/palette.svg`,
`assets/variants.svg`, `assets/swatch/` and the palette tables in each
`README.md`.

```sh
uv run scripts/generate.py    # write everything again
uv run scripts/validate.py    # check the source and the output
```

Your change must obey two conditions:

1. `scripts/validate.py` shows that each check passes.
2. A second run of `scripts/generate.py` leaves the working tree clean.

Edit the source file. If a pull request edits a generated file, the maintainer
makes the same edit in the source instead.

## To propose a colour

Open an issue first. Give these measurements:

- the OKLCH figures;
- the contrast on base01;
- the distance in ΔE to the two nearest accents.

The measurements rank the options. They also show where an option fails. The
eye then selects the winner, so tell us how the colour looks in a terminal and
in a syntax highlighter.

Four constraints apply. Work inside them:

| Constraint | Figure |
| --- | --- |
| The three anchor hues stay | yellow 76.3°, green 128.6°, cyan 152.9° |
| The green band keeps its density | two accents inside 24°, a 94° gap at cyan |
| Accent separation has a ceiling | 0.082 ΔE, between green and cyan |
| Each accent holds its contrast | 3:1 on base01 |

The five free hues are red, orange, blue, violet and magenta. Each one moves
inside the band of its own name. A search in `scripts/generate.py` puts them
there. To move one, change its band in the source file.

## To propose a variant rule

The Tint and Mono rules are in `src/phosphor.yaml`, under `derivation`. One
parameter changes every variant at the same time, so show the full set before
the change and after it.

The arcs under `derivation.kinship` give the hues that a rotated slot accepts.
A slot becomes a relative of the colour that it replaced: the red slot accepts
a brown, an orange or a purple. The arcs and the separation floor together
give the strength of each Tint. To get a different strength or a wider arc,
propose the rule, not the number.

## Commit messages

The repository uses [Conventional Commits
1.0.0](https://www.conventionalcommits.org/en/v1.0.0/):

```
<type>(<scope>): <description>
```

Write the description in the imperative. Start it with a capital letter. Leave
out the full stop. Keep the subject line at 50 characters, and at 72
characters as the limit.

| Type | Use it for |
| --- | --- |
| `feat` | A new variant, export or format. |
| `fix` | A correction to a colour, a mapping or a script. |
| `docs` | A change to the text that keeps the colours. |
| `refactor` | A new arrangement that keeps the same output. |
| `test` | A change to the validator or to a self-check. |
| `chore` | Repository maintenance: assets, licence, structure. |

The scopes `palette`, `tint` and `mono` mark a change to the colours. The
scopes `schemes`, `exports` and `assets` mark generated output. The scopes
`en`, `es` and `la` mark one language.

```
fix(palette): Correct the violet lightness
feat(tint): Add the kinship arc for orange
docs(es): Make the Tint section clearer
```

Add a body when the difference does not show the intention. Put one empty line
before it, and wrap the text at 72 characters. Give the measurement, the
constraint, or the alternative that you refused.

A breaking change here is a change to a published colour. A reader has that
colour in a terminal configuration. Put `!` before the colon, or add a
`BREAKING CHANGE:` footer.

## Translations

The repository has three languages: Latin in `i18n/la/`, Spanish in `i18n/es/`
and English in `i18n/en/`. Each one has a `README.md`, because GitHub shows
only that name when a reader opens a directory.

A change to one document also changes the other two. If you cannot translate
your change, say so in the pull request. A maintainer then translates it. An
untranslated change is better than no change.

The generator writes the palette tables between the `<!-- palette:start -->`
and `<!-- palette:end -->` markers. Keep the markers. The generator fills them.

### To add a language

1. Make `i18n/<code>/README.md`. Put the `palette` and `variants` markers in it.
2. Add the table headings and the ramp roles to `WORDS` and `ROLES` in
   `scripts/generate.py`.
3. Put the language marker in `assets/flags/`. Give its source and its licence
   in `LICENCE.md`.
4. Add the language to the selector in `README.md` and in each translation.
5. Run the generator.

## Language rules

Each language has one variety:

- **Latin** is technical Neo-Latin, with the vocabulary of Vicipaedia Latina
  and the Lexicon Recentis Latinitatis. Proper nouns and variant names stay
  undeclined.
- **Spanish** is formal Chilean Spanish, and it follows UNE-ISO 24495-1: an
  explicit subject, the active voice, one idea in one sentence. It keeps each
  accent.
- **English** is Oxford English with British spelling, and it follows
  ASD-STE100: the active voice, the simple tenses, one instruction in one
  sentence.

Two rules apply to all three:

- **Say what a thing is.** Define by presence. A sentence that needs "not" for
  its meaning has a positive fact below it. Write that fact.
- **The palette stands alone.** The documentation describes Phosphor as it is
  today. `CHANGELOG.md` is the one place that describes a release.

All three keep the same technical content. A translation that drops a figure
or a condition is incorrect.

## To propose a change

1. Fork the repository.
2. Make a branch: `git checkout -b fix/violet-contrast`.
3. Edit `src/phosphor.yaml` or the documentation.
4. Run `uv run scripts/generate.py`.
5. Run `uv run scripts/validate.py`.
6. Commit with a conventional message. Include the generated files.
7. Push the branch. Open a pull request. Say what you measured and what you
   looked at.

For a question or an idea, open an issue first.

## Licence

Your contributions carry CC BY-SA 4.0 or later, the licence of this
repository. See [LICENCE.md](LICENCE.md).
