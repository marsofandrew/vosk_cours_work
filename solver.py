import numpy as np
import math


class ForwardSolver:
    def __init__(self, C, f):
        self._C = np.array(C)
        self._f = f
        self._n = len(self._f)
        self._p = dict()
        self._p[0] = {i: np.array(self._f[i]) for i in range(1, self._n)}

    def count(self):
        for k in range(1, self._n):
            j = 2 ** k
            self._p[k] = dict()
            while j <= self._n - 2 ** k:
                phi = self._p[k - 1][j - 2 ** (k - 1)] + self._p[k - 1][j + 2 ** (k - 1)]
                self._p[k][j] = 0
                for l in range(1, 2 ** (k - 1)):
                    self._p[k][j] += self._count_v(self._count_matrix_c(l, k - 1), self._count_a(l, k - 1), phi)
                self._p[k][j] *=0.5
                j *= 2
        return self._p

    def get_p(self):
        return self._p

    def _count_v(self, C, a, phi):
        return np.multiply(np.asmatrix(C).I, np.multiply(a, phi))

    def _count_matrix_c(self, l, k):
        return self._C - np.multiply(2 * math.cos((2 * l - 1) * math.pi / (2 ** (k + 1))), np.eye(self._C.shape[0]))

    @staticmethod
    def _count_a(l, k):
        return (((-1) ** (l + 1)) / 2 ** k) * math.sin((2 * l - 1) * math.pi / 2 ** (k + 1))


if __name__ == '__main__':
    pass
