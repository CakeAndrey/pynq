from core.decorators import extends


@extends(list)
def where(self, pred):
    result = list()

    for item in self:
        if pred(item):
            result.append(item)

    return result


@extends(list)
def one(self):
    if len(self) != 1:
        raise Exception('Sequence length is not one.')

    return self[0]


@extends(list)
def first(self, pred):
    for item in self:
        if pred(item):
            return item
    raise Exception('Sequence contains no matching element.')


@extends(list)
def all(self, pred):
    for item in self:
        if not pred(item):
            return False
    return True
