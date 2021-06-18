class Solution:
    # 递归，time: N
    def reversePrint(self, head):
        return self.reversePrint(head.next) + [head.val] if head else []

    # 递归
    res = []
    def reversePrint(self, head):
        if not head: return []
        self.reversePrint（head.next)
        self.res.append(head.val)
        return self.res

    def reversePrint(self, head):
        stack = []
        while head: 
            stack.append(head.val)
            head = head.next
        return stack[::-1]
