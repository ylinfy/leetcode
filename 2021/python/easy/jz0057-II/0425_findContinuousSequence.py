class Solution:
    # 输入一个正整数target，输出所有和为target的连续正整数序列(至少两个数), target = 9 , res = [[2,3,4], [4,5]]
    # 假设连续正整数序列为[i,...,j], 则根据等差数列求和公式，有(i + j) * (j - i + 1) // 2 = t, 其中t是target
    # 令i,j间距为d, 即有d = j - i, 代入上述求和公式并化简，得到i = (t - d*(d+1)//2) // (d+1)
    # 由于i是正整数，则必须满足以下两条件:
    # 条件1：i > 0 => d * (d + 1) // 2 < t; 条件2：i是正整数 => (t - d*(d+1)//2) % (d+1) == 0
    # 根据题义连续正整数序列至少两个数，即d的取值范围是：1 ~ 满足条件d(d+1)//2 < t的值
    # 遍历间距d，把符合两条件的i全部找出来, j = i + d，即可求出所有连续正整数序列
    def findContinuousSequence(self, target):
        d, t, res = 1, target, []
        # 遍历d, 满足条件1
        while d * (d + 1) // 2 < t:
            # 满足条件2
            if (t - d * (d + 1) // 2) % (d + 1) == 0:
                i = (t - d * (d + 1) // 2) // (d + 1) 
                res.append(list(range(i, i + d + 1)))
            d += 1
        # 根据题义，结果中各连续正整数序列需要按首个元素从小到大排列
        # 而解题是间距从小到大的顺序，即首个元素是从大到小，因此反转一下结果列表
        return res[::-1]


    # 双指针，滑动区域
    # i, j双指针在[1, t//2 + 1]上滑动，初始化为最小两正整数1，2
    # 根据求和公式求出sum([i,...,j]), 和t比较，若比t大，则i自加1，减少区间范围，若比t小，则j自加1，增大区间范围
    def findContinuousSequence(self, target):
        i, j, t, res = 1, 2, target, []
        while j <= t // 2 + 1:
            s = (i + j) * (j - i + 1) // 2
            if s > t: i += 1
            elif s < t: j += 1
            else:
                res.append(list(range(i, j+1)))
                i += 2  # 也可以i += 1
        return res

            
        
        
        
