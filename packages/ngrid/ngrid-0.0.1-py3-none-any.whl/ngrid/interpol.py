import numpy as np

from ngrid.exceptions import GridError


class LagrangeInterpolator:

    def __init__(self, grid_points):
        npoints = len(grid_points)
        x = grid_points

        # TODO: optimize for loops with numpy
        a = np.ones(npoints)
        for i in range(npoints):
            for j in range(npoints):
                if i != j:
                    a[i] *= 1 / (x[i] - x[j])
        self._a = a
        self._x = x

    def create_interpolant(self, f):
        N = len(self._a)
        if N != len(f):
            raise GridError("Incompatible grid size: %d vs %s." % (N, len(f)))
        a = self._a
        x = self._x
        def p(x_):
            result = 0.
            for i in range(N):
                term_i = a[i] * f[i]
                for j in range(N):
                    if i != j:
                        term_i *= x_ - x[j]
                result += term_i
            return result

        return p