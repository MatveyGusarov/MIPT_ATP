from simple_library_01.functions import is_leap


def test_not_leap():
    assert False == is_leap(2022)
    assert True == is_leap(400)
    assert False == is_leap(100)
    assert True == is_leap(4)
    assert "Year must be greater than 0" == is_leap(-1)
    