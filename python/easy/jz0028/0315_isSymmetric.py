class Solution:
    # 递归，逐一比较, time: N
    def isSymmetric(self, root):
        if not root: return True
        return self._judge(root.left, root.right)

    def _judge(L, R):
        if L is None and R is None: return True
        if L is None or R is None: return False
        if L.val != R.val: return False
        return self._judge(L.left, R.right) and self._judge(L.right, R.left)


    # 辅助栈或双端队列，逐一比较，time: N
    def isSymmetric(self, root):
        if not root: return True
        queue = [root.right, root.left]
        while queue:
            L = queue.pop()
            R = queue.pop()
            if L is None and R is None: continue
            if L is None or R is None: return False
            if L.val != R.val: return False
            queue.append(R.right)
            queue.append(L.left)
            queue.append(L.right)
            queue.append(R.left)
        return True



