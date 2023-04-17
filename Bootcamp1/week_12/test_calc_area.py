import unittest
from src.calc_area import calc_area


class TestCalcArea(unittest.TestCase):
    def test_calc_area(self):
        """
        Test that the definition multiplies the height and width
        """

        height = 3
        width = 3

        result = calc_area(height, width)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()