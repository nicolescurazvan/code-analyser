#include <stdio.h>
#include <stdlib.h>

typedef struct matrix {
    int *data, **rows, m, n;
} matrix;

matrix new_matrix(int m, int n) {
    matrix mat;
    mat.data = malloc(m * n * sizeof(int));
    mat.rows = malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        mat.rows[i] = mat.data + (n * i);
    }
    mat.m = m;
    mat.n = n;
    return mat;
}

void delete_matrix(matrix *mat) {
    free(mat->data);
    free(mat->rows);
}

matrix multiply(matrix A, matrix B) {
    matrix C = new_matrix(A.m, B.n);
    for (int i = 0; i < A.m; i++) {
        for (int j = 0; j < B.n; j++) {
            C.rows[i][j] = 0;
            for (int k = 0; k < A.n; k++) {
                C.rows[i][j] += A.rows[i][k] * B.rows[k][j];
            }
        }
    }
    return C;
}


int main() {
    matrix I = new_matrix(2, 2);
    I.rows[0][0] = 1;
    I.rows[0][1] = 0;
    I.rows[1][0] = 0;
    I.rows[1][1] = 1;
    matrix A = multiply(I, I);
    printf(" %d %d \n %d %d", A.rows[0][0], A.rows[0][1], A.rows[1][0], A.rows[1][1]);
    return 0;
}