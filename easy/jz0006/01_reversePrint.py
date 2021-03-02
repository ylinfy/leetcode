class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 递归法，DFS
    def __init__(self):
        self.res = []

    def reversePrint(self, head):
        if not head: return []
        self.reversePrint(head.next)
        self.res.append(head.val)
        return self.res

    # 辅助栈
    def reversePrint(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
