class Solution:
    # 递归，逐一比较，不满足即可返回, time: M*N (M:A的节点数，N:B的节点数)
    def isSubStructure(self, A, B):
        if not A or not B: return False
        # 拿A的每一个节点去与B进行比较，只要比较成功，即B是子树，直接返回True 
        return self.compare(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def compare(self, A, B):
        # 每次比较，如果B空了，说明比较完了，全部通过，B是A的子树
        if not B: return True
        # 如果A空了，B还没空，或者某一个节点，A的值与B的值不等，即以此节点为根节点的子树，与B不相同
        # 返回False, 继续下一节点的compare
        if not A or A.val != B.val: return False
        # 逐点比较
        return self.compare(A.left, B.left) and self.compare(A.right, B.right)
        
