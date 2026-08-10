class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # Split by '/' to handle multiple slashes
        parts = path.split('/')
        
        for part in parts:
            if part == '' or part == '.':
                # Skip empty or current directory
                continue
            elif part == '..':
                # Go up one level if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory/file name
                stack.append(part)
        
        # Join stack into canonical path
        return '/' + '/'.join(stack)
