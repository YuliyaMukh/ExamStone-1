#Хочу заранее попросить пощение, за потраченое время, на проверку этого УЖАСА (мягко говоря),
#там все бред и ничего не работает,
#но ничего больше в данный момент представить я не в состонии(
#Надеюсь на минимум с натяжкой хватит

import unittest
from prod.model.entity import *
from prod.model.logic import *


class TestJeweler(unittest.TestCase):

    def test_calculate_total_price_basic(self):
        necklace = Necklace()
        necklace.add(Stone(1, 1, 1))
        necklace.add(Stone(2, 2, 1))
        necklace.add(Stone(1, 3, 1))
        expected = 12

        actual = Jeweler.calculate_total_price(necklace)

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_only_one_stone(self):
        necklace = Necklace()
        stone = Stone(1, 3, 1)
        necklace.add(stone)
        expected = stone.price

        actual = Jeweler.calculate_total_price(necklace)

        self.assertEqual(expected, actual)


    def test_calculate_total_price_with_empty_necklace(self):
        expected = 0

        actual = Jeweler.calculate_total_price(necklace)

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_incorrect_data(self):
        expected = -1

        actual = Jeweler.calculate_total_price(5)

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()


