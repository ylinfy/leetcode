class Solution:
    # 辅助栈，直接将链A所有节点存储在栈中，遍历链B，如果有节点存在于栈中，返回该节点即可
    # time: M + N
    def getIntersectionNode(self, headA, headB):
        aux, tmpA, tmpB = set(), headA, headB 
        while tmpA:
            aux.add(tmpA)
            tmpA = tmpA.next 
        while tmpB:
            if tmpB in aux: return tmpB
            tmpB = tmpB.next
        return None


    # 从不同起点开始，保证起点到链尾长度一致
    # time: N
    def getIntersectionNode(self,headA, headB):
        tmpA = dummyA = headA
        tmpB = dummyB = headB

        # 两链表长度差为N, 则循环遍历后，短链表已经到None, 长链表剩余长度为N
        while tmpA and tmpB: tmpA, tmpB = tmpA.next, tmpB.next

        # 再次遍历两链表，短链表不会再遍历，长链表则会指到第N个Node节点(dummy是从head开始遍历)
        while tmpA: dummyA, tmpA = dummyA.next, tmpA.next
        while tmpB: dummyB, tmpB = dummyB.next, tmpB.next

        # 此时dummyA和dummyB链表长度一致，遍历，找到第一个公共节点并返回
        while dummyA and dummyB:
            if dummyA == dummyB: return dummyA
            dummyA, dummyB = dummyA.next, dummyB.next
        return None  # 没找到，则表示没有公共节点，直接返回None


    # 两链表长度和是确定的，从不同链表的头节点开始遍历，最终相遇在公共节点
    def getIntersectionNode(self, headA, headB):
        tmpA, tmpB = headA, headB
        while tmpA != tmpB:
            # A和B长度不一致，即A和B不会同一时间到None, 只有到了公共节点，才会有tmpA == tmpB
            tmpA = tmpA.next if tmpA else headB
            tmpB = tmpB.next if tmpB else headA
        return tmpA
        
