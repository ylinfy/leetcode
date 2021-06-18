class Solution:
    # 1~14代表A~K，大小王为0, 0是赖子，抽五张牌，是否为顺子
    # 最大值减最小值小于5即可（重复非零值除外)
    # time: N
    def isStraight(self, nums):
        # 判重集合
        repeat = set()
        ma, mi = 0, 14
        for n in nums:
            # 存在重复的零是OK的, 跳过0
            if n == 0: continue
            # 存在重复非零数字，直接返回False
            if n in repeat: return False 
            temp.add(n)
            ma = max(ma, n)
            mi = min(mi, n)
        return ma - mi < 5

    
    # 先排序，再用nums[-1] - 第一个不为0的值<5进行判断
    # time: N*logN
    def isStraight(self, nums):
        # 记录大小王数，以找到第一个不为0的数
        joker = 0
        nums.sort()  
        for i in range(4):  # 此处只取到倒数第二个数，防止取i+1越界
            if nums[i] == 0: joker += 1
            # 如果存在重复非零值，直接返回False
            elif nums[i] == nums[i+1]: return False
        return nums[-1] - nums[joker] < 5
