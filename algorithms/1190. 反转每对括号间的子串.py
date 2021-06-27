class Solution:
    def reverseParentheses(self, s: str) -> str:
        opened = []
        pair = {}
        for i, c in enumerate(s):
            if c =='(':
                opened.append(i)
            elif c == ')':
                j = opened.pop()
                pair[i], pair[j] = j, i 
        res = []
        i, d = 0, 1
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                d = -d 
            else:
                res.append(s[i])
            i += d
        return ''.join(res)

    def reverseParentheses1(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ')':
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                for t in tmp:
                    stack.append(t)
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)