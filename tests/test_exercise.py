import pytest
from src.exercise import print_numbers_in_range

def test_exercise(capsys):
    numbers = [1,3,10,-1,5,0]
    print_numbers_in_range(numbers,0,5)
    out, err = capsys.readouterr()
    assert out == "The numbers in the range [0, 5]\n1\n3\n5\n0\n", "Should read:\n 'The numbers in the range [0, 5]\n1\n3\n5\n0\n'"
