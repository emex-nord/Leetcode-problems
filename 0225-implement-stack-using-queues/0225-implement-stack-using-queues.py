class MyStack:

    def __init__(self):
        self.stack = deque()
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        for i in range(len(self.stack) - 1):
            a = self.stack.popleft()
            self.stack.append(a)    

    def pop(self) -> int:
        if self.empty():
            return 
        else:
            return self.stack.popleft()
        
    def top(self) -> int:
        if self.empty():
            return 
        else:
            return self.stack[0]
        
    def empty(self) -> bool:
        return not len(self.stack)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()