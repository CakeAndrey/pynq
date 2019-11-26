from src.core.decorators import extends


@extends(list)
def any(self, pred=None):
    if pred is None:
        return len(self) > 0

    for item in self:
        if pred(item):
            return True
    return False


@extends(list)
def all(self, pred):
    for item in self:
        if not pred(item):
            return False
    return True


@extends(list)
def aggregate(self, func):
    result = self[0]

    for item in self[1:]:
        result = func(result, item)
    return result


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


@extends(list)
def sum(self, converter):
    result = 0

    for item in self:
        result += converter(item)
    return result


@extends(list)
def average(self, converter):
    return sum(self, converter) / len(self)


@extends(list)
def concat(self, other):
    result = self.copy()
    result.extend(other)
    return result
