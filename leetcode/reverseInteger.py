class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        y=0
        r=0
        while x>0:
            r=x%10
            x=x//10
            y=y*10+r
        y = sign * y
        if -2**31 <= y <= 2**31 - 1:
            return y
        return 0
    
    
    def reverse2(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = int(str(x)[::-1])
        x = sign * reversed_num
        if -2**31 <= x <= 2**31 - 1:
            return x
        return 0

x = -120
print(Solution.reverse(Solution,x))    