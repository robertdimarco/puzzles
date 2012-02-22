#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct coord { int id; double x, y; } coord;
typedef struct node { int id; double x, y, dSQ; struct node * left, * right; }  node;


double euclidianDistanceSq(node * a, node * b);
node* buildTree(coord * arr, int n, int depth);
void quickSort(coord arr[], int left, int right, short d);

void quickSort(coord arr[], int left, int right, short d) {
  /* d = 0, sort by y. d = 1, sort by x. */
  int i = left, j = right;
  coord tmp;
  coord pivot = arr[(left + right) / 2];

  /* Partition */
  while (i <= j) {
    if (d == 1) {
      while (arr[i].x < pivot.x)
        i++;
      while (arr[j].x > pivot.x)
        j--;
    }
    else {
      while (arr[i].y < pivot.y)
        i++;
      while (arr[j].y > pivot.y)
        j--;
    }

    if (i <= j) {
      tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
      i++;
      j--;
    }
  };

  /* Recursion */
  if (left < j)
    quickSort(arr, left, j, d);
  if (i < right)
    quickSort(arr, i, right, d);
}

node * buildTree(coord * arr, int n, int depth) {
  node *new = malloc(sizeof(node));
  coord *temp = malloc(n*sizeof(coord));
  int i, median = n/2, axis = depth % 2 + 1;

  quickSort(arr, 0, n-1, axis);

  new->x = arr[median].x;
  new->y = arr[median].y;
  new->id = arr[median].id;

  for (i = 0; i < median; i++)
    temp[i] = arr[i];
  if (i > 0)
    new->left = buildTree(temp, i, depth+1);
  for (i = median + 1; i < n; i++)
    temp[i-median-1] = arr[i];
  if (i-median-1 > 0)
    new->right = buildTree(temp, i-median-1, depth+1);
  return new;
}

double euclidianDistanceSq(node * a, node * b) {
  double c = a->x - b->x;
  double d = a->y - b->y;
  return ((c*c)+(d*d));
}

void addSolution(node * find, node * root, double ** sol, int ** solid, int * c) {
  int i, j = *c;
  double *arr = *sol;
  int *arr2 = *solid;
  double d = euclidianDistanceSq(find, root);

  if (*c == 0) {
    arr[0] = d;
    arr2[0] = root->id;
  }
  else if ((*c == 4) && (d > arr[3]))
    return;
  else {
    for (i = 0; i < *c; i++) {
      if (d < arr[i]) {
        j = i;
        break;
      }
    }
    for (i = *c; i > j; i--) {
      arr[i] = arr[i - 1];
      arr2[i] = arr2[i - 1];
    }
    arr[j] = d;
    arr2[j] = root->id;
  }
  if (*c < 4)
    (*c)++;
}

void kNearestNeighbor(node * find, node * root, double ** sol, int ** solid, int * c, int depth) {
  double z1, z2, axis = depth % 2;
  double d, *arr = *sol;
  node * a, * b;

  if (!root)
    return;

  a = root->right;
  b = root->left;
  d = euclidianDistanceSq(find, root);

  if (!a && !b) {
    addSolution(find, root, sol, solid, c);
    return;
  }

  if (!axis) {
    z1 = find->x;
    z2 = root->x;
  }
  else {
    z1 = find->y;
    z2 = root->y;
  }

  if (!a || (b && (z1 <= z2))) {
    a = root->left;
    b = root->right;
  }

  kNearestNeighbor(find, a, sol, solid, c, depth+1);

  if (b) {
    if ((*c < 4) || (((z1 - z2)*(z1 - z2)) <= arr[*c-1]))
      kNearestNeighbor(find, b, sol, solid, c, depth+1);
  }
  addSolution(find, root, sol, solid, c);
}

int main(int argc, char** argv) {
  /* Variable declarations */
  int i, j, k, n = 0;
  int capacity = 50;
  coord x;
  coord * arr;
  node *list = NULL;
  node *root = NULL;
  node *target = malloc(sizeof(*target));
  double * sol = malloc(sizeof(double)*5);
  int * solid = malloc(sizeof(int)*5);

  FILE *file = fopen(argv[1], "r");

  /* Ensure proper input file */
  if ((argc < 1) || (file == NULL)) {
    printf("usage: ./smallworld <in>\n");
    exit(1);
  }

  /* Load and parse input coordinates */
  arr = malloc(capacity*sizeof(coord));
  list = malloc(capacity*sizeof(node));
  while (fscanf(file,"%d", &x.id) > 0) {
    if (n == capacity) {
      capacity *= 2;
      arr = realloc(arr, capacity*sizeof(coord));
      list = realloc(list, capacity*sizeof(node));
    }
    fscanf(file,"%lf%lf", &x.x, &x.y);
    arr[n] = x;
    list[n].x = x.x;
    list[n].y = x.y;
    list[n].id = x.id;
    n++;
  }
  fclose(file);

  /* Build kd-tree */
  root = buildTree(arr, n, 0);
  free(arr);

  /* Kick off kNearestNeighbor algorithm */
  for (i = 0; i < n; i++){
    k = 0;
    kNearestNeighbor(&(list[i]), root, &sol, &solid, &k, 0);
    printf("%d ", list[i].id);
    for (j = 1; j < k; j++) {
      printf("%d", solid[j]);
      if (j != k-1)
        printf(",");
    }
    printf("\n");
  }

  free(list);
  return (EXIT_SUCCESS);
}
