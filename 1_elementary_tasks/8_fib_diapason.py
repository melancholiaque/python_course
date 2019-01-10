class Fibs:

    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.value_ = None

    def __calc(self):
        a, b = 0, 1
        while a < self.high:
            if self.low <= a:
                yield a
            a, b = b, a+b

    @property
    def value(self):
        if self.value_ is None:
            self.value_ = list(self.__calc())
        return self.value_


print(', '.join(str(i) for i in Fibs(0, 10).value))
