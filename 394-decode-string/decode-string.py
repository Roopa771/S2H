class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        
        for ch in s:
            if ch.isdigit():
                # Build the number (could be multiple digits)
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                # Push current string and number onto stack
                stack.append((curr_str, curr_num))
                # Reset for new segment
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                # Pop from stack and repeat
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                # Normal character
                curr_str += ch
        
        return curr_str
