#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
	int x, i;
	FILE *fin = fopen(argv[1],"r");

	if (argc < 1) {
		printf("Usage: hoppity <in.txt>\n");
		exit(1);
	}
	
	if (fin==NULL) {
		printf("Usage: hoppity <in.txt>\n");
		exit(1);
	}
	
	fscanf(fin, "%d", &x);
	fclose(fin);
	
	for (i=1; i<(x+1); i++) {
		if (i % 3 == 0) {
			if (i % 5 == 0) {
				printf("Hop\n");
			} else {
			  printf("Hoppity\n");
			}
		} else if (i % 5 == 0) {
			printf("Hophop\n");
		}
	}
	return 0;
}
