# 344
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

# 541
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)
        
# 151
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
    
    def reverseWords1(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left < right and s[left] == " ":
            left += 1
        while left < right and s[right] == " ":
            right -= 1
        
        d, word = collection.deque(), []

        while left <= right:
            if s[left] == " " and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))

        return " ".join(d)

# 557
class Solution:
    def reverseWords(self, s: str) -> str:
        return "".join(word[::-1] for word in s.split(" "))
    
    def reverseWords1(self, s: str) -> str:
        stack, res, s = [], "", s + " "
        for i in s:
            stack.append(i)
            if i == " ":
                while stack:
                    res += stack.pop()
        return res[1:]

# 917
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)
    
    def reverseOnlyLetters1(self, S: str) -> str:
        ans = []
        j = len(S) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        return "".join(ans)

# 125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

    def isPalindrome1(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
        return True