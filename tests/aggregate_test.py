from pynq.core.list import List


def test_aggregate_returns_list_sum():
    actual = List([1, 2, 3, 4, 5]).aggregate(lambda x, y: x + y)
    expected = 1 + 2 + 3 + 4 + 5

    assert actual == expected
