class Solution:
    def isSubStructure(self, A, B):
        if not A or not B: return False
        return self.compare(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def compare(self, A, B):
        if not B: return True
        if not A: return False
        if A.val != B.val: return False
        return self.compare(A.left, B.left) and self.compare(A.right, B.right)

