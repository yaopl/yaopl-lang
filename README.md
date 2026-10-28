# YAOPL translations

The menu translations of [YAOPL](https://github.com/yaopl/yaopl) (Yet Another Open PS2 Loader). This repository
is a fork of [Open-PS2-Loader-lang](https://github.com/ps2homebrew/Open-PS2-Loader-lang): it keeps all of
OPL's translations, adds the strings that only YAOPL has, and takes in upstream's changes regularly.

Every YAOPL build packs these files into `OPNPS2LD-LANGS-<version>.7z` on the
[`latest` release](https://github.com/yaopl/yaopl/releases/tag/latest). How to install a language is in the
[documentation](https://yaopl.github.io/yaopl/features/customizing/#languages).

## Files

- `<Language>.yml`: one file per language, UTF-8. The English text and the list of strings come from
  [`lng_tmpl/_base.yml`](https://github.com/yaopl/yaopl/blob/master/lng_tmpl/_base.yml) in the YAOPL
  repository; English itself has no file here.
- `thirdparty/font_<Language>.ttf` (or `.otf`): the font for a script that the built-in font does not cover.

Each string is in one of three states:

```yaml
  SAVE_CHANGES: Сохранить настройки   # translated
  MMCE:                               # intentionally the same as in English
  - same
  - original: MMCE
  UDPBD_GAMES:                        # not translated yet: YAOPL shows the English text
  - untranslated
  - original: UDPBD Games
```

To translate a string, replace its two lines `- untranslated` and `- original: …` with the text after the
colon. Use `same` for a string that should stay in English (device names, for example).

## Translating

1. Edit `<Language>.yml` (on GitHub: open the file, then the pencil icon) and open a pull request; its
   template lists what to check.
2. Keep `%s`, `%d`, `%i` and similar placeholders, in the same order. Keep the text short: the PS2 menu has
   little room, and long hints are cut off.
3. Put the text in quotes if it contains a colon followed by a space, or starts with `%`, `[`, `{`, `'`
   or `"`.
4. The CI of the pull request compiles every language against YAOPL; it must pass.

To see it on a console: the CI run of the pull request has a `compiled-languages` artifact with the `.lng`
files. Copy `lang_<Language>.lng` (and the font, if the language has one) to the `LNG` folder of a device or
to `mc0:OPL`, then pick it under Display Settings → Language.

A new language: copy an existing file, change `LOCALE` and the header comment, translate, and ask in the pull
request for the language to be added to YAOPL's `Makefile` (`TRANSLATIONS`).

## Maintenance

- **New strings in YAOPL.** When YAOPL adds strings to `lng_tmpl/_base.yml`, they are appended to every file
  here as `untranslated`, in the order of `_base.yml`, without reformatting the rest of the file. YAOPL's
  `lang_compiler.py --update_translation_yml` lists them, but it also rewraps the whole file, so only the
  entries it appends are kept.
- **Upstream.** `upstream` is `ps2homebrew/Open-PS2-Loader-lang`; its `main` is merged into ours
  (`git fetch upstream && git merge upstream/main`). Translations of strings that OPL also has can be offered
  upstream as well.
- YAOPL's build takes `main` of this repository (`download_lng.sh`), so a merged translation reaches the next
  YAOPL build on `latest`.

Problems with a translation: open an issue in [YAOPL](https://github.com/yaopl/yaopl/issues) and name the
language.
