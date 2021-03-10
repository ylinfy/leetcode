class Solution:
    def isSubStructure(self, A, B):
        if not A or not B: return False
        return self._compare(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def _compare(self, A, B):
        if not B: return True
        if not A or A.val != B.val: return False
        return self._compare(A.left, B.left) and self._compare(A.right, B.right)
