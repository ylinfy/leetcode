class Solution:
    # recursion, time: N
    def __init__(self):
        self.res = []

    def reversePrint(self, head):
        if not head: return []
        self.reversePrint(head.next)
        self.res.append(head.val)
        return self.res

    # stack, time: N
    def reversePrint(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
