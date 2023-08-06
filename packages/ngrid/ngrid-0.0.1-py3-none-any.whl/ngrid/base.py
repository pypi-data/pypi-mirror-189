import abc

from ngrid.exceptions import GridError
from ngrid.interpol import LagrangeInterpolator


class Grid(abc.ABC):
    interpolator_class = LagrangeInterpolator

    def __init__(self, npoints, domain):
        x_left, x_right = domain
        if x_right <= x_left:
            raise GridError("Invalid domain: %s" % str(domain))

        self.npoints = npoints
        self.domain = domain

        # To be overwritten by child classes:
        self.x = None
        self._interpolator = None
        self._diff = None

    def interpolant(self, f):
        if not self._interpolator:
            self._interpolator = LagrangeInterpolator(self.x)
        return self._interpolator.create_interpolant(f)
