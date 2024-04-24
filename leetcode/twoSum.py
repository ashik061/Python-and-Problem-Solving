class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        helper = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in helper:
                return [helper[dif], i]
            else:
                helper[nums[i]] = i

    def twoSum2(self, nums: list[int], target: int) -> list[int]:    
        result=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
        return result


lst = [3,2,4]
target = 6

print(Solution.twoSum(Solution, lst, target))
            

