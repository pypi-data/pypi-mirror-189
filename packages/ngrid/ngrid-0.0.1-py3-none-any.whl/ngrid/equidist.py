import numpy as np
from findiff import FinDiff
from ngrid.base import Grid
from ngrid.exceptions import GridError
from ngrid.utils import reduce_periodic
from numpy.fft import fft, ifft, fftfreq
from scipy.integrate import simpson


class EquidistantGrid(Grid):

    def __init__(self, npoints, domain, periodic=False):
        super(EquidistantGrid, self).__init__(npoints, domain)
        self.x = np.linspace(*domain, npoints, endpoint=(not periodic))
        self.periodic = periodic
        self.dx = self.x[1] - self.x[0]

    def interpolant(self, f):
        f_inter = super(EquidistantGrid, self).interpolant(f)
        if self.periodic:
            return lambda x: f_inter(
                reduce_periodic(*self.domain, x)
            )
        return f_inter

    def diff(self, method=None):
        """Returns a callable representing a derivative operator.

        Parameters
        ----------
        method : str
            The method to use for differentiation. Allowed values:

                'findiff'   for finite difference scheme
                'fft'       for spectral differentiation

            Default is dependent on whether the grid is periodic or not.
            For periodic grids, 'fft' method is applied by default, otherwise
            'findiff'.

        Returns
        -------
        out:
            Derivative operator as callable
        """

        if method is None:
            if self.periodic:
                method = 'fft'
            else:
                method = 'findiff'

        if method == 'findiff':
            return FinDiff(0, self.dx)
        elif method == 'fft':
            mask = False if self.periodic else True
            return SpectralDiffOperator(self.dx, mask)
        else:
            raise GridError('No such method: %s' % method)

    def integral(self):
        if self.periodic:
            return SpectralIntegral()
        else:
            return lambda f: simpson(f, dx=self.dx)


class SpectralDiffOperator:

    def __init__(self, dx, use_mask=False):
        self.dx = dx
        self.use_mask = use_mask

    def __call__(self, f, **kwargs):
        N = len(f)
        if self.use_mask:
            mask = np.ones_like(f)
            mask_length = 4
            mask[:mask_length] = np.sin(np.pi / 2. / mask_length*np.arange(mask_length))**6
            mask[-mask_length:] = mask[:mask_length][::-1]
            f = mask * f
        k = fftfreq(N, self.dx)
        F = fft(f)
        W = 1j * k * F
        fx = ifft(W) * 2 * np.pi
        if np.any(np.iscomplex(f)):
            return fx
        return fx.real


class SpectralIntegral:

    def __call__(self, f, **kwargs):
        N = len(f)
        return np.mean(f) * 2 * np.pi