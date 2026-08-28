import re

_VALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Canonical Roman numeral form — rejects letter sequences that merely happen to
# consist of Roman letters (acronyms like "VID", "LIC", "DVD", "VIDM")
_CANONICAL = re.compile(
    r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
)


def roman_to_int(s: str) -> int:
    if not s or not all(c in _VALS for c in s):
        return -1
    result = 0
    prev = 0
    for c in reversed(s):
        curr = _VALS[c]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    if result <= 0:
        return -1
    return result


def is_valid_roman(s: str) -> bool:
    """True only for canonically written Roman numerals (I–MMMCMXCIX)."""
    return bool(s) and _CANONICAL.match(s) is not None
