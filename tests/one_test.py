import pytest

from pynq.core.list import List


def test_one_returns_item_if_list_has_one_item():
    list = List(['Only you.'])

    actual = list.one()
    expected = 'Only you.'

    assert actual == expected


def test_one_raises_exception_if_list_has_not_one_item():
    list = List([
        'We',
        'are',
        'the',
        'champions'
    ])

    with pytest.raises(Exception):
        list.one()
