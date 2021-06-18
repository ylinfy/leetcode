class Solution:
    # 递归，time: N
    def deleteNode(self, head, val):
        # terminator
        if not head: return head

        # head.next = head.next.next if head.val == val else head.next
        # 当head.val == val时，直接返回head.next.next
        head.next = self.deleteNode(head.next, val)
        return head.next if head.val == val else head


    # 双指针，time: N
    def deleteNode(self, head, val):
        if not head: return head  # 如果是None, 直接返回
        # 如果要删除的节点是头节点，直接删除, 特殊情况，双指针
        if head.val == val: return head.next  
        # 遍历链表
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = pre.next, cur.next
        if cur: pre.next = cur.next
        return head


    # 单指针，tiem: N
    def deleteNode(self, head, val):
        if not head: return head  # 如果是None, 直接返回
        # 如果要删除的节点是头节点，直接删除, 特殊情况，双指针
        if head.val == val: return head.next  

        # 遍历链表, 仿照双指针, 此处cur是双指针中的pre
        cur = head
        while cur.next and cur.next.val != val:
            cur = cur.next
        if cur.next: cur.next = cur.next.next
        return head
