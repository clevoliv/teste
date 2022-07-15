from fuel import convert, gauge
import pytest

def main():

    test_convert()
    test_gauge()
    test_zero_div_err()
    test_value_err()

def test_convert():
    assert convert('1/1') == 100
    assert convert('99/100') == 99
    assert convert('1/100') == 1

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"

def test_zero_div_err():
    with pytest.raises(ZeroDivisionError):
        convert('1 / 0')
        convert('1/0')

def test_value_err():
    with pytest.raises(ValueError):
        convert('cat/dog')
