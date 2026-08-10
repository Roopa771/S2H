from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Always push into q1
        self.q1.append(x)

    def pop(self) -> int:
        # Move all elements except last from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        # Last element is the "top" of stack
        top = self.q1.popleft()
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        return top

    def top(self) -> int:
        # Similar to pop but keep the last element
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top = self.q1.popleft()
        self.q2.append(top)  # put it back
        self.q1, self.q2 = self.q2, self.q1
        return top

    def empty(self) -> bool:
        return not self.q1
