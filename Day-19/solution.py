class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if not self.stack:
            print("Stack is empty")
            return
        
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            print("Stack is empty")
            return -1
        
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            print("Stack is empty")
            return -1
        
        return self.min_stack[-1]

s = MinStack()

s.push(5)
s.push(3)
s.push(7)
s.push(3)

print(s.getMin())  # 3
s.pop()
print(s.getMin())  # 3
s.pop()
print(s.getMin())  # 3
s.pop()
print(s.getMin())  # 5