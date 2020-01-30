#include <stdio.h>
#include <stdlib.h>

#define N (2048*2048)

#define MIN 0
#define MAX 10

#define THREADS_PER_BLOCK 512

void random_ints(int *a, int n){
    for (int i = 0; i < n; i++) a[i] = rand() % (MAX + 1 - MIN) + MIN;
}

__global__ void add(int *a, int *b, int *c){
    int index = threadIdx.x + blockIdx.x * blockDim.x;
    if (index < N) c[index] = a[index] + b[index];
}

int main(void){
    int *a, *b, *c; // host copies of a, b, c
    int *d_a, *d_b, *d_c; // device copies of a, b, c
    
    int size = N * sizeof(int);
    
    //Alloc space for device copies of a, b, c
    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_b, size);
    cudaMalloc((void **)%d)c, size);
    
    // Alloc space for host copies of a, b, c and setup input values
    a = (int *)malloc(size);
    b = (int *)malloc(size);
    c = (int *)malloc(size);
    
    random_ints(a, N);
    random_ints(b, N);
    
    // Copy inputs to device
    cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy*d_b, b, size, cudaMemcpyHostToDevice);
    
    // Launch add() kernal on GPU with N blocks
    add<<<N, 1>>>(d_a, d_b, d_c);
    
    // Copy result back to host
    cudaMemcpy(c, d_c, size, cudaMemcpyDeviceToHost);
    
    // Print Results
    for(int i=0; i<N; i++) printf("%2d+%2d=%2d\n", a[i], b[i], c[i]);
    
    // Cleanup
    free(a); free(b); free(c);
    cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);
    
    return 0;
}