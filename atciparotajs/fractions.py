from __future__ import annotations

from atciparotajs.cardinals import cardinal

# Buckets that indicate feminine gender
_FEMININE_BUCKETS = {2, 3, 5, 12, 13}


# For plural buckets the integer part stays in nominative singular (gender-matched);
# for singular/accusative buckets the integer part follows the same case as the noun.
_PLURAL_BUCKETS = {3, 8, 9, 11}


def fraction(integer_part: int, decimal_str: str, bucket: int = 1,
             int_bucket: int | None = None) -> str:
    gender_bucket = 2 if bucket in _FEMININE_BUCKETS else 1
    if int_bucket is None:
        int_bucket = gender_bucket if bucket in _PLURAL_BUCKETS else bucket
    # Leading zeros are spoken digit by digit, so "0,06" and "0,6" stay distinct
    lead_zeros = len(decimal_str) - len(decimal_str.lstrip("0"))
    rest = decimal_str[lead_zeros:]
    dec_words = [cardinal(0, bucket)] * lead_zeros
    if rest:
        dec_words.append(cardinal(int(rest), bucket))
    return " ".join([cardinal(integer_part, int_bucket), "komats", *dec_words])
