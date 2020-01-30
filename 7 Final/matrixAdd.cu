#include <cuda.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define N 4
#define MIN 1
#define MAX 9

void random_ints(int a[][N]){
    // Remeber this nested for loop is single line so it just ends with ';', it doesn't need '{' and '}'
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            a[i][j] = rand() % (MAX + 1 - MIN) + MIN;
}

void print(int a[][N]){
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++) 
            printf("%2d", a[i][j]);
        printf("\n");
    }
}

__global__ void matAdd(int a[][N], int b[][N], int c[][N]){
    // insert your code here
}

int main(void) {
    int a[N][N], b[N][N], c[N][N]; // host copies of a, b, c
    int (*d_a)[N], (*d_b)[N], (*d_c)[N];  // device copies of a, b, c
    
    int size = (N * N) * sizeof(int);
    
    // Alloc space for device copies of a, b, c
    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_b, size);
    cudaMalloc((void **)&d_c, size);
    
    random_ints(a);
    random_ints(b);
    
    // Copy inputs to device
    cudaMemcpy(d_a, a, size, cudaMemHostToDevice);
    cudaMemcpy(d_b, b, size, cudaMemHostToDevice);
    
    int numBlocks = 1;
    dim3 threadsPerBlock(N, N);
    
    // Launch add() kernal on GPU with N blocks
    matAdd<<<numBlocks, threadsPerBlock>>>(d_a, d_b, d_c);
    
    // Copy result back to host
    cudaMemcpy(c, d_c, size, cudaMemcpyDeviceToHost);
    
    // Print Result
    print(a); printf("+\n"); print(b); printf("=\n"); print(c);
    
    // Cleanup
    cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);
    
    return 0;
}