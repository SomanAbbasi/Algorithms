import sys
import random

input = sys.stdin.readline

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def solve():
    t = int(input())
    for _ in range(t):
        x, k = input().split()
        y_str = x * int(k)
        y = int(y_str)

        if is_prime(y):
            print("YES")
        else:
            print("NO")


solve()
