class Solution:
    def isSymmetric(self, root):
        if not root: return True
        return self._judge(root.left, root.right)

    def _judge(self, L, R):
        if L is None and R is None: return True
        if L is None or R is None: return False
        return L.val == R.val and self._judge(L.left, R.right) and self._judge(R.left, L.right)


    def isSymmetric(self, root):
        if not root: return True
        queue = deque()
        queue.appendleft(root.left)
        queue.append(root.right)
        while queue:
            L = queue.popleft()
            R = queue.pop()
            # 提前结束
            if L is None and R is None: continue
            if L is None or R is None: return False
            if L.val != R.val: return False
            queue.appendleft(L.left)
            queue.appendleft(R.left)
            queue.append(R.right)
            queue.append(L.right)
        return True

