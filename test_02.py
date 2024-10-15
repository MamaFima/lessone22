import pytest
from dz_test02 import count_vowels


def test_only_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0

def test_mixed_case_vowels():
    assert count_vowels("Hello World!") == 3
    assert count_vowels("PyTest IS great!") == 4
