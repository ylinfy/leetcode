class Solution:
    # set判重, 直接把headA所有节点存储在集合中, 遍历headB如果有节点在集合中，直接返回
    # time: N, space: N
    def getIntersectionNode(self, headA, headB):
        tmp, tNodeA, tNodeB = set(), headA, headB
        while tNodeA:
            tmp.add(tNodeA)
            tNodeA = tNodeA.next
        while tNodeB:
            if tNodeB in tmp:
                return tNodeB
        return None


    # two ptr 1, time: N, space: 1
    # 将长度不一致的链表，长链表的起点是长度差值，即保证从起点开始，两链表长度一致
    def getIntersectionNode(self, headA, headB):
        tmpA = dummyA = headA
        tmpB = dummyB = headB
        # 遍历A,B
        while tmpA and tmpB:
            tmpA, tmpB = tmpA.next, tmpB.next
        # 找出长链表的起点dummy
        while tmpA:
            tmpA, dummyA = tmpA.next, dummyA.next
        while tmpB:
            tmpB, dummyB = tmpB.next, dummyB.next
        # 以dummyA和dummyB为起点，两链表长度一致, 长到相等的节点，返回即可
        while dummyA and dummyB:
            if dummyA == dummyB:
                return dummyA
            dummyA, dummyB = dummyA.next, dummyB.next
        return None


    # two ptr 2, time: M + N, space: 1
    # 遍历两链表，A遍历完后，跳到B起点，B遍历完后，跳到A起点，最终相遇会在第一个公共节点
    def getIntersectionNode(self, headA, headB):
        tmpA, tmpB = headA, headB
        # 若链表A和链表B长度一致，若无交点将同时到达末尾None, 即满足tmpA == tmpB, 退出循环返回None
        # 若两链表长度不一致，若无交点，则需要遍历完lenA + lenB，才能同时得到None, 满足tmpA == tmpB, 退出循环返回None
        # 若有交点，则会返回交点
        while tmpA != tmpB:
            tmpA = tmpA.next if tmpA else headB
            tmpB = tmpB.next if tmpB else headA
        return tmpA



            
