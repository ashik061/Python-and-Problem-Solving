class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                matrix[i][j],matrix[n-i-1][j]= matrix[n-i-1][j], matrix[i][j]
        
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    def rotate2(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        matrix.reverse()
        
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]



matrix =[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(matrix)
Solution.rotate2(Solution, matrix)
print(matrix)