def maxgongyue(a, b):
    if not (type(a) == 'int') or not (type(b) == 'int'):
        raise TypeError("input digit number")
    if a <= 0 or b <= 0:
        raise TypeError("input postive integer")
    minnum = min(a, b)
    for div in range(minnum, 0, -1):
        if a % div == 0 and b % div == 0:
            return div

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a  

print(gcd(10, 1000))