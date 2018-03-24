
class QuickUnionUF():
    def __init__(self, N):
        self.data = list(range(N))
        self.sz = [1] * N

    def connected(self, p, q):
        return self.__root(p) == self.__root(q)

    def union(self, p, q):
        rp = self.__root(p)
        rq = self.__root(q)

        # already same root/connected, no need to update
        if rp == rq: return

        if self.sz[rp] < self.sz[rq]:
            self.data[rp] = rq
            self.sz[rq] += self.sz[rp]
        else:
            self.data[rq] = rp
            self.sz[rp] += self.sz[rq]

    def __root(self, p):
        while p != self.data[p]:
            self.data[p] =  self.data[self.data[p]]
            p = self.data[p]

        return p

def test_QuickFindUF():
    qu = QuickUnionUF(10)

    assert not qu.connected(1,2)
    assert not qu.connected(1,4)
    assert qu.connected(1,1)
    assert not qu.connected(4,3)

    qu.union(4,3)
    assert qu.connected(4,3)
    assert qu.data[4] == 4
    assert qu.data[3] == 4

    qu.union(4,8)
    assert qu.connected(4,3)
    assert qu.connected(4,8)
    assert qu.connected(3,8)

    assert qu.data[3] == 4
    assert qu.data[4] == 4
    assert qu.data[8] == 4

    qu.union(6,5)
    qu.union(9,4)
    assert qu.data[9] == 4

    qu.union(2,1)
    assert qu.data[1] == 2

    qu.union(5,0)
    assert qu.data[0] == 6

    print("All checks passed!")

if __name__ == "__main__":
    test_QuickFindUF()