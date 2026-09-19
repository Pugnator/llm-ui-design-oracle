# corpus/cli — sources of the `cli` module

The `cli` module was built from five bodies of guidance, all read in full on
2026-09-19. Two are archived here; three are not, for licence reasons, and
are quoted in `modules/cli.md` and `UI_EVIDENCE.md` with a hash of the exact
page that was read so a later reader can confirm they are looking at the
same text.

## Archived in this directory

| ID | Files | Licence |
|---|---|---|
| `GNU-STD` | `gnu-*.md` — GNU Coding Standards, chapter 4 *Program Behavior for All Programs*: 4.1 Non-GNU Standards, 4.2 Writing Robust Programs, 4.4 Formatting Error Messages, 4.5 Standards for Interfaces Generally, 4.8 Standards for Command Line Interfaces with 4.8.1 `--version` and 4.8.2 `--help`, 4.10 Table of Long Options, 4.12 Memory Usage, 4.13 File Usage | GNU Free Documentation License 1.3 or later, no Invariant Sections, no Cover Texts. Reproduced with attribution; page chrome removed, text unaltered |

`CLIG`, the Command Line Interface Guidelines (clig.dev, CC BY-SA 4.0), is
archived as `../writing/clig-dev.md` because the `writing` module used it
first; the `cli` module cites the same file.

## Read in full, quoted, not archived

| ID | Source | Read | SHA-256 of the page as fetched | Why not archived |
|---|---|---|---|---|
| `POSIX-12` | *The Open Group Base Specifications Issue 7, 2018 edition, IEEE Std 1003.1-2017*, Chapter 12 *Utility Conventions* — https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html | 2026-09-19 | `b5d0f5c6643a8fc0d702aeb812f2fa501b9480e38a31ef8dc1d52ef1d151d4f3` | Copyright IEEE and The Open Group; the online edition permits reading, not redistribution. The fourteen Utility Syntax Guidelines are short and are quoted where a rule uses them |
| `12F-CLI` | Jeff Dickey, *12 Factor CLI Apps*, Medium — https://jdxcode.medium.com/12-factor-cli-apps-dd3c227a0e46 | 2026-09-19 | `09bbab218a2e09b44f1603bf9f6bd270ae848316220c8f03ac7bf23f0203e00a` | Author's copyright; no licence stated. Quoted for commentary |
| `HEROKU-CLI` | *CLI Style Guide*, Heroku Dev Center, last updated 2025-01-31 — https://devcenter.heroku.com/articles/cli-style-guide | 2026-09-19 | `610c33adcbb05d20105a87c21fc23a67e4cab48cd46912a0e3a1835bc533ad3b` | Salesforce copyright; Dev Center terms do not grant redistribution. Quoted for commentary |

The hash is of the raw HTML response (`curl -sL` with a browser user-agent),
not of extracted text. If a re-fetch produces a different hash the page has
changed and the quotations should be re-verified against it.
