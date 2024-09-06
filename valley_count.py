steps = 8
path = 'UDDDUDUU'
level = 0
valley = 0
sea_level = True

for i in path:
    if i == 'U':
        level += 1
    else:
        level -= 1

    if level < 0 and sea_level == True:
        valley += 1
        sea_level = False

    if level == 0:
        sea_level = True

print(valley)





###EXERCICIO
# https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
