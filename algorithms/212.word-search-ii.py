#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

#@lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def search(i, j, node, pre, visited): # (i,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
            if '#' in node:
                res.add(pre)
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and board[_i][_j] in node\
                    and (_i, _j) not in visited:
                    search(_i, _j, node[board[_i][_j]], pre + board[_i][_j], visited | {(_i, _j)})

        res, m, n = set(), len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        
        return list(res)


# @lc code=end

