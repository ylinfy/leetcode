class Solution:
    # 两个栈实现队列，一个负责出，一个负责进
    def __init__(self):
        self.IN, self.OUT = [], []
    
    # time: 1
    def appendTail(self, value):
        self.IN.append(value)
    
    # time: N
    def deleteHead(self):
        if self.OUT: return self.OUT.pop()
        if not self.IN: return -1
        while self.IN:
            self.OUT.append(self.IN.pop())
        return self.OUT.pop()
