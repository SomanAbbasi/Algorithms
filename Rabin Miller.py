import sys
import random

input = sys.stdin.readline

def is_prime(n, k=5):
    """
    Handle trivial case:
        If n≤3 directly return True for 2 and 3.
        if n id even return False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    """
    Write n - 1 as (2^s) * d:
        We factor out powers of 2 from n-1:
           =>  n-1=2s⋅d  where d is odd.
        For Example:
            => For n=37:
                n-1=36=2^2*9
            so s=2, and d=9
    """
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    """
    3. Pick a random base a
    =>      Choose a uniformly in [2, n-2].
    """
    """
    4. Compute a^d % n
            => x=a^d mod n
        if:
            x=1 or x=n-1 -> the base a passes this round.
        Otherwise:
        
            5. Repeat s-1 times: x = x² mod n
                => if any steps x=n-1, the base passes.
                => if after all squaring, x never becomes n-1, the base a 
                    is a witness for compositeness, and n is opposite.
    
    """
    
    """
    6. Repeat multiple rounds

        To reduce error probability, repeat the above test for k different bases (e.g. k = 5 or 10).
        If any base finds n composite → definitely composite.
        If all pass → probably prime with error ≤ 4^(-k).  
    Complexity:
        => Each round costs O(log n) modular exponentiation.
        => Total O(k log n) -> extremely fast.
    """

    
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
