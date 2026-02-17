#include <stdio.h>

int signature() {
    printf("Function with no arguments\n");
    return 10;
}

float signature(float a) {
    printf("Function with one argument\n");
    return 10 + a;
}

double signature(double a , double b) {
    printf("Function with two arguments\n");
    return 10 + a + b;
}

int main() {
    // Write C code here
int result1 = signature();
float result2 = signature(1.5);
double result3 = signature(1.5,2.5);

printf("result 1 %d\n ", result1);
printf("result 2 %f\n ", result2);
printf("result 3 %lf\n ", result3);


    return 0;
}