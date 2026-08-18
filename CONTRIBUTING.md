<!--
CONTRIBUTING.md
@fraxgut
CC-BY-SA-4.0
Contribution rules, commit conventions and translation synchronisation
-->

# Contributing

Thank you for your interest in this palette. This document gives the
conventions that the repository follows.

English is the infrastructure language of the repository. Directory names, file
names, commit messages, the source comments and this document are in English.
Inside `i18n/`, each language is equal.

## One file holds the colours

`src/phosphor.yaml` is the canonical palette and the only file a person edits.
Everything under `schemes/`, `dist/`, `assets/palette.svg`,
`assets/variants.svg` and `assets/swatch/` comes from it, along with the
palette tables inside every `README.md`.

```sh
uv run scripts/generate.py    # rewrite everything generated
uv run scripts/validate.py    # check the source and the output
```

Two conditions decide whether a change can be merged:

1. `scripts/validate.py` reports every check as passing.
2. Running `scripts/generate.py` twice leaves the working tree clean.

A pull request that edits a generated file receives the equivalent edit to
`src/phosphor.yaml` instead.

## Proposing a colour

Open an issue first, and bring the measurements: the OKLCH figures, the
contrast on base01, and the distance in ΔE to the neighbouring accents. The
measurements rank the options and show where one of them fails. The eye picks
the winner, so say what the change looks like in a terminal and in a syntax
highlighter, not only what it does to a number.

Four constraints hold, and a proposal works inside them:

**The three anchors keep their hue.** The yellow at OKLCH 76.3°, the lime green
at 128.6°, and the spring green at 152.9° that the scheme calls cyan. They
carry the identity of the scheme.

**The gap and the crowding stay.** Two accents sit within 24° of each other in
the green band, and the wheel carries a 94° gap where a cyan would go. Both
belong to the palette.

**0.082 ΔE is the ceiling on accent separation.** It is the distance between
green and cyan, and both are fixed, so no arrangement of the free hues raises
it.

**Every accent holds 3:1 against base01.** Accents are syntax colours, and that
is the ratio WCAG sets for large text and interface components. The generator
enforces it by raising lightness.

The five free hues — red, orange, blue, violet and magenta — move inside the
band their name occupies. A search in `scripts/generate.py` places them, so a
proposal that moves one changes the band in the source rather than the hex.

## Proposing a variant rule

The Tint and Mono rules live in `src/phosphor.yaml` under `derivation`.
Changing a parameter there changes every generated variant at once, so bring
the before and after of the whole set, not one variant.

The kinship arcs under `derivation.kinship` say which hues a rotated slot may
occupy. A slot may change identity into a relative of the colour it replaced:
the red slot accepts a brown, an orange or a purple, and the green slot accepts
a yellow-green, a cyan or a blue. Widening an arc is a design decision, so open
an issue for it.

The strength of each Tint follows from those arcs and from the separation
floor. It is derived rather than chosen, so a proposal that wants a different
strength argues for a different rule.

## Commit messages

The repository uses [Conventional Commits
1.0.0](https://www.conventionalcommits.org/en/v1.0.0/):

```
<type>(<scope>): <description>
```

Write the description in the imperative. Start it with a capital letter. Leave
off the full stop. Keep the subject line at about 50 characters, and at 72
characters as the limit.

### Types

| Type       | Use                                                          |
|------------|--------------------------------------------------------------|
| `feat`     | A new variant, export, format or capability.                 |
| `fix`      | A correction to a colour value, a mapping or a script.        |
| `docs`     | A change to the text that leaves the colours alone.          |
| `refactor` | A reorganisation that keeps the same output.                 |
| `test`     | A change to the validator or to a self-check.                |
| `chore`    | Repository maintenance: assets, licence, structure.          |
| `revert`   | A reversal of an earlier commit.                             |

### Scopes

Use the scope that names the part you changed:

```
fix(palette): Correct the violet lightness
feat(tint): Add the kinship arc for orange
feat(schemes): Add the Base24 export
docs(es): Make the Tint section clearer
docs(la): Correct the ablative in the standards section
test(colour): Add a gamut mapping anchor
chore(assets): Regenerate the palette preview
```

The scopes `palette`, `tint` and `mono` mark a change to the colours. The
scopes `schemes`, `exports` and `assets` mark generated output. The scopes
`en`, `es` and `la` mark a change to one language alone.

### The body

Add a body when the difference does not show the intention. Separate it from
the subject with one empty line, and wrap the text at about 72 characters.
Write what changed and why it had to change: the measurement, the constraint,
or the alternative you rejected.

### Breaking changes

Put `!` before the colon, or add a `BREAKING CHANGE:` footer. A breaking change
in this repository is a change to a published colour value, because a reader
has that value in their terminal configuration.

## Translations

The repository carries three languages, in this order of priority: Latin,
Spanish, English. Each holds one document, and `README.md` keeps its name
everywhere, because GitHub renders only that name when a reader opens the
directory.

| Language | Document |
|---|---|
| Latin | `i18n/la/README.md` |
| Spanish | `i18n/es/README.md` |
| English | `i18n/en/README.md` |

A change to the content of one document should also change the other two. If
you cannot translate your change, say so in the pull request and a maintainer
translates it. An untranslated change is better than no change.

The palette tables inside each document sit between `<!-- palette:start -->`
and `<!-- palette:end -->` markers, and the generator writes them. Leave the
markers in place and let the generator fill them.

### Adding a language

1. Create `i18n/<code>/README.md` with the two pairs of markers, `palette` and
   `variants`.
2. Add the table headings and the neutral ramp roles to `WORDS` and `ROLES` in
   `scripts/generate.py`.
3. Add the language marker to `assets/flags/`, and name its source and licence
   in `LICENCE.md`.
4. Add the language to the selector in `README.md` and in every translation.
5. Run the generator.

## Language rules

Each language has a fixed variety:

**Latin** is technical Neo-Latin, with the vocabulary of Vicipaedia Latina and
the Lexicon Recentis Latinitatis. Proper nouns and the names of the variants
stay undeclined.

**Spanish** is formal Chilean Spanish. It avoids chilenismos and Rioplatense
forms alike, uses `tú` or `usted` and never `vos`, and keeps every accent. It
follows UNE-ISO 24495-1 plain language: an explicit subject, the active voice,
and one idea per sentence.

**English** is Oxford English with British spelling, and it follows ASD-STE100
Simplified Technical English: the active voice, the simple tenses, one
instruction in one sentence.

Two rules hold in all three:

**Say what a thing is.** Define by presence. A sentence that needs "not" to
carry its meaning has a positive fact underneath it, and that fact is the one
to write.

**The palette stands on its own.** The documentation describes Phosphor as it
is. `CHANGELOG.md` is the one place where a release is described.

All three keep the same technical content. A translation that drops a figure or
a condition is incorrect.

## How to propose a change

1. Fork the repository.
2. Make a branch: `git checkout -b fix/violet-contrast`
3. Make your change in `src/phosphor.yaml` or in the documentation.
4. Run `uv run scripts/generate.py` and then `uv run scripts/validate.py`.
5. Commit with a conventional message, generated files included.
6. Push the branch and open a pull request. Say what you measured and what you
   looked at.

For a question or an idea, open an issue first. A discussion before the work
saves time for everybody.

## Licence

Your contributions are licensed under CC BY-SA 4.0 or later, the licence of
this repository. See [LICENCE.md](LICENCE.md).
