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
        if self.pre:
            self.pre.right, cur.left = cur, self.pre
        else:
            self.head = cur
        self.pre = cur
        self.inorder(cur.right)

            
