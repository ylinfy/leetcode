class Solution:
    def reverseList(self, head):
        if not head: return head
        pre, cur = None, head
        while cur:
            temp = cur
            cur = cur.next
            temp.next = pre
            pre = temp
        return pre


    def reverseList(self, head):
        if not head or not head.next: return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res


    def reverseList(self, head):
        if not head: return head
        return self.recur(None, head)
        
    def recur(self, pre_node, cur_node):
        if not cur_node: return pre_node
        res = self.recur(cur_node, cur_node.next)
        cur_node.next = pre_node
        return res
        



