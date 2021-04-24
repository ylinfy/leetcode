class Solution:
    def deleteNode(self, head, val):
        if not head: return head
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = pre.next, cur.next
        if cur: pre.next = cur.next
        return head

    def deleteNode(self, head, val):
        if not head: return head
        head.next = self.deleteNode(head.next, val)
        return head.next if head.val == val else head
        
    
