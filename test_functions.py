from functions import salary, hello_who

def test_salary():
    assert salary(3, 2) == 8
    assert salary(3, 3) == 6