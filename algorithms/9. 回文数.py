class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div  = 1
        while x // div >= 10:
            div *= 10
        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div //= 100
        return True

    def isPalindrome1(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revert = 0
        while x > revert:
            revert = revert * 10 + x % 10
            x //= 10
        return x == revert or x == revert // 10