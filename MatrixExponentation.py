
MOD = 10**9 + 7

def multiply(a, b):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
         (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
         (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]
    ]

def matrix_power(matrix, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
        n //= 2
    return result

def fibonacci(n):
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    result = matrix_power(base, n - 1)
    return result[0][0]

# Input
n = int(input("Enter n (0 ≤ n ≤ 10^18): "))
print("Fibonacci F(n) mod 10^9+7:", fibonacci(n))







#MOD = 10**9 + 7

# Multiply two 3x3 matrices modulo MOD
def multiply(a, b):
    res = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
    return res

# Exponentiation of 3x3 matrix
def matrix_power(matrix, n):
    result = [[1 if i==j else 0 for j in range(3)] for i in range(3)]  #identity matrix 3x3
    while n > 0:
        if n % 2 == 1:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
        n //= 2
    return result

# Compute nth Tribonacci number
def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    base = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
    result = matrix_power(base, n-2)
    # Multiply result with initial vector [T2, T1, T0] = [1,0,0]
    nth = (result[0][0]*1 + result[0][1]*0 + result[0][2]*0) % MOD
    return nth

# Input
n = int(input("Enter n (0 ≤ n ≤ 10^18): "))
print(f"Tribonacci T({n}) mod 10^9+7:", tribonacci(n))
