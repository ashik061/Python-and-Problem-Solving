# This is a solution taken from the leeccode discussion. Understood the logic, but seems to tough to come out with the idea on my own. 

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        visited=[]
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val !='.':
                    visited+=((val,j),(i,val),(i//3,j//3,val))
                    print(visited)
                    print('\n')
        return len(visited)==len(set(visited)) 


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution.isValidSudoku(Solution,board))
