class Solution:
    # 递归，time: N
    def buildTree(self, preorder, inorder):
        if not preorder: return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root

    # 只需要将索引值传入递归函数即可，time: N
    def buildTree(self, preorder, inorder):
        def helper(rooti, lefti, righti):
            if lefti > righti: return None
            root = TreeNode(preorder[rooti])
            idx = dic[root.val]
            root.left = helper(rooti + 1, lefti, idx - 1)
            root.right = helper(rooti + 1 + idx - lefti, idx + 1, righti)
            return root
        dic = {}
        for i, n in enumerate(inorder): dic[n] = i
        return helper(0, 0, len(inorder) - 1)

