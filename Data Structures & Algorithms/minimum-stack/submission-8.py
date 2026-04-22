class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimumVal = min(val, self.minimum[-1] if self.minimum else val)
        self.minimum.append(minimumVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
