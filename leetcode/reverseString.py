class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()

    def reverseString2(self, s: list[str]) -> None:
        for i in range(len(s)//2):
            s[i],s[-i-1]=s[-i-1],s[i]
    
    def reverseString3(self, s: list[str]) -> None:
        i = 0
        j = len(s)-1

        while(j>i):
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1

s = ["h","e","l","l","o"]
print(s)
Solution.reverseString3(Solution, s)
print(s)