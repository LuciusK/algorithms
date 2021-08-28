class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            try:
                stack.append(int(s))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.operate(num1, num2, s))
        return stack[0]
    
    def operate(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return int(num1 / num2)