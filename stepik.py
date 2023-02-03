class MyList(list):
    def __iter__(self):
        return DoublePairIterator(self)


class DoublePairIterator:

    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if len(self.lst) > self.i:
            self.i += 2
            try:
                return self.lst[self.i - 2], self.lst[self.i - 1]
            except IndexError:
                return f"Последний элемент списка не нашел себе пару  {self.lst[-1]}"
        else:
            raise StopIteration


