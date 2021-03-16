class Solution:
    # 递归分治，镜像一一对应, time: N
    def isSymmetric(self, root):
        if not root: return True
        return self._judge(root.left, root.right)

    def _judge(self, L, R):
        if L is None and R is None: return True
        if L is None or R is None: return False
        return L.val == R.val and self._judge(L.left, R.right) and self._judge(R.left, L.right)
    

    # 栈或队列，time: N
    def isSymmetric(self, root):
        if not root: return True
        stack = [root.left, root.right]
        while stack:
            R = stack.pop()
            L = stack.pop()
            if L is None and R is None: continue
            if L is None or R is None: return False
            if L.val != R.val: return False
            stack.append(L.left)
            stack.append(R.right)
            stack.append(R.left)
            stack.append(L.right)
        return True

