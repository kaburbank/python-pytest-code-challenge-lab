import pytest
from lib.palindrome import longest_palindromic_substring

@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("babad", ("bab", "aba")),
        ("cbbd", ("bb",)),
        ("a", ("a",)),
        ("ac", ("a", "c")),
        ("racecar", ("racecar",)),
        ("", ("",)),
        ("aaaaa", ("aaaaa",)),
        ("abcdefg", tuple("abcdefg")),
        ("abccba", ("abccba",)),
        ("abacdfgdcaba", ("aba", "cdc")),
        ("1234321", ("1234321",)),
        ("abbahello", ("abba",)),
        ("helloracecar", ("racecar",)),
        ("aa", ("aa",)),
        ("ab", ("a", "b")),
    ]
)
def test_longest_palindromic_substring(input_str, expected):
    result = longest_palindromic_substring(input_str)
    if input_str != "":
        assert result is not None, f"For input '{input_str}', got None, expected one of {expected}"
    assert result in expected, f"For input '{input_str}', got '{result}', expected one of {expected}"
