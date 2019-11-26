import src.core.list_extensions


def test_select_returns_values_as_strings():
    list = [
        123,
        True,
        None,
        'Aaa',
        {}
    ]

    actual = list.select(lambda x: str(x))
    expected = [
        str(123),
        str(True),
        str(None),
        str('Aaa'),
        str({})
    ]

    assert actual == expected


def test_select_not_changing_old_list():
    default = [
        123,
        True,
        None,
        'Aaa',
        {}
    ]

    list = default.copy()
    list.select(lambda x: str(x))

    assert list == default
