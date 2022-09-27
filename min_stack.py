class MinStack:

    def __init__(self):
        self.list=[]

    def push(self, val: int):
        self.list.append(val)

    def pop(self):
        return self.list.pop()
        

    def top(self) :
        return self.list[len(self.list)-1]

    def getMin(self):
        return min(self.list)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
