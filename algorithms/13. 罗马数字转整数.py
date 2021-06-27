class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        output = 0
        mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(n - 1):
            if mapping[s[i]] >= mapping[s[i + 1]]:
                output += mapping[s[i]]
            else:
                output -= mapping[s[i]]
        output += mapping[s[-1]]
        return output