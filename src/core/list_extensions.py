from src.core.decorators import extends


@extends(list)
def all(self, pred):
    for item in self:
        if not pred(item):
            return False
    return True


@extends(list)
def first(self, pred):
    for item in self:
        if pred(item):
            return item
    raise Exception('List contains no matching element.')


@extends(list)
def one(self):
    if len(self) != 1:
        raise Exception('List length is not one.')

    return self[0]


@extends(list)
def pynq_append(self, item):
    result = self.copy()
    result.append(item)
    return result


@extends(list)
def select(self, selector):
    result = list()

    for item in self:
        result.append(selector(item))
    return result


@extends(list)
def where(self, pred):
    result = list()

    for item in self:
        if pred(item):
            result.append(item)

    return result
