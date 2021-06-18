class Solution:
    # 双指针，time: N
    # 局部两两反转(以None,head开始)
    # 先将第三个(head.next)记录在tNode, 
    def reverseList(self, head):
        per, cur = None, head
        while cur:
            tNode = cur.next
            cur.next = pre
            pre = cur
            cur = tNode
        return pre


    # 递归，time: N
    # 以None, head开始，依次两两压栈(stride=1)，最后再弹栈时，将cur.next指向pre
    def reverseList(self, head):
        pre, cur = None, head
        return self._recur(pre, cur)

    def _recur(self, pre, cur):
        if not cur: return pre
        res = self._recur(cur, cur.next)
        cur.next = pre
        return res


    # 递归，time: N
    # 依次将链表压栈，最后再弹栈时，将cur.next.next指向cur，相当于反转
    def reverseList(self, head):
        if not head or not head.next: return head
        tNode = self.reverseList(head.next)
        head.next.next = head
        # 思考, 为什么此处要将head.next指向None
        # 不指向None, 最后两个节点会互指
        head.next = None
        return tNode


            
