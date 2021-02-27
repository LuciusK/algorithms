#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if not commands:
            return 0
        direx = [0, 1, 0, -1]
        direy = [1, 0, -1, 0]
        curx, cury, curdire, ans = 0, 0, 0, 0
        com_len, obs_len = len(commands), len(obstacles)
        obstacle_set = {(obstacles[i][0], obstacles[i][1]) for i in range(obs_len)}

        for i in range(com_len):
            if commands[i] == -1:
                curdire = (curdire + 1) % 4
            elif commands[i] == -2:
                curdire = (curdire + 3) % 4
            else:
                for j in range(commands[i]):
                    nx = curx + direx[curdire]
                    ny = cury + direy[curdire]
                    if (nx, ny) not in obstacle_set:
                        curx = nx
                        cury = ny
                        ans = max(ans, curx * curx + cury * cury)
                    else:
                        break
        return ans
        
# @lc code=end