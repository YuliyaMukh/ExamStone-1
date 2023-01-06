from prod.model.entity.stone import Stone
class Necklace:


    DEFAULT_SIZE = 9
    #
    def __init__(self, size=DEFAULT_SIZE):
        self._ls = []
        if size > 0:
            self._size = size
        else:
            self._size = Necklace.DEFAULT_SIZE

    @property
    def size(self):
        return self._size


    def __len__(self):
        return len(self._ls)


    def add(self, stone):
        if isinstance(stone, Stone):
            self._ls.append(stone)


    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            return self._ls[index]
        else:
            raise Exception()


    def __setitem__(self, index, value):
        if isinstance(index, int) and 0 <= index < len(self) and isinstance(value, Stone):
            self._ls[index] = value
        else:
            raise Exception()


    def __delitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            del self._ls[index]
        else:
            raise Exception()


    def __str__(self):
        if not self._ls:
            return "There are no stones in the necklace"
        else:
            msg = "Necklace list: \n"
            for stone in self._ls:
                msg += str(stone) + "\n"
            return msg




