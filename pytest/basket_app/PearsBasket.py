class PearsBasket:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.amount)

    def __floordiv__(self, number):
        whole = self.amount // number
        rest = self.amount % number
        res = [PearsBasket(whole) for _ in range(whole)]
        if rest > 0: res.append(PearsBasket(rest))
        return res

    def __add__(self, other):
        return PearsBasket(self.amount + other.amount)

    def __mod__(self, amount):
        return self.amount % amount

    def __sub__(self, amount):
        self.amount -= amount
