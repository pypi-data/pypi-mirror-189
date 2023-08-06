import unittest

import numpy as np
from matplotlib import pyplot as plt
from numpy.testing import assert_array_almost_equal, assert_allclose

from ngrid import ChebyshevGrid, EquidistantGrid


class TestEquidistantCartesian(unittest.TestCase):

    def test_create_grid_1d_in_standard_interval(self):
        # Arrange
        domain = (-1, 1)
        npoints = 21
        x = np.linspace(-1, 1, 21)

        # Act
        grid = EquidistantGrid(npoints, domain)

        # Assert
        assert_array_almost_equal(x, grid.x)

    def test_create_grid_1d_in_nonstandard_interval(self):
        # Arrange
        domain = (-2, 3)
        npoints = 5
        x = np.linspace(-2, 3, npoints)

        # Act
        grid = EquidistantGrid(npoints, domain)

        # Assert
        assert_array_almost_equal(x, grid.x)

    def test_interpolate_grid(self):
        # Arrange
        domain = (-1, 1)
        npoints = 21
        grid = EquidistantGrid(npoints, domain)
        f = grid.x ** 2

        # Act
        f_inter = grid.interpolant(f)

        # Assert
        self.assertAlmostEqual(
            0.5 ** 2,
            f_inter(0.5)
        )

    def test_interpolate_grid_periodic(self):
        # Arrange
        domain = (-1, 1)
        npoints = 21
        grid = EquidistantGrid(npoints, domain, periodic=True)
        f = grid.x ** 2

        # Act
        f_inter = grid.interpolant(f)

        # Assert
        self.assertAlmostEqual(
            0.5 ** 2,
            f_inter(0.5)
        )

        # Assert
        self.assertAlmostEqual(
            0.5 ** 2,
            f_inter(2.5)
        )

    def test_diff_nonperiodic(self):
        domain = (0, 1)
        npoints = 21
        grid = EquidistantGrid(npoints, domain)
        f = grid.x ** 2

        d_dx = grid.diff()
        df_dx = d_dx(f)

        assert_array_almost_equal(
            2*grid.x,
            df_dx
        )

    def test_diff_periodic(self):
        domain = (0, 2*np.pi)
        npoints = 31
        grid = EquidistantGrid(npoints, domain, periodic=True)
        x = grid.x
        f = np.exp(np.sin(x))

        d_dx = grid.diff()
        df_dx = d_dx(f)

        assert_array_almost_equal(
            np.cos(x)*f,
            df_dx
        )

    def test_diff_nonperiodic_spectral(self):
        domain = (-7, 7)
        npoints = 31
        grid = EquidistantGrid(npoints, domain)
        x = grid.x
        f = np.exp(-x**2)

        d_dx = grid.diff(method='fft')
        df_dx = d_dx(f)

        assert_allclose(
            -2*x*f,
            df_dx, atol=2.E-5
        )

    def test_integrate_nonperiodic(self):
        domain = (0, 3)
        npoints = 50
        grid = EquidistantGrid(npoints, domain)
        f = np.cos(grid.x)

        integ = grid.integral()

        actual = integ(f)
        self.assertAlmostEqual(np.sin(3), actual, places=5)

    def test_integrate_periodic(self):
        grid = EquidistantGrid(npoints=30, domain=(0, 2*np.pi), periodic=True)
        x = grid.x
        f_arr = np.sqrt(0.25 * np.sin(x)**2 + np.cos(x)**2)
        integ = grid.integral()
        actual = integ(f_arr)
        self.assertAlmostEqual(4.84422411027386, actual)

    @unittest.skip
    def test_integrate_periodic_scaling(self):
        Ns = np.logspace(1, 2.5, 100, dtype=int)
        errs = []
        for N in Ns:
            _, err = integration_run(
                lambda x: np.exp(np.sin(x)),
                lambda x: np.cos(x) * np.exp(np.sin(x)),
                (0, 2*np.pi),
                npoints=N,
                periodic=True)
            errs.append(err)
        plt.loglog(Ns, errs)
        plt.show()


def integration_run(indefinite, f, domain, npoints, periodic):
    grid = EquidistantGrid(npoints, domain, periodic=periodic)
    f_arr = f(grid.x)
    integ = grid.integral()
    actual = integ(f_arr)
    err = np.abs(actual - (indefinite(domain[1]) - indefinite(domain[0])))
    return actual, err


if __name__ == '__main__':
    unittest.main()
