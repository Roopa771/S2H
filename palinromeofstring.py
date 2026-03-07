class Solution:
    def isPalindrome(self, s):
        # code here
        rev=s[::-1]
        if s==rev:
            return 1
        else:
            return 0
        
