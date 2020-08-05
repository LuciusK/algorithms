#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import defaultdict, deque
from typing import List
import string


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res
        
        successors = defaultdict(set)

        found = self.__bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res
    
    def __bfs(self, beginWord, endWord, word_set, successors):
        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        found = False
        word_len = len(beginWord)
        next_level_visited = set()

        while queue:
            current_size = len(queue)
            for i in range(current_size):
                current_word = queue.popleft()
                word_list = list(current_word)

                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)

                        if next_word in word_set:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True
                                
                                if next_word not in next_level_visited:
                                    next_level_visited.add(next_word)
                                    queue.append(next_word)
                                
                                successors[current_word].add(next_word)
                    word_list[j] = origin_char
            if found:
                break
            visited |= next_level_visited
            next_level_visited.clear()
        return found
    
    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return
        
        if beginWord not in successors:
            return 
        
        successors_words = successors[beginWord]
        for next_word in successors_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        found = self.__bidirectional_bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res
    
    def __bidirectional_bfs(self, beginWord, endWord, word_set, successors):
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)

        begin_visited = set()
        begin_visited.add(beginWord)

        end_visited = set()
        end_visited.add(endWord)

        found = False
        forward = True
        word_len = len(beginWord)
        while begin_visited:
            if len(begin_visited) > len(end_visited):
                begin_visited, end_visited = end_visited, begin_visited
                forward = not forward
            
            next_level_visited = set()
            for current_word in begin_visited:
                word_list = list(current_word)
                for j in range(word_len):
                    origin_char = word_list[j]
                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word in end_visited:
                                found = True
                                self.__add_to_successors(successors, forward, current_word, next_word)
                            if next_word not in visited:
                                next_level_visited.add(next_word)
                                self.__add_to_successors(successors, forward, current_word, next_word)
                    word_list[j] = origin_char
            begin_visited = next_level_visited

            visited |= next_level_visited
            if found:
                break
        return found
    
    def __add_to_successors(self, successors, forward, current_word, next_word):
        if forward:
            successors[current_word].add(next_word)
        else:
            successors[next_word].add(current_word)
    
    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return 
        
        if beginWord not in successors:
            return 
        
        successors_words = successors[beginWord]
        for next_word in successors_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()
            



# @lc code=end

