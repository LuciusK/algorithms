class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if first == second:
            return True
        n1 = len(first)
        n2 = len(second)
        if abs(n1 - n2) > 1:
            return False
        
        i, j, k = 0, n1 - 1, n2 - 1
        while i < n1 and i < n2 and first[i] == second[i]:
            i += 1
        while j >= 0 and k >= 0 and first[j] == second[k]:
            k -= 1
            j -= 1
        return k - i < 1 and j - i < 1