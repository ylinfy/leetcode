class Solution:
    def isSymmetric(self, root):
        if not root: return True
        return self.compare(root.left, root.right)

    def compare(self, L, R):
        if L is None and R is None: return True
        if L is None or R is None: return False
        if L.val != R.val: return False
        return self.compare(L.left, R.right) and self.compare(R.left, L.right)
        
    
    def isSymmetric(self, root):
        if not root: return True
        queue = [root.right, root.left]
        while queue:
            L = queue.pop()
            R = queue.pop()
            if L is None and R is None: continue
            if L is None or R is None: return False
            if L.val != R.val: return False
            queue.append(L.right)
            queue.append(R.left)
            queue.append(R.right)
            queue.append(L.left)
        return True
