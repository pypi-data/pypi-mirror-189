import unittest

import matplotlib.pyplot as plt
import numpy as np
from numpy.testing import assert_array_almost_equal

from ngrid import ChebyshevGrid


class TestChebyshevCartesian(unittest.TestCase):

    def test_create_grid_1d_in_standard_interval(self):
        # Arrange
        domain = (-1, 1)
        npoints = 21
        x = np.cos(np.pi - np.arange(npoints) * np.pi / (npoints - 1))

        # Act
        grid = ChebyshevGrid(npoints, domain)

        # Assert
        assert_array_almost_equal(x, grid.x)

    def test_create_grid_1d_in_nonstandard_interval(self):
        # Arrange
        domain = (-2, 3)
        npoints = 6
        x = [-2., -1.52254249, -0.27254249, 1.27254249, 2.52254249, 3.]

        # Act
        grid = ChebyshevGrid(npoints, domain)

        # Assert
        assert_array_almost_equal(x, grid.x)

    def test_interpolate_grid(self):
        # Arrange
        domain = (-1, 1)
        npoints = 21
        grid = ChebyshevGrid(npoints, domain)
        f = grid.x ** 2

        # Act
        f_inter = grid.interpolant(f)

        # Assert
        self.assertAlmostEqual(
            0.5 ** 2,
            f_inter(0.5)
        )

    def test_diff(self):
        domain = (0, 1)
        npoints = 21
        grid = ChebyshevGrid(npoints, domain)
        f = grid.x ** 2

        d_dx = grid.diff()
        df_dx = d_dx(f)
        assert_array_almost_equal(
            2 * grid.x,
            df_dx
        )

    def test_diff_shifted(self):
        domain = (2, 3)
        npoints = 21
        grid = ChebyshevGrid(npoints, domain)
        f = grid.x ** 2

        d_dx = grid.diff()
        df_dx = d_dx(f)
        assert_array_almost_equal(
            2 * grid.x,
            df_dx
        )

    @unittest.skip
    def test_diff_sin(self):
        domain = (0, 10)
        grid = ChebyshevGrid(30, domain)
        x = grid.x
        f = np.sin(x)
        d_dx = grid.diff()
        df_dx = d_dx(f)
        plt.plot(x, np.cos(x))
        plt.plot(x, df_dx, 'o')
        plt.show()

    @unittest.skip
    def test_diff_scaling(self):
        domain = (0, 10)
        Ns = np.logspace(0.5, 2, 20, dtype=int)
        errs = []
        for N in Ns:
            grid = ChebyshevGrid(N, domain)
            d_dx = grid.diff()
            f = np.sin(grid.x)
            err = np.max(np.abs(np.cos(grid.x) - d_dx(f)))
            errs.append(err)
        plt.loglog(Ns, errs, 'o-')
        plt.show()

    def test_integration(self):
        domain = (0, np.pi)
        grid = ChebyshevGrid(20, domain)
        x = grid.x
        f = np.sin(x)**2
        integ = grid.integral()
        actual = integ(f)
        self.assertAlmostEqual(np.pi/2, actual)

    @unittest.skip
    def test_integration_scaling(self):
        domain = (0, np.pi)
        Ns = np.logspace(0.5, 2, 20, dtype=int)
        errs = []
        for N in Ns:
            grid = ChebyshevGrid(N, domain)
            x = grid.x
            f = np.sin(x) ** 2
            integ = grid.integral()
            actual = integ(f)

            err = np.max(np.abs(np.pi/2 - actual))
            errs.append(err)
        plt.loglog(Ns, errs, 'o-')
        plt.show()

    def test_integration_elliptic(self):
        grid = ChebyshevGrid(npoints=40, domain=(0, 2*np.pi))
        x = grid.x
        f_arr = np.sqrt(0.25 * np.sin(x)**2 + np.cos(x)**2)
        integ = grid.integral()
        actual = integ(f_arr)
        self.assertAlmostEqual(4.84422411027386, actual)

if __name__ == '__main__':
    unittest.main()
