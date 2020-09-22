#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary(object):
    class Node:
        def __init__(self):
            self.is_word = False
            self.next = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordDictionary.Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        for alpha in word:
            if alpha not in cur_node.next:
                cur_node.next[alpha] = WordDictionary.Node()
            cur_node = cur_node.next[alpha]
        if not cur_node.is_word:
            cur_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # 注意：这里要设置辅助函数
        return self.match(self.root, word, 0)

    def match(self, node, word, index):
        if index == len(word):
            return node.is_word
        alpha = word[index]
        if alpha == '.':
            for next in node.next:
                if self.match(node.next[next], word, index + 1):
                    return True
            # 注意：这里要返回
            return False
        else:
            # 注意：这里要使用 else
            if alpha not in node.next:
                return False
            # 注意：这里要使用 return 返回
            return self.match(node.next[alpha], word, index + 1)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

