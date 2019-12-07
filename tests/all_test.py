from pynq.core.list import List


def test_all_returns_true_if_all_items_matching_predicate():
    actual = List([
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
        'Mordor'
    ]).all(lambda x: x[0].isupper())

    assert actual is True


def test_all_returns_false_if_one_item_does_not_matching_predicate():
    actual = List([
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
        'Mordor',
        'city'
    ]).all(lambda x: x[0].isupper())


    assert actual is False
