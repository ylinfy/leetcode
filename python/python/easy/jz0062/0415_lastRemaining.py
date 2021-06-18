class Solution:
    def lastRemaining(self, n, m):
        # n, m定下来后，最终剩下的值也就固定了，假定最终剩下的值为F
        # idx: F在数环中的索引，环长度为1时，索引为0，即idx初始化为0
        # 长度为l的环索引[0, l-1], 在删除第m个数( 索引为(m-1) % l )后, 新环的起点索引相当于原环中的m%l
        # 即新环索引[0, l-2]映射到原长度为l的环删除一个元素后对应索引[m%l, m%l+1, m%l+2,...,l,0,...,m%l-2]
        # 得到映射关系：idx -> (idx + m%l) % l, 化简：idx -> (idx + m) % l
        # 因此由索引映射关系，可根据idx(n-1)得到idx(n) = (idx(n-1) + m) % l
        idx = 0
        for l in range(2, n + 1):
            idx = (idx + m) % l
        return idx
