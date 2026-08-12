class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # will store indices

        for i, temp in enumerate(temperatures):
            # While current temp is warmer than the last stacked day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)

        return answer
