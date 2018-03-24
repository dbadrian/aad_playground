import random
import sys

import numpy as np

from quick_union_3 import QuickUnionUF

class Percolation():
    def __init__(self, N):
        self.qu = QuickUnionUF(N*N+2)
        self.N = N

        self.vt_id = N*N
        self.vb_id = N*N+1

        self.min_idx = 0
        self.max_idx = N*N-1

        # Create Virtual Top
        [self.qu.union(self.vt_id, i) for i in range(0, N)]

        # Create Virtual Bottom
        [self.qu.union(self.vb_id,i) for i in range(N*(N-1), N*N)]

        # Set of open sites
        self.open_sites = set()

    def open(self, i, j):
        assert self.__validate_coords(i, j), "({},{}) is not a valid coordinate".format(i,j)

        idx = self.__coords_to_idx(i,j)

        # no check, just add anyway.
        if idx in self.open_sites:
            return
        else:
            self.open_sites.add(idx)

            for ai, aj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if self.__validate_coords(ai, aj):
                    a_idx = self.__coords_to_idx(ai, aj)
                    if self.__is_open(a_idx):
                        self.qu.union(idx, a_idx)

    def is_open(self, i, j):
        idx = self.__coords_to_idx(i,j)
        return self.__is_open(idx)

    def __is_open(self, idx):
        return idx in self.open_sites

    def is_full(self, i, j):
        idx = self.__coords_to_idx(i,j)
        return self.__is_full(idx)

    def __is_full(self, idx):
        return self.qu.connected(self.vt_id, idx)

    def number_of_open_sites(self):
        return len(self.open_sites)

    def number_of_open_sites_fraction(self):
            return self.number_of_open_sites() / (self.N * self.N)

    def percolates(self):
        return self.qu.connected(self.vt_id, self.vb_id)

    def __coords_to_idx(self, i, j):
        return (i-1)*self.N + (j-1)

    def __validate_coords(self, i, j):
        if i < 1 or i > self.N:
            return False
        if j < 1 or j > self.N:
            return False

        return True

class MCPercolationSimulation():
    def __init__(self, N, iterations):
        self.N = N
        self.iterations = iterations

    def sim(self):
        fractions = []

        for i in range(self.iterations):
            perc = Percolation(self.N)

            while not perc.percolates():
                i = random.randint(1, self.N)
                j = random.randint(1, self.N)
                perc.open(i, j)

            fractions.append(perc.number_of_open_sites_fraction())


        mean = np.mean(fractions)
        std = np.std(fractions)
        sc_std = 1.96/np.sqrt(self.iterations) * std
        cnf = np.asarray([-sc_std, sc_std]) + mean

        print("Mean:", mean)
        print("Std:", std)
        print("CNF-Interval:", cnf)



if __name__ == "__main__":
    assert len(sys.argv) == 3, "Not enough arguments (N, iters)"
    mcs = MCPercolationSimulation(int(sys.argv[1]), int(sys.argv[2]))
    mcs.sim()