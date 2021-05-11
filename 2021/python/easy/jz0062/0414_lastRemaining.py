class Solution:
    # 双端队列，time: NM, 超出时间限制
    def lastRemaining(self, n, m):
        queue = deque()
        for i in range(n): queue.append(i)
        while len(queue) > 1:
            for i in range(m - 1):
                queue.append(queue.popleft())
            queue.popleft()
        return queue[0]


    def lastRemaining(self, n, m):
        idx = 0  # 索引初始化为0，即当长度为1时，即该数就是最后一个剩下的数，并且索引为0
        # n和m定下后，最终值其实就是确定的, 假定最终值为: FINAL
        # 全程操作索引，idx(n)代表0,1,...,n-1中 FINAL 对应的索引
        # idx(n-1)代表删除一个值后，新起点环 FINAL 对应的索引
        # 0,1,...,n-1环，删除第一个元素后，对应新环：t,t+1,...,n,0,1,...,t-2, 其中t = m % n, 因为上一轮[0, n-1]删除的元素索引是(m-1)%n, 即新环起点为m%n
        # idx(n-1)是 FINAL 在新环索引[0,n-2]中对应的索引, 映射到原环索引[0,n-1]中索引为：(idx(n-1) + t) % n
        # 上述idx(n) = ( idx(n-1) + t) % n, 由新环索引[0,n-2]映射到原环删除元素后的索引[t,...,n,0,...,t-2]而来, 即x -> (x + t) % n
        # 即idx(n) = ( idx(n-1) + t ) % n --> idx(n) = ( idx(n-1) + m%n ) % n --> idx(n) = ( idx(n-1) + m ) % n

        # 遍历[2, n]的环长度，根据长度为1的环FINAL索引值: idx(1) = 0 (只有一个值，索引为0), 递推出idx(2),...,idx(n) 
        for lenth in range(2, n + 1):
            idx = (idx + m) % lenth  # FINAL在当前步的索引，等于 ( FINAL在上一步索引 + m ) % 当前步的环长度lenth
        return idx  # 倒推出idx(n)后，由于[0,n-1]的环状数组，索引值即对应的数值 
         

            
        
