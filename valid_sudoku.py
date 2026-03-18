"""
keytakeaway: formula to get the box number: (row//3) * 3 + (col//3)
we know that the board is 9x9 and each box is 3x3, so we can use integer division to get the box number
anytime we see grids/sub-boxes/group by chunks, we can use integer division to get the chunk number

36. Valid Sudoku
"""


from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        c = defaultdict(set) #will be updated until the end 
        r = defaultdict(set) #will be updated after each row iteration
        sq = defaultdict(set) #will be updated throughout 


        for rw in range(len(board)):
            for cl in range(len(board[rw])):
                if board[rw][cl] == ".":
                    continue 
                num = board[rw][cl]
                box = (rw//3) * 3 + (cl//3)
                if num in r[rw] or num in c[cl] or num in sq[box]:
                    return False
                r[rw].add(num)
                c[cl].add(num)
                sq[box].add(num)
        return True
                
                                
                
                

        return True