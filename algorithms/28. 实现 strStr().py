class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        haystack = ' ' + haystack
        needle = ' ' + needle
        next = [0 for _ in range(m + 1)]
        j = 0
        for i in range(2, m + 1):
            while j and needle[i] != needle[j + 1]:
                j = next[j]
            if needle[i] == needle[j + 1]:
                j += 1
            next[i] = j 
        
        j = 0
        for i in range(1, n + 1):
            while j and haystack[i] != needle[j + 1]:
                j = next[j]
            if haystack[i] == needle[j + 1]:
                j += 1
            if j == m:
                return i - m 
        return -1