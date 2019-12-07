from pynq.core.list import List


def test_any_returns_true_if_list_not_empty():
    assert List(['a']).any() is True


def test_any_returns_true_if_one_item_matching_predicate():
    assert List(['A', None, False, 1]).any(lambda x: x == 1) is True


def test_any_returns_false_if_list_empty():
    assert List([]).any() is False


def test_any_returns_false_if_no_item_matching_predicate():
    assert List(['A', None, False, 1]).any(lambda x: x == 2) is False

