n = int(input())
start = ''
for i in range(1, n + 1):
    a = (str(i) + ' ') * i
    start += a
    if len(start.split()) >= n:
        print(*start.split()[:n])
        break

