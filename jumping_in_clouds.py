""" example
input
7
0 0 1 0 0 1 0

output
4

input
6
0 0 0 0 1 0

output
3


 """

n = int(input)
c = map(int, input.split(' '))
result = 0
i = 0
while i < n-1:
    if i + 2 >= n or c[i+2] == 1:
        i = i+1
        result += 1
    else:
        i = i+2
        result += 1

print(result)