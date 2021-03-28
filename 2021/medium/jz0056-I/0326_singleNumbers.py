class Solution:
    # 整型数组里除两个数字外，其他数字均出现两次，找出此两只出现一次的数字
    # time: N, space: 1
    # 此类题目使用位运算异或处理，一个数异或同一个数两次，结果不变
    # 将所有数异或，结果即是两个出现一次异或的结果，选取一个值为1的bit, 区分两个区间，每个区间只有一个出现一次的数字
    def singleNumbers(self, nums):
        # 使用库函数将所有数异或
        # reduce函数，从nums中取前两个数计算结果，将结果再依次与取出来一个数继续计算
        # 若有初始化另一个数，则第一次也只从nums中取一个数
        xor = functools.reduce(lambda x, y: x ^ y, nums)
        # 取最低位的1
        bit = xor & -xor
        a = b = 0  # 初始化a, b
        for n in nums:
            # bit位为0的数作为一个区间，将该区间数全部异或起来，即得到出现一次的数a
            if bit & n == 0: a ^= n
            # bit位为1的数作为另一个区间，全部异或即得到另一个出现一次的数b
            else: b ^= n
        return [a, b]
