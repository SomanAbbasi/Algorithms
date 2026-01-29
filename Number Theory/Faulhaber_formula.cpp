/*
Faulhaber’s formula gives a closed-form expression for the sum of powers 
of the first n natural numbers.

        Sp(n) =   1^p+2^p+3^p+⋯+n^p
        from fractions import Fraction
from math import comb

def bernoulli_numbers(m):
    B=[Fraction(0)]*(m+1)
    B[0]=Fraction(1)
    for n in range(1,m+1):
        s=Fraction(0)
        for k in range(n):
            s+=comb(n+1,k)*B[k]
        B[n]=-s/Fraction(n+1)
    return B

def faulhaber(n,p):
    B=bernoulli_numbers(p)
    s=Fraction(0)
    for j in range(p+1):
        s+=comb(p+1,j)*B[j]*n**(p+1-j)
    return s//(p+1)

n=int(input())
p=int(input())
print(faulhaber(n,p))

*/

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Compute Bernoulli numbers B0, B1, ..., Bm
vector<long double> bernoulli(int m){
    vector<long double> B(m+1,0.0L);
    B[0] = 1.0L;
    for(int n=1; n<=m; n++){
        long double s = 0.0L;
        for(int k=0; k<n; k++){
            long double bin = 1.0L;
            for(int i=0; i<k; i++) bin *= (n+1-i)/(long double)(i+1);
            s += bin * B[k];
        }
        B[n] = -s/(n+1);
    }
    return B;
}

// Faulhaber formula
long long faulhaber(long long n, int p){
    auto B = bernoulli(p);
    long double s = 0.0L;
    for(int j=0; j<=p; j++){
        long double bin = 1.0L;
        for(int i=0; i<j; i++) bin *= (p+1-i)/(long double)(i+1);
        s += bin * B[j] * pow((long double)n, p+1-j);
    }
    s /= (p+1);
    return (long long)(s + 0.5); // rounding to nearest integer
}

int main(){
    long long n;
    int p;
    cout << "Enter n and p: ";
    cin >> n >> p;
    cout << faulhaber(n,p) << endl;
    return 0;
}

