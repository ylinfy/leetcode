class Solution:
    # 双指针，time: N, space: 1
    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            tNode = cur.next
            cur.next = pre
            pre = cur
            cur = tNode
        return pre


    # 递归，time: N, space: N
    def reverseList(self, head):
        return self._recur(None, head)

    def _recur(self, pre, cur):
        if not cur: return pre
        res = self._recur(cur, cur.next)
        cur.next = pre
        return res


    # 递归2，time: N, space: N
    def reverseList(self, head):
        if not head or not head.next: return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res

            
