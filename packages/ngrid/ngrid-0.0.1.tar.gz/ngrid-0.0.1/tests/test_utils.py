import unittest

from ngrid.utils import reduce_periodic


class TestReducePeriodic(unittest.TestCase):

    def test_point_to_right(self):

        interval = (1, 3)
        x = 4

        actual = reduce_periodic(*interval, 4.1)
        self.assertAlmostEqual(2.1, actual)

        actual = reduce_periodic(*interval, 6.1)
        self.assertAlmostEqual(2.1, actual)

        actual = reduce_periodic(*interval, 0.1)
        self.assertAlmostEqual(2.1, actual)

        actual = reduce_periodic(*interval, 0.1-2)
        self.assertAlmostEqual(2.1, actual)