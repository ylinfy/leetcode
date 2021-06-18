class Solution:
    # 递归，逐点比较，time: MN, M,N分别是A,B的节点个数
    def isSubStructure(self, A, B):
        if not A or not B: return False
        return self._recursion(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def _recursion(self, A, B):
        if not B: return True
        if not A or A.val != B.val: return False
        return self._recursion(A.left, B.left) and self._recursion(A.right, B.right)
