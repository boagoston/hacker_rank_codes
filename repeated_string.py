from collections import Counter

s = 'a'
n = 1000000000000
rest = n % len(s)
i = 0

A = s.count('a')
B = s[:n % len(s)].count('a') 

ans = (n // len(s)) * A + B


print (ans)






