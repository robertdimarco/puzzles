#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	if (argc < 1) {
		printf("Usage: meepmeep <in.txt>\n");
		exit(1);
	}
	printf("Meep meep!\n");
	return 0;
}
