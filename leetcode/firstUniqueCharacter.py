from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i)==1:
                return s.index(i)
        return -1
    
    def firstUniqChar2(self, s: str) -> int:
        for i in s:
            if s.rindex(i)== s.index(i):
                return s.index(i)
        return -1
    
    def firstUniqChar3(self, s: str) -> int:    
        count = Counter(s)
        print(count)
        for i in s:
            if count[i]==1:
                return  s.index(i)
        return -1

    def firstUniqChar4(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                return i
        
        return -1


s = "leetcode"
print(Solution.firstUniqChar3(Solution,s))