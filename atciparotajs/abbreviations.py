import re

ABBREVIATIONS = {
    "gs.":    "gadsimts",
    "g.":     "gads",
    "km.":    "kilometrs",
    "m.":     "metrs",
    "kg.":    "kilograms",
    "mg.":    "miligrams",
    "ml.":    "mililitrs",
    "l.":     "litrs",
    "Nr.":    "numur",
    "nr.":    "numur",
    "lpp.":   "lappuse",
    "u.c.":   "un citi",
    "u.tml.": "un tamlīdzīgi",
    "t.i.":   "tas ir",
    "plkst.": "pulksten",
    "pr.Kr.": "pirms Kristus",
    "p.Kr.":  "pēc Kristus",
}

# A letter in any alphabet (unicode-aware, excludes digits and underscore)
_LETTER = r"[^\W\d_]"

# An abbreviation only counts when it is not glued to surrounding letters:
# "mežiem." must not match "m.", and "g.a" must not match "g.".
_ABBR_RE = re.compile(
    r"(?<!" + _LETTER + r")(?:"
    + "|".join(re.escape(a) for a in sorted(ABBREVIATIONS, key=len, reverse=True))
    + r")(?!" + _LETTER + r")"
)


def expand_abbreviations(text: str) -> str:
    return _ABBR_RE.sub(lambda m: ABBREVIATIONS[m.group(0)], text)
