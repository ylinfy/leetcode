class Solution:
    def __init__(self):
        self.dic = {}
    
    # 递归，操作索引, time: N
    def buildTree(self, preorder, inorder):
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0, 0, len(inorder) - 1, preorder)

    def recur(self, root, left, right, preorder):
        if left > right: return None
        node = TreeNode(preorder[root])
        idx = self.dic[node.val]
        node.left = self.recur(root + 1, left, idx - 1, preorder)
        node.right = self.recur(root + (idx - left + 1), idx + 1, right, preorder)
        return node

