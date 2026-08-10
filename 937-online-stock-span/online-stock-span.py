class StockSpanner:

    def __init__(self):
        # Stack will store pairs: (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1  # At least today counts
        # Pop while stack top price <= current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]  # Add that span
            self.stack.pop()
        # Push current price with its span
        self.stack.append((price, span))
        return span
