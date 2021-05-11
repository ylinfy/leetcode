class Solution:
    def treeToDoublyList(self, root):
        if not root: return None
        self.head = self.pre = None
        self.inorder(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

    def inorder(self, cur):
        if not cur: return
        self.inorder(cur.left)
        if not self.pre:
            self.head = cur
        else:
            self.pre.right, cur.left = cur, self.pre
        self.pre = cur
        self.inorder(cur.right)
            
