#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        box = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_i = (i // 3) * 3 + j // 3

                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    box[box_i][num] = box[box_i].get(num, 0) + 1

                    if row[i][num] > 1 or col[j][num] > 1 or box[box_i][num] > 1:
                        return False
        
        return True


        
# @lc code=end

