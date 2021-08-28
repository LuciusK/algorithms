class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)
    
    def move(self, n, A, B, C):
        if n == 1:
            C.append(A.pop())
            return
        self.move(n - 1, A, C, B)
        C.append(A.pop())
        self.move(n - 1, B, A, C)