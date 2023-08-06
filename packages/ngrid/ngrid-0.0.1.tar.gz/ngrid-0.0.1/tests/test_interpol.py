import unittest

import numpy as np

from ngrid.interpol import LagrangeInterpolator


class TestLagrangeInterpolator(unittest.TestCase):

    def test_interpolate_equidistant(self):

        x = np.linspace(-1, 1, 20)
        f = x**2

        interpolator = LagrangeInterpolator(x)

        f_inter = interpolator.create_interpolant(f)

        self.assertAlmostEqual(
            0.5**2,
            f_inter(0.5)
        )


if __name__ == '__main__':
    unittest.main()