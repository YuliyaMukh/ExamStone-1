from prod.model.entity import *

class Sorter:

    @staticmethod
    def sort(necklace):
        if isinstance(necklace, Necklace):
            for i in range(len(necklace) - 1):
                for index in range(len(necklace) - 1 - i):
                    if necklace[index].carat > necklace[index + 1].carat:
                        temp = necklace[index]
                        necklace[index] = necklace[index + 1]
                        necklace[index + 1] = temp

# necklace = Necklace(5)
# necklace.add(Stone(4, 1, 0.5))
# necklace.add(Stone(4, 10, 1))
# necklace.add(Stone(8, 1, 0.8))
# necklace.add(Stone(9, 1, 5))
#
# print("\nBefore sorting: ")
# print(necklace)
#
# Sorter.sort(necklace)
#
# print("\nAfter sorting: ")
# print(necklace)