import pytest
from lib.palindrome import longest_palindromic_substring

def test_babad():
    result = longest_palindromic_substring("babad")
    assert result in ("bab", "aba")

def test_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_char():
    assert longest_palindromic_substring("a") == "a"

def test_ac():
    result = longest_palindromic_substring("ac")
    assert result in ("a", "c")

def test_racecar():
    assert longest_palindromic_substring("racecar") == "racecar"
