class MyStack:

    def __init__(self):
        self.qeue = deque()

    def push(self, x: int) -> None:
        self.qeue.append(x)

    def pop(self) -> int:
        res = self.qeue.pop()
        return res

    def top(self) -> int:
        return self.qeue[-1]
        

    def empty(self) -> bool:
        return len(self.qeue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()