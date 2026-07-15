class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        pro=1
        while n>0:
            rem=n%10
            sum=sum+rem
            pro=pro*rem
            n=n//10
        return(pro-sum)