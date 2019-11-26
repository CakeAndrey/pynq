import src.core.list_extensions


def test_aggregate_returns_list_sum():
    list = [1, 2, 3, 4, 5]

    actual = list.aggregate(lambda x, y: x + y)
    expected = 1 + 2 + 3 + 4 + 5

    assert actual == expected
