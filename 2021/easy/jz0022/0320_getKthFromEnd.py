class Solution:
    # 辅助栈, time: N, space: N
    def getKthFromEnd(self, head, k):
        stack, count = [], 0
        while head:
            stack.append((0, head))
            head = head.next
            count += 1
        if len(stack) < k: return None
        return stack[len(stack) - k][1]

    # 双指针, time: N, space: 1
    def getKthFromEnd(self, head, k):
        pre = cur = head
        for _ in range(k):
            cur = cur.next
        while cur:
            pre, cur = pre.next, cur.next
        return pre
