from project import get_input, check_length, generate_password
import random

def test_get_input():
    try:
        assert get_input("y") == 'y'
        assert get_input("no") == 'y'
    except SystemExit:
        pass

def test_check_length():
    assert check_length("8") == 8
    try:
        assert check_length("5") == "Input a value equal or greater than 8."
        assert check_length("eight") == "You should input a whole number, not a word or written number."
    except SystemExit:
        pass

def test_generate_password():
    random.seed(1)
    assert generate_password(8) == "fpM^*5I5"