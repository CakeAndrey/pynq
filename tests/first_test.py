from sympy.utilities import pytest

from pynq.core.list import List


def test_first_returns_value_when_list_has_matching_value():
    list = List([
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
        'Mordor'
    ])

    actual = list.first(lambda x: x == 'Mordor')
    expected = 'Mordor'

    assert actual == expected


def test_first_raises_exception_if_list_has_not_matching_value():
    list = List([
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
        'Mordor'
    ])

    with pytest.raises(Exception):
        list.first(lambda x: x == 'Shire')


def test_first_returns_value_if_list_has_diff_types():
    list = List([
        'string',
        True,
        None,
        123
    ])

    actual = list.first(lambda x: x == 123)
    expected = 123

    assert actual == expected


