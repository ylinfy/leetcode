class Solution:
    def reverseList(self, head):
        if not head or not head.next: return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res

    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            tNode = cur.next
            cur.next, pre, cur = pre, cur, tNode
        return pre   

    def reverseList(self, head):
        def recur(pre, cur):
            if not cur: return pre
            res = recur(cur, cur.next)
            cur.next = pre
            return res
        return recur(None, head)

