class MinStack:

    def __init__(self):
        # Main stack to store values
        self.stack = []
        # Auxiliary stack to store minimums
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new min if stack is empty or val <= current min
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # If popped value is the current min, pop from minStack too
            if val == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
