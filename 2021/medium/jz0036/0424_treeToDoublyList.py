class Solution:
    # 将二叉搜索树转换成有序循环双向链表
    # 因为有序，考虑使用中序遍历变体，在遍历中修改各指向来实现循环双向链表结构
    def treeToDoublyList(self, root):
        if not root: return None
        self.head = self.pre = None
        self.inorder(root)  # 遍历完后，pre等于最后一个节点，也就是最右右节点
        # 将首节点head和末节点pre对应互指，即完成了双向链表的循环属性
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

    def inorder(self, node):
        if not node: return
        self.inorder(node.left)  # 中序遍历，先递归到最左左节点
        if self.pre is None:  # 如果是最左左节点，即pre还未被赋值
            self.head = node  # 将最左左节点赋值给有序双向循环链表头节点
        else:  # 实现前一节点和当前节点的互指
            self.pre.right, node.left = node, self.pre
        self.pre = node  # 遍历后，将当前节点赋给pre, 继续中序遍历下一节点
        self.inorder(node.right)
            

