
class QuickFindUF():
    """ Find: O(1)
        Union: O(N), but for n-Union operations this means O(N^2)
     """
    def __init__(self, N):
        self.data = list(range(N))

    def connected(self, p, q):
        return self.data[p] == self.data[q]

    def union(self, p, q):
        pid = self.data[p]
        qid = self.data[q]

        for idx, cid in enumerate(self.data):
            if cid == pid:
                self.data[idx] = qid

def test_QuickFindUF():
    qf = QuickFindUF(10)

    assert not qf.connected(1,2)
    assert not qf.connected(1,4)
    assert qf.connected(1,1)
    assert not qf.connected(4,3)
    qf.union(4,3)
    assert qf.connected(4,3)
    assert qf.data[4] == 3
    qf.union(3,8)
    assert qf.connected(4,3)
    assert qf.connected(4,8)
    assert qf.connected(3,8)
    assert qf.data[3] == 8
    assert qf.data[4] == 8
    assert qf.data[8] == 8

    print("All checks passed!")

if __name__ == "__main__":
    test_QuickFindUF()