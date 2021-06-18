class Solution:
    # 将二叉搜索树转换为排序双向循环
    # time: N, 遍历完所有节点
    # 使用中序遍历，保证有序，在遍历过程中修改各节点指向
    def treeToDoublyList(self, root):
        if not root: return None
        # 头节点和前一节点初始化
        self.head, self.pre = None, None
        # 中序遍历，遍历过程中修改各节点指向
        self.inorder(root)
        # 最后把头节点和尾节点连接起来，完成双向循环链表
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

    def inorder(self, cur):
        if not cur: return
        # 递归到最左值
        self.inorder(cur.left)
        # 如果存在前一节点pre, 则修改当前节点与前一节点的指向
        if self.pre:
            self.pre.right, cur.left = cur, self.pre
        else:
            self.head = cur  # 不存在前一节点，即cur是最左值时，直接把cur赋给head
        self.pre = cur
        self.inorder(cur.right)


