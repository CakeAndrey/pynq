from src.core import extensions


def test_where_returns_integers_less_then_50():
    list = []

    for i in range(100):
        list.append(i)

    actual = list.where(lambda x: x < 50)

    for item in actual:
        assert item < 50


def test_where_returns_words():
    list = ['My name is... What?',
           'Knife',
           'No rest for the wicked',
           'Chair',
           'Avada',
           'Kedavra'
]

    actual = list.where(lambda x: ' ' not in x)
    expected = [
        'Knife',
        'Chair',
        'Avada',
        'Kedavra'
    ]

    assert actual == expected


def test_where_returns_strings_started_with_capital_letter():
    list = [
        'String',
        None,
        123,
        'another string',
        lambda x: x + 1
    ]

    actual = list\
        .where(lambda x: type(x) is str)\
        .where(lambda x: x[0].isupper())
    expected = [
        'String'
    ]

    assert actual == expected
