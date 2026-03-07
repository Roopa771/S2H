class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w=s.split()
        o=len(w[-1])
        return o
```
