/*
Binet’s formula gives the n-th Fibonacci number in a closed form,
without using recursion or iteration:

            Fn=(ϕ^n -ψ^n​ )/sqrt(5)

        =>Fn=n-th Fibonancci number
        => ϕ= (1+sqrt(5))/2   = Golden ratio
        => ψ= (1-sqrt(5))/2  = Conjugate of Golden Ratio
*/

#include <iostream>
#include <cmath>
using namespace std;

long long fib(long long n)
{
    double sqrt5 = sqrt(5);
    double phi = (1 + sqrt5) / 2.0;
    double psi = (1 - sqrt5) / 2.0;

    // Binet Formula
    return round((pow(phi, n) - pow(psi, n)) / sqrt5);
}

int main()
{
    for (int n = 0; n <= 20; n++)
    {
        cout << "F_" << n << " = " << fib(n) << "\n";
    }
}


