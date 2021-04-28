class Solution:
    def getKthFromEnd(self, head, k):
        pre = cur = head
        for i in range(k): cur = cur.next
        while cur: pre, cur = pre.next, cur.next
        return pre
        
        
