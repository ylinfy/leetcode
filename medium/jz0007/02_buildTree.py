class Solution:
    # time: N
    def buildTree(self, preorder, inorder):
        if not preorder: return None
        node = TreeNode(preorder[0])
        idx = inorder.index(node.val)
        node.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        node.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return node

    # time: N (速度相对更快)
    def buildTree(self, preorder, inorder):
        def recursion(root, left, right):
            if left > right: return
            node = TreeNode(preorder[root])
            i = dic[node.val]
            node.left = recursion(root + 1, left, i - 1)
            node.right = recursion(root + (i - left + 1), i + 1, right)
            return node
        # 先用字典将对应关系存储起来
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recursion(0, 0, len(inorder) - 1)
