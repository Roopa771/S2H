class MyCircularQueue:
    def __init__(self, k: int):
        # Initialize queue with fixed size k
        self.q = [0] * k
        self.size = k
        self.count = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Move rear forward circularly
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # Move front forward circularly
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
