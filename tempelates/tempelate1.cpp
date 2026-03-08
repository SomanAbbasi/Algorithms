/*
   Competitive Programming Template
   Author: Soman Abbasi
   Features:
     - Fast I/O
     - Useful macros
     - Debug utilities
     - Predefined constants
     - Common type aliases
     - Modular structure for quick problem solving
*/

#include <bits/stdc++.h>
using namespace std;

//---------------------- CONSTANTS ----------------------
const int INF = 1e9 + 5;
const long long LINF = 1e18 + 5;
const int MOD = 1e9 + 7; // Common modulus
const double PI = acos(-1.0);

//---------------------- TYPE ALIASES -------------------
using ll = long long;
using ull = unsigned long long;
using ld = long double;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vll = vector<ll>;
using vpii = vector<pii>;

//---------------------- MACROS ------------------------
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())
#define fi first
#define se second
#define endl "\n"

//---------------------- FAST I/O ----------------------
void fast_io() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

//---------------------- DEBUGGING --------------------
#ifdef LOCAL
#define debug(x) cerr << #x << " = " << x << endl;
#else
#define debug(x)
#endif

//---------------------- HELPER FUNCTIONS --------------
ll mod_add(ll a, ll b, ll m = MOD) { return (a % m + b % m + m) % m; }
ll mod_sub(ll a, ll b, ll m = MOD) { return (a % m - b % m + m) % m; }
ll mod_mul(ll a, ll b, ll m = MOD) { return ((a % m) * (b % m)) % m; }
ll mod_pow(ll a, ll b, ll m = MOD) {
    ll res = 1;
    a %= m;
    while (b) {
        if (b & 1) res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}
ll mod_inv(ll a, ll m = MOD) { return mod_pow(a, m - 2, m); } // Only if m is prime

//---------------------- MAIN LOGIC --------------------
void solve() {
    // Example
    int n;
    cin >> n;
    vi arr(n);
    for(int &x : arr) cin >> x;

    // Sample operation: sum
    ll sum = 0;
    for(int x : arr) sum += x;
    cout << sum << endl;
}

//---------------------- MAIN -------------------------
int main() {
    fast_io();

    int t = 1;
    cin >> t; // Uncomment if multiple test cases
    while(t--) {
        solve();
    }

    return 0;
}

/*-------------------- NOTES ------------------------
1. Use __int128 for very large integer arithmetic if needed.
2. Use ordered_set from pbds for advanced queries (requires extra header).
3. Add commonly used algorithms (binary search, DSU, segment trees) in separate functions.
4. Use LOCAL macro to enable debug prints without affecting online submission.
----------------------------------------------------*/