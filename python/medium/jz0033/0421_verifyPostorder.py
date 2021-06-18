class Solution:
    # 给定一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果，是返回True，否返回False
    # 假定每个数字都互不相同
    
    # 递归，根据后序遍历的特性，找到根节点，即nums[-1], 判断剩余数据是否符合后续遍历特性
    # time: N**2 (当树退化成链表时，最大时间复杂度N**2)
    def verifyPostorder(self, postorder):
        return self.judge(postorder, 0, len(postorder) - 1)

    def judge(self, nums, i, j):
        # i, j分别为树的后序遍历首尾索引，根据后序遍历特性，可以找到左右子树的后续遍历首尾索引
        # 依次递归，且满足二叉搜索树定义
        if i >= j: return True
        t = i  # 记录左子树首索引，用于递归左子树, 用临时索引t去遍历 
        while nums[t] < nums[j]: t += 1  # 根据左子树小于根节点，找到分界点
        m = t  # 记录右子树首元素索引, 用于划分左右子树，从而drill down下去
        while nums[t] > nums[j]: t += 1
        # 满足条件t == j即右子树都大于根节点，才进入下一层，
        return t == j and self.judge(nums, i, m - 1) and self.judge(nums, m, j - 1)


    # 单调递归栈，将后序遍历数组反转，得到根、右、左的遍历顺序，即可维护一个递增栈
    # 当遇到一个小于栈中元素的数据时，找到第一个大于该数据的栈中元素，即为该元素的根节点
    # time: N (最坏的情况，每个节点都要入栈出栈)
    def verifyPostorder(self, postorder):
        if not postorder: return True
        # 新增一个虚拟的根节点, 假设postorder都是该root的左子树
        stack, root = [], float("inf")
        for i in range(len(postorder) - 1, -1, -1): 
            if postorder[i] > root: return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()  # 循环遍历单调栈，找到postorder[i]的根节点
            stack.append(postorder[i])
        return True  # 遍历完，都满足规则，即返回True

    
