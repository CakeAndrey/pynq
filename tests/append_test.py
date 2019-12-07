from pynq.core.list import List


def test_append_created_new_list():
    actual = List([
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith',
    ]).append('asd')\
        .append('q')\

    assert 'asd' and 'q' in actual


def test_append_not_changing_old_list():
    actual = List([
        'Erebor',
        'Rivendell',
        'Gondor',
        'Isengard',
        'Minas Ithil',
        'Minas Tirith'])

    actual.append('asd')

    assert actual == ['Erebor', 'Rivendell', 'Gondor', 'Isengard', 'Minas Ithil', 'Minas Tirith']
