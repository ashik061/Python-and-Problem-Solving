class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        index = len(digits)-1
        for i in range(index, -1, -1):
            digits[i]+=1
            if digits[i]!= 10:
                return digits
            else:
                digits[i]=0
        digits.insert(0,1)
        return digits
    
    def plusOne2(self, digits: list[int]) -> list[int]:
        number = ""
        for i in digits:
            number= number + str(i)
        number = int(number)
        number +=1
        result=[]
        while number>0:
            r=number%10
            number=number//10
            result.insert(0,r)
        return result

    

digits = [9,9,9]

print(Solution.plusOne(Solution,digits))