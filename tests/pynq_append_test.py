from src.core import list_extensions


def test_pynq_append_created_new_list():
    list = [
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
    ]

    actual = list.pynq_append('asd').pynq_append('q')

    assert list and 'asd' and 'q' in actual


def test_pynq_append_not_changing_old_list():
    list = [
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
    ]

    list.pynq_append('asd')

    assert list == ['Erebor', 'Rivendell', 'Gondor', 'Isengard', 'Minas Ithil', 'Minas Tirith', ]
