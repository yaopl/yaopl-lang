"""Check that every translated string keeps the printf placeholders of the English one.

Usage: check_placeholders.py <_base.yml> <Language.yml>...

YAOPL formats these strings with snprintf, so a translation must have the same conversions (%s, %d, %i, ...)
in the same order as the English text in YAOPL's lng_tmpl/_base.yml; otherwise the menu can print garbage
or crash. Untranslated and "same" entries show the English text and are not checked.
"""
import re
import sys

import yaml

# A printf conversion: flags, width, precision, length, type. "%%" is a literal percent sign.
CONVERSION = re.compile(r'%(?:%|[-+ #0]*(?:\d+|\*)?(?:\.(?:\d+|\*))?(?:hh|h|ll|l|L|q|j|z|t)?[diouxXeEfFgGaAcspn])')


def placeholders(text):
    return [m for m in CONVERSION.findall(text) if m != '%%']


def main():
    base = yaml.safe_load(open(sys.argv[1], encoding='utf-8'))
    english = {s['label']: s['string'] for s in base['gui_strings']}
    errors = 0
    for path in sys.argv[2:]:
        translations = yaml.safe_load(open(path, encoding='utf-8'))['translations']
        for label, text in translations.items():
            if not isinstance(text, str) or label not in english:
                continue
            want, got = placeholders(english[label]), placeholders(text)
            if got != want:
                print(f'{path}: {label}: placeholders {got} but English has {want}')
                errors += 1
    if errors:
        print(f'{errors} string(s) with wrong placeholders')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
