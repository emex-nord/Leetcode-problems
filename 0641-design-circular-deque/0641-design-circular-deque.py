class MyCircularDeque:
#deque implementation using list
    def __init__(self, k: int):
        self.k = k
        self.deque = []
        self.size = 0
        
    def insertFront(self, value: int) -> bool:
        if self.size < self.k:
            self.deque.insert(0,value)
            self.size += 1
            return True
        return False
            
    def insertLast(self, value: int) -> bool:
        if self.size < self.k:
            self.deque.append(value)
            self.size += 1
            return True
        return False    

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.deque.pop(0)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.deque.pop()
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return (self.size == self.k)
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()