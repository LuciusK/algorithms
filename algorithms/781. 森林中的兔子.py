class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        n = len(answers)
        ans, i = 0, 0
        while i < n:
            cur = answers[i]
            ans += cur + 1
            while cur > 0 and i + 1 < n and answers[i] == answers[i + 1]:
                cur -= 1
                i += 1
            i += 1
        return ans