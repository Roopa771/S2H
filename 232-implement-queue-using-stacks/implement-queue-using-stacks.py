class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        # Always push onto inStack
        self.inStack.append(x)

    def pop(self) -> int:
        # Ensure outStack has the front element
        self._move()
        return self.outStack.pop()

    def peek(self) -> int:
        # Ensure outStack has the front element
        self._move()
        return self.outStack[-1]

    def empty(self) -> bool:
        return not self.inStack and not self.outStack

    def _move(self):
        # Move elements only when outStack is empty
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
