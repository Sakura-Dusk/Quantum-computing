#include<bits/stdc++.h>

namespace quantum {
    const int N = 2e2 + 100;
    struct matrix {
        int n, m;
        double a[N][N];
    };

    matrix operator *(matrix x, matrix y) {
        matrix re;
        re.n = x.n; re.m = y.m;
        assert(x.m == y.n);
        for (int i = 0; i < re.n; i++)
            for (int j = 0; j < re.m; j++) re.a[i][j] = 0;
        for (int k = 0; k < x.m; k++)
            for (int i = 0; i < re.n; i++)
                for (int j = 0; j < re.m; j++)
                    re.a[i][j] += x.a[i][k] * y.a[k][j];
        return re;
    }
    matrix AT(matrix A) {
        matrix re;
        re.n = A.m; re.n = A.n;
        for (int i = 0; i < re.n; i++)
            for (int j = 0; j < re.m; j++) re.a[i][j] = A.a[j][i];
        return re;
    }

    struct quantum {
        int size;
        double p[N];//0~2^size-1
    };

    quantum merge(quantum A, quantum B) {
        quantum re;//A:0~A.size-1, B:A.size~A.size+B.size-1
        re.size = A.size + B.size;
        for (int i = 0; i < (1 << A.size); i++)
            for (int j = 0; j < (1 << B.size); j++)
                re.p[i + (j << A.size)] = A.p[i] * B.p[j];
        return re;
    }

    matrix get_unitary_matrix(quantum *f, quantum *g, int n) {
        matrix re;
        re.n = (1 << n) - 1; re.m = (1 << n) - 1;
        for (int i = 0; i < re.n; i++)
            for (int j = 0; j < re.m; j++) re.a[i][j] = 0;
        for (int i = 0; i < (1 << n); i++) {
            for (int j = 0; j < (1 << n); j++)
                for (int k = 0; k < (1 << n); k++) 
                    re.a[j][k] += f[i].p[j] * g[i].p[k];
        }
        return re;
    }
}
