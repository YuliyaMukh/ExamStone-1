from prod.model.entity import *


class Jeweler:
    FABULOUS = (5, 1000)
    NICE = (40, 700)
    SATISFACTORY = (75, 500)
    UNPRESENTABLE = (108, 200)

    @staticmethod

    def calculate_price(stone, carat):
        if isinstance(stone, Stone) and carat > 0:
            if stone.square <= Jeweler.FABULOUS[0]:
                price = Jeweler.FABULOUS[1]
            elif stone.square <= Jeweler.NICE[0]:
                price = Jeweler.NICE[1]
            elif stone.square <= Jeweler.SATISFACTORY[0]:
                price = Jeweler.SATISFACTORY[1]
            else:
                price = Jeweler.UNPRESENTABLE[1]

            price *= carat
            return price
        else:
            raise Exception()


    def calculate_total_price(necklaces):
        if not isinstance(necklaces, Necklace):
            return -1
        total = 0

        for i in range(1, len(necklaces)):

            stones = necklaces.__getitem__(i)
            if isinstance(stone, Stone):
                total += stone.price

        return total
