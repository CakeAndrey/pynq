import pytest

from core.pynq import Pynq


def test_first_returns_value_when_seq_has_matching_value():
    list = [
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
        'Mordor'
    ]

    actual = Pynq(list).first(lambda x: x == 'Mordor')
    expected = 'Mordor'

    assert actual == expected


def test_first_raises_exception_if_seq_has_not_matching_value():
    list = [
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
        'Mordor'
    ]

    with pytest.raises(Exception):
        Pynq(list).first(lambda x: x == 'Shire')


def test_first_returns_value_if_seq_has_diff_types():
    list = [
        'string',
        True,
        None,
        123
    ]

    actual = Pynq(list).first(lambda x: x == 123)
    expected = 123

    assert actual == expected


