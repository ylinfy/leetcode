class Solution:
    # 递归，time: N
    def deleteNode(self, head, val):
        if not head: return head
        head.next = self.deleteNode(head.next, val)
        return head.next if head.val == val else head
        

    # 双指针，time: N
    def deleteNode(self, head, val):
        if not head: return head
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head


    # 单指针，time: N
    def deleteNode(self, head, val):
        if not head: return head
        if head.val == val: return head.next
        cur = head
        while cur.next and cur.next.val != val:
            cur = cur.next
        if cur.next: cur.next = cur.next.next
        return head

