#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        used = set()
        cnt = 0
        s = "".join(str(c) for row in board for c in row)

        q = [s]
        while q:
            new = []
            for s in q:
                used.add(s)
                if s =="123450":
                    return cnt
                arr = [c for c in s]

                zero_index = s.index('0')
                for move in moves[zero_index]:
                    new_arr = arr[:]
                    new_arr[zero_index], new_arr[move] = new_arr[move], new_arr[zero_index]
                    new_s = "".join(new_arr)
                    if new_s not in used:
                        new.append(new_s)
            
            cnt += 1
            q = new
        return -1
    
    def slidingPuzzle1(self, board: List[List[int]]) -> int:
        from collections import namedtuple
        self.scores = [0] * 6
        goal_pos = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 0: (1, 2)}

        for num in range(6):
            self.scores[num] = [[abs(goal_pos[num][0] - i) + abs(goal_pos[num][1] - j) for j in range(3)]
             for i in range(2)]
        
        Node =  namedtuple('Node', ['heuristic_score', 'distance', 'board'])
        heap = [Node(0, 0, board)]
        closed = []

        while len(heap) > 0:
            node = heapq.heappop(heap)
            if self.get_score(node.board) == 0:
                return node.distance
            elif node.board in closed:
                continue
            else:
                for neighbor in self.get_neighbor(node.board):
                    if neighbor in closed:
                        continue
                    heapq.heappush(heap, Node(node.distance + 1 + self.get_score(neighbor), node.distance\
                        + 1, neighbor))
            closed.append(node.board)
        return -1 

    def get_neighbor(self,board):
        r, c = (0, board[0].index(0)) if 0 in board[0] else (1, board[1].index(0))
        res = []

        for offr, offc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= r + offr < 2 and 0 <= c + offc < 3:
                board1 = copy.deepcopy(board)
                board1[r][c], board1[r + offr][c + offc] = board1[r+offr][c+offc], board1[r][c]
                res.append(board1)
        return res

    def get_score(self, board):
        return sum([self.scores[board[i][j]][i][j] for i in range(2) for j in range(3)])

        
# @lc code=end

