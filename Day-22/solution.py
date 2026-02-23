class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    # Push element x to the back of queue
    def push(self, x: int) -> None:
        self.in_stack.append(x)

    # Removes the element from in front of queue and returns it
    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            raise IndexError("Queue is empty")

        return self.out_stack.pop()

    # Get the front element
    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            raise IndexError("Queue is empty")

        return self.out_stack[-1]

    # Returns whether the queue is empty
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


# Example usage
if __name__ == "__main__":
    q = MyQueue()

    q.push(10)
    q.push(20)
    q.push(30)

    print("Front:", q.peek())   # 10
    print("Pop:", q.pop())      # 10
    print("Front after pop:", q.peek())  # 20
    print("Is Empty:", q.empty())