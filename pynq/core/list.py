class List:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return iter(self.wrapped)

    def __len__(self):
        return len(self.wrapped)

    def __eq__(self, other):
        if other is List:
            return self.wrapped == other.wrapped
        return self.wrapped == other

    def append(self, item):
        result = self.wrapped.copy()
        result.append(item)
        return List(result)

    def any(self, pred=None):
        if pred is None:
            return len(self) > 0

        for item in self:
            if pred(item):
                return True
        return False

    def all(self, pred):
        for item in self:
            if not pred(item):
                return False
        return True

    def aggregate(self, func):
        result = self.wrapped[0]

        for item in self.wrapped[1:]:
            result = func(result, item)
        return result

    def first(self, pred):
        for item in self:
            if pred(item):
                return item
        raise Exception('List contains no matching element.')

    def one(self):
        if len(self) != 1:
            raise Exception('List length is not one.')

        return self.wrapped[0]

    def select(self, selector):
        result = list()

        for item in self:
            result.append(selector(item))
        return result

    def where(self, pred):
        result = list()

        for item in self:
            if pred(item):
                result.append(item)
        return List(result)

    def sum(self, converter=lambda x: x):
        result = 0

        for item in self:
            result += converter(item)
        return result

    def average(self, converter):
        return sum(self, converter) / len(self)

    def concat(self, other):
        result = self.copy()
        result.extend(other)
        return result

    def distinct(self):
        return list(set(self))

    def last(self, predicate=lambda x: x):
        for item in self[::-1]:
            if predicate(item):
                return item
        raise Exception('List contains no matching element.')
