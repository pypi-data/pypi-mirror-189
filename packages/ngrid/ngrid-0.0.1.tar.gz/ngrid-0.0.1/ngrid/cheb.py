import numpy as np
from numpy.fft import fft, ifft
from numpy.linalg import inv

from ngrid.base import Grid


class ChebyshevGrid(Grid):
    """Represents a 1D Chebychev grid."""

    def __init__(self, npoints, domain):
        """Constructor

        Parameters
        ----------
        npoints: int
            The number of grid points (x_0,...,x_{N-1}).
        domain: tuple of floats
            The interval on the real line described by the grid.
        """
        super(ChebyshevGrid, self).__init__(npoints, domain)
        x_left, x_right = self.domain
        center = (x_right + x_left) / 2.
        radius = (x_right - x_left) / 2.

        self.x = center + radius * (
            np.cos(np.pi - np.arange(self.npoints)*np.pi / (self.npoints-1))
        )

        self._diff = None # lazy evaluation
        self._integral = None

    def diff(self):
        if self._diff is None:
            self._diff = ChebyshevDiffOperator(self.domain, self.npoints)
        return self._diff

    def integral(self):
        return SpectralIntegral(self.diff().as_matrix())


class ChebyshevDiffOperator:

    def __init__(self, domain, npoints):
        self._domain = domain
        self._npoints = npoints
        self._matrix = None # lazy evaluation

    def __call__(self, f, **kwargs):
        N = len(f) - 1

        F_long, k, x = chebfft(N, f)
        W = ifft(1j * k * F_long)

        w = np.zeros_like(f)
        w[1:-1] = - W.real[1:N] / np.sqrt(1 - x[1:-1] ** 2)

        n = np.arange(N + 1)
        w[0] = np.sum(
            n** 2 * F_long[:N + 1]
        ) / N

        w[-1] = np.sum(
            (-1) ** (n + 1) * n ** 2 * F_long[:N + 1]
        ) / N

        return 2 * w[::-1] / (self._domain[-1] - self._domain[0])

    def as_matrix(self):
        if self._matrix is not None:
            return self._matrix
        N = self._npoints - 1
        x = np.cos(np.pi * np.arange(N + 1) / N)
        x = x.reshape(1, N + 1)
        X = x - x.T

        c = np.ones_like(x)
        c[0, 0] = c[0, -1] = 2
        C = c / c.T

        j = np.arange(N + 1).reshape(1, N + 1)
        S = (-1) ** j * (-1) ** j.T

        mask_diag = np.eye(N + 1, dtype=bool)
        mask_off = ~mask_diag

        D = np.zeros((N + 1, N + 1))
        D[mask_off] = C[mask_off] * S[mask_off] / X[mask_off]

        x = x.reshape(-1)  # turns x back into shape (N,)

        diag = np.zeros(N + 1)
        diag[1:-1] = - x[1:-1] / (2 * (1 - x[1:-1] ** 2))

        D[mask_diag] = diag
        D[0, 0] = (2 * N ** 2 + 1) / 6
        D[N, N] = - D[0, 0]
        self._matrix = D.T * (2 / (self._domain[1] - self._domain[0]))
        return self._matrix


class SpectralIntegral:

    def __init__(self, D):
        self._D = D[1:, 1:]
        self._Dinv = None # lazy evaluation

    def __call__(self, f, **kwargs):
        if not self._Dinv:
            self._Dinv = inv(self._D)
        # -f because the sense of integration is reversed for D
        return np.dot(self._Dinv[-1, :], -f[1:])


def chebfft(N, f):
    f = f[::-1]
    x = np.cos(np.arange(N + 1) * np.pi / N)
    f_long = np.append(f, f[::-1][1:-1])
    F_long = np.real(fft(f_long))
    k = [i for i in range(N)] + [0] + [i for i in range(1 - N, 0)]
    k = np.asarray(k)
    return F_long, k, x
