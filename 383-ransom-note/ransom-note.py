class Solution:
    from collections import Counter
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=Counter(magazine)
        for x in ransomNote:
            if c[x]==0:
                return False
            c[x]=c[x]-1
        return True        