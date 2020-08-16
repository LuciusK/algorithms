

class Leaderboard:

    def __init__(self):
        self.dic = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.dic[playerId] = self.dic.get(playerId, 0) + score

    def top(self, K: int) -> int:
        s = sorted([v for v in self.dic.values()], reverse=True)
        return sum(s[:K])

    def reset(self, playerId: int) -> None:
        self.dic[playerId] = 0