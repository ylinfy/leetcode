class Solution:
    # 递归分治，time: N**2, (当树退化成链表时，最大时间复杂度N**2)
    def verifyPostorder(self, postorder):
        if not postorder: return True
        return self._verify(postorder, 0, len(postorder) - 1)

    def _verify(self, postorder, i, j):
        if i >= j: return True
        t = i
        while postorder[t] < postorder[j]: t += 1
        m = t
        while postorder[t] > postorder[j]: t += 1
        return t == j and self._verify(postorder, i, m - 1) and self._verify(postorder, m, j - 1)
    

    # 单调辅助栈，time: N(最坏情况每个节点均入栈出栈一次)
    def verifyPostorder(self, postorder):
        if not postorder: return True
        stack, root = [], float("inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True


        
