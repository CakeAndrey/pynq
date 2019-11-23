from core.pynq import Pynq


def test_all_returns_true_if_all_items_matching_predicate():
    list = [
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
        'Mordor'
    ]

    actual = Pynq(list).all(lambda x: x[0].isupper())
    expected = True

    assert actual == expected


def test_all_returns_false_if_one_item_does_not_matching_predicate():
    list = [
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
        'Mordor',
        'city'
    ]

    actual = Pynq(list).all(lambda x: x[0].isupper())
    expected = False

    assert actual == expected
