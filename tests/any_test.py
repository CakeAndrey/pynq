import src.core.list_extensions


def test_any_returns_true_if_list_not_empty():
    list = ['a']

    assert list.any() is True


def test_any_returns_true_if_one_item_matching_predicate():
    list = ['A', None, False, 1]

    assert list.any(lambda x: x == 1) is True


def test_any_returns_false_if_list_empty():
    list = []

    assert list.any() is False


def test_any_returns_false_if_no_item_matching_predicate():
    list = ['A', None, False, 1]

    assert list.any(lambda x: x == 2) is False

