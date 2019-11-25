#include <stdio.h>
#include "mpi.h"

int main(int argc, char *argv[])
{
	MPI_Init(&argc, &argv);
	
	/* code goes here */
	
	MPI_Finalize();
	return 0;
}
