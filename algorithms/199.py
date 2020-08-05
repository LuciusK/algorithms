class Solution: 
    def minFlips(self, target: str) -> int:
        target = list(target)
        if len(target) < 1 or target is None:
            return
        
        steps = 0
        base = ["0" for i in range(len(target))]

        for i, s in enumerate(target):
            if s != base[i]:
                base[i:] = s * (len(target)-i)
                steps += 1
            if base == target:
                break
        return steps


if __name__ == '__main__':
    target = "10111"
    solution = Solution()
    res = solution.minFlips(target)
    print(res)
