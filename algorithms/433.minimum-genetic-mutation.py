#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        
        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "ACT",
            "T": "ACG"
        }
        queue = [(start, 0)]

        while queue:
            node, step = queue.pop(0)

            if node == end:
                return step
            
            for i, s in enumerate(node):
                for c in change_map[s]:
                    new = node[:i] + c + node[i+1:]
                    if new in bank:
                        queue.append((new, step + 1))
                        bank.remove(new)
        
        return -1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        bank = set(bank)
        length = 0
        change_map = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while start_set:
            length += 1
            new_set = set()
            for node in start_set:
                for i, s in enumerate(node):
                    for c in change_map[s]:
                        new = node[:i] + c + node[i + 1:]
                        if new in end_set:
                            return length
                        if new in bank:
                            new_set.add(new)
                            bank.remove(new)
            start_set = new_set
            if len(end_set) < len(start_set):
                start_set, end_set = end_set, start_set
        return -1

# @lc code=end

