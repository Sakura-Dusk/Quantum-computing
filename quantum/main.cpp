#include "unitary-matrix.h"
#include<bits/stdc++.h>

using namespace std;

const int N = 2e2 + 100;
quantum::quantum f[N], g[N];

int main() {
    int n;
    scanf("%d", &n);
    for (int S = 0; S < (1 << n); S++) {//读入对于 i 状态 input 的 output（读入每个结果的可能）
        quantum::quantum b;
        b.size = 0; b.p[0] = 1;
        for (int i = 1; i <= n; i++) {
            double p; cin >> p;
            quantum::quantum tmp; tmp.size = 1; tmp.p[1] = p * p; tmp.p[0] = (1.0 - p) * (1.0 - p);
            b = quantum::merge(b, tmp);
            for (int i = 0; i < (1 << n); i++) printf("%lf ", b.p[i]); printf("\n");
        }
        f[S].size = n;
        for (int i = 0; i < (1 << n); i++) f[S].p[i] = 0;
        f[S].p[S] = 1;// |i>
        g[S] = b;// |result_i>
    }
    quantum::matrix ans = quantum::get_unitary_matrix(f, g, n);
    for (int i = 0; i < (1 << n); i++) {//输出酉矩阵
        for (int j = 0; j < (1 << n); j++) {
            printf("%lf ", ans.a[i][j]);
        }
        printf("\n");
    }
    return 0;
}