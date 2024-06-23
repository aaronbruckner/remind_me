import pytest

from tests.given import Given

@pytest.mark.parametrize('expected_length', [1, 2, 3])
def test_alpha_num_str_returns_str_of_correct_length(given: Given, expected_length: int):
    assert len(given.alpha_num_str(expected_length)) == expected_length

def test_alpha_num_str_returns_random_string(given: Given):
    s1 = given.alpha_num_str(100)
    s2 = given.alpha_num_str(100)
    
    assert s1 != s2