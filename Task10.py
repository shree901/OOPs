class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


for i in Counter(1, 5):
    print(i)
