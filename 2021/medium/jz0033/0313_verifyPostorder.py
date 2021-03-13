class Solution:
    # 递归，分治，time: N**2 
    def verifyPostorder(self, postorder):
        if not postorder: return True
        return self.recur(postorder, 0, len(postorder) - 1)

    def recur(self, postorder, i, j):
        if i >= j: return True
        st = i
        while postorder[i] < postorder[j]: i += 1
        m = i
        while postorder[i] > postorder[j]: i += 1
        return i == j and self.recur(postorder, st, m - 1) and self.recur(postorder, m, j - 1)


    # 单调辅助栈，time: N
    def verifyPostorder(self, postorder):
        if not postorder: return True
        stack, root = [], float('inf')
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while (stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True



