class Solution:
    def reverse(self, x: int) -> int:
        negsign = x<0
        x = abs(x)
        res=0

        while x>0:
            res = res * 10 + x % 10
            x //= 10

        if negsign: res= -res

        if res> (2** 31)-1 or res < -2** 31:
            return 0

        return res
        