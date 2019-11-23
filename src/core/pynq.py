class Pynq:
    def __init__(self, list):
        self._list = list

    def where(self, pred):
        result = list()

        for item in self._list:
            if pred(item):
                result.append(item)

        return Pynq(result)

    def one(self):
        if len(self._list) != 1:
            raise Exception('Sequence length is not one.')

        return self._list[0]

    def first(self, pred):
        for item in self._list:
            if pred(item):
                return item
        raise Exception('Sequence contains no matching element.')

    def all(self, pred):
        for item in self._list:
            if not pred(item):
                return False
        return True

    def __str__(self):
        return str(self._list)

    def __iter__(self):
        return self._list.__iter__()

    def __eq__(self, other):
        return self._list == (other._list if type(other) is Pynq else other)
