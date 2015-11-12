#include "my_func.h"

int array_div (const double *a, const double *b, double *c, int n) {
    for (int i=0; i<n; i++) {
        c[i] = a[i] / b[i];
    }
}
