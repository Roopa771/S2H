class MinStack:
    def __init__(self):
        # Each element is stored as (value, currentMin)
        self.stack = []

    def push(self, val: int) -> None:
        # If stack is empty, currentMin is val itself
        # Otherwise, currentMin is min(val, previous currentMin)
        curMin = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, curMin))

    def pop(self) -> None:
        # Remove the top element (value, currentMin)
        self.stack.pop()

    def top(self) -> int:
        # Return only the value part of the top element
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the currentMin part of the top element
        return self.stack[-1][1]
