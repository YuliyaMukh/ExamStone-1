
class Stone:
    def __init__(self, color, clarity, carat, price=0):
        self._color = color
        self._clarity = clarity
        self._carat = carat
        self._price = price


    @property
    def square(self):
        return self._color * self._clarity

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if 1 <= color <= 9:
            self._color = color
        else:
            raise Exception()

    @color.deleter
    def color(self):
        del self._color


    @property
    def clarity(self):
        return self._clarity

    @clarity.setter
    def clarity(self, clarity):
        if 1 <= clarity <= 12:
            self._clarity = clarity
        else:
            raise Exception()

    @clarity.deleter
    def clarity(self):
        del self._clarity


    @property
    def carat(self):
        return self._carat

    @carat.setter
    def carat(self, carat):
        if carat > 0:
            self._carat = carat
        else:
            raise Exception()

    @carat.deleter
    def carat(self):
        del self._carat

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price > 0:
            self._price = price
        else:
            raise Exception()

    @price.deleter
    def price(self):
        del self._price



    def __str__(self):
        return f"color = {self._color}, clarity = {self._clarity}, carat = {self._carat}"


