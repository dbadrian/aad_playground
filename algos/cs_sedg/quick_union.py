
class QuickUnionUF():
    """ Find: O(n) (worst-case)
        Union: O(N)
     """
    def __init__(self, N):
        self.data = list(range(N))

    def connected(self, p, q):
        return self.__root(p) == self.__root(q)

    def union(self, p, q):
        rp = self.__root(p)
        rq = self.__root(q)
        self.data[rp] = rq

    def __root(self, p):
        while p != self.data[p]:
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
    assert qu.data[4] == 3
    qu.union(3,8)
    assert qu.connected(4,3)
    assert qu.connected(4,8)
    assert qu.connected(3,8)
    assert qu.data[3] == 8
    assert qu.data[4] == 3
    assert qu.data[8] == 8

    print("All checks passed!")

if __name__ == "__main__":
    test_QuickFindUF()