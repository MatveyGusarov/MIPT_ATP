from simple_library_01.functions import get_month_days


def test_get_month_days():
    assert 30 == get_month_days(1930, 10)
    assert 29 == get_month_days(400, 2)
    assert 28 == get_month_days(100, 2)
    assert 30 == get_month_days(3, 9)
    assert 31 == get_month_days(1, 1)
    assert "Month should be in range [1-12]" == get_month_days(1, 13)