t = int(input())

for i in range(t):
    s = int(input())
    n = int(input())

    plus = 0

    for j in range(n):
        q, p = map(int, input().split())
        plus += q*p


    print(s + plus)
