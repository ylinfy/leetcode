class Solution:
    # 双指针，间隔k，cur到末尾，返回pre
    # time: N, space: 1
    def getKthFromEnd(self, head, k):
        pre = cur = head
        # cur指向第k个node, 即pre,cur间隔k
        for _ in range(k): cur = cur.next
        # 当cur指向末尾时，pre即倒数第k个节
        while cur: pre, cur = pre.next, cur.next
        return pre

    # 辅助栈，将链表全部压入栈中，返回倒数第k个即可
    # time: N, space: N
    def getKthFromEnd(self, head, k):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        return stack[- k] if len(stack) >= k else None
