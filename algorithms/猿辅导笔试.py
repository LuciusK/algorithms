def findbox(s:str) -> int:
    n = len(s)
    stack = []
    for i in range(n):
        if s[i] == '[':
            stack.append(-1)
        elif s[i] == ']':
            tmp = 1
            while stack[-1] != -1:
                tmp += stack.pop()
            stack.pop()
            stack.append(tmp)
        else:
            top = stack.pop()
            stack.append(top * int(s[i]))
    
    return sum(stack)

print(findbox('[[][[][][]2]]3'))
print(findbox('[]3'))
print(findbox('[][[][][]2]3'))
print(findbox('[][][[[]3[]2]2]2'))