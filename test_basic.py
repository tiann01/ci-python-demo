import pytest
from main import Calculator
from main import StringProcessor


@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_sub(calc):
    assert calc.sub(5, 2) == 3

def test_mul(calc):
    assert calc.mul(3, 4) == 12

def test_div(calc):
    assert calc.div(10, 2) == 5

def test_div_zero(calc):
    import pytest
    with pytest.raises(ValueError):
        calc.div(5, 0)


@pytest.fixture
def sp():
    return StringProcessor()

def test_reverse(sp):
    assert sp.reverse("abc") == "cba"

def test_is_palindrome(sp):
    assert sp.is_palindrome("Racecar")
    assert not sp.is_palindrome("hello")

def test_count_vowels(sp):
    assert sp.count_vowels("hello") == 2


@pytest.fixture
def test_calc_and_string():
    calc = Calculator()
    sp = StringProcessor()

    result = calc.add(10, 5)
    reversed_result = sp.reverse(str(result))
    assert reversed_result == "51"  # 15 翻转是 51

    assert sp.is_palindrome("madam")

