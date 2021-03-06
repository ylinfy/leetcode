class Solution:
    # 递归，类似于DFS，先往深处递归，一直递归到尾，数据先压栈再弹栈
    def __init__(self):
        self.res = []

    def reversePrint(self, head):
        if not head: return []
        self.reversePrint(head.next)
        self.res.append(head.val)
        return self.res
