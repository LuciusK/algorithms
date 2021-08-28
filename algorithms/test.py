def lis(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n-2,-1,-1):
        for y in range(n-1,x,-1):
            if arr[x] < arr[y] and m[x] <= m[y]:
                m[x] += 1
        # print(m)
        max_value = max(m)
        result = []
        for i in range(n):
            if i > 0 and m[i] == m[i - 1]:
                result[-1] = arr[i]
                print(result[-1])
                continue
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
            
    print(m)
    return result
 
arr = [2,1,5,3,6,4,8,9,7]
print(lis(arr))