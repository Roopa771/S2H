class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            op=haystack.index(needle)
            return op
        else:
            return -1
        
