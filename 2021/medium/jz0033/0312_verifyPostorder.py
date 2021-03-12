class Solution:
    # 分治递归，time: N**2 (当退化成链表时，时间度为最大N**2)
    def verifyPostorder(self, postorder):
        return self._recur(postorder, 0, len(postorder) - 1)

    def _recur(self, postorder, i, j):
        if i >= j: return True
        t = i
        # 找到第一个大于根节点的数，即为右子树第一个值
        while postorder[t] < postorder[j]: t += 1
        # 判断所有右子树均大于根节点
        m = t
        while postorder[t] > postorder[j]: t += 1
        # 判断右子树是否均大于根节点，以及左右子树是否也为二叉搜索树
        return t == j and self._recur(postorder, i, m - 1) and self._recur(postorder, m, j - 1)

    
    # 倒序 & 辅助单调栈，time: N (遍历所有节点，各节点均入栈出栈一次)
    def verifyPostorder(self, postorder):
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True

        




        
            
            


