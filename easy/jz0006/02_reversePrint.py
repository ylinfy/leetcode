class Solution:
    def __init__(self):
        self.res = []

    def reversePrint(self, head):
        if not head: return []
        self.reversePrint(head.next)
        self.res.append(head.val)
        return self.res
