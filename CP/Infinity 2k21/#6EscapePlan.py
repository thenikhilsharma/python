#VIPS

'''
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

#define ll long long
#define mp make_pair
#define pii pair<int, int>
#define f first
#define s second

const int MOD = 1000000007;
const ll INF = 1000000000000000000;

int n, a[1000005], parent[1000005], sz[1000005];
ll dp[1000005];
vector<int> edges[1000005];

int leaf(int x) {
    return edges[x].size() == 1 && x > 1;
}

void dfs(int v, int p) {
    sz[v] = leaf(v);
    parent[v] = p;
    for (int i : edges[v]) {
        if (i != p) {
            dfs(i, v);
            sz[v] += sz[i];
        }
    }
}

ll ans(int x) {
    if (dp[x] != -1) return dp[x];
    if (leaf(x)) return dp[x] = a[x] ? a[x] : INF;
    dp[x] = 0;
    for (int i : edges[x]) {
        if (i != parent[x] && dp[x] < INF) dp[x] += ans(i);
    }
    if (a[x]) dp[x] = min(dp[x], 1ll*sz[x]*a[x]);
    return dp[x];
}

void solve() {
    int x, y;
    scanf("%d", &n);
    for (int i=1; i<=n; i++) {
        edges[i].clear();
        dp[i] = -1;
    }
    for (int i=1; i<n; i++) {
        scanf("%d%d", &x, &y);
        edges[x].push_back(y);
        edges[y].push_back(x);
    }
    for (int i=1; i<=n; i++) scanf("%d", &a[i]);
    if (n == 1) {
        printf("%d\n", a[1]);
        return;
    }
    dfs(1, 1);
    printf("%lld\n", ans(1));
}

int main() {
    int tests = 1;
    scanf("%d", &tests);
    while (tests--) solve();
}
'''