class ForwardSolver:
    def __init__(self, f, n):
        if not callable(f):
            raise ValueError("f should be callable")
        self._f = f
        self._n = n
        self._p = dict()
        self._p[0] = {i: self._f(i) for i in range(1, self._n)}

    def count(self):
        for k in range(1, self._n):
            j = 2 ** k
            while j <= self._n - 2 ** k:
                phi = self._p[k - 1][j - 2 ** (k - 1)] + self._p[k - 1][j + 2 ** (k - 1)]
                self._p[k][j] = self._p[k - 1][j]
                for l in range(1, 2 ** (k - 1)):
                    self._p[k][j] += self._count_v(self._count_matrix_c(), self._count_a(), phi)
                self._p[k][j] *= 0.5
                j *= 2

    def get_p(self):
        return self._p

    def _count_v(self, C, a, phi):
        pass

    def _count_matrix_c(self):
        pass

    def _count_a(self):
        pass


if __name__ == '__main__':
    ForwardSolver(lambda x: x, 10)
