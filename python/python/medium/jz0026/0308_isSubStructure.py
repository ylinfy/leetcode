class Solution:
    # time: MN --> (先序遍历树A占用O(M)，每次调用recur(A, B)判断占用O(N))
    # 以A中任意一个节点为根节点，去一一比较和B的所有节点值
    # 若B遍历完，则返回True, 否则A遍历完或者出现A.val != B.val，即返回False 
    def isSubStructure(self, A, B):
        if not A or not B: return False

        # 以A根节点为根节点，与B各节点一一比较
        root_compare = self.compareAllNode(A, B)
        if root_compare: return True

        # 上述未匹配到，则将左，右子节点当作根节点，继续比较
        left_compare = self.isSubStructure(A.left, B) 
        if left_compare: return True
        right_compare = self.isSubStructure(A.right, B)
        if right_compare: return True
        return False

    def compareAllNode(self, A, B):
        if not B: return True
        if not A or A.val != B.val: return False
        return self.compareAllNode(A.left, B.left) and self.compareAllNode(A.right, B.right)
        
        
