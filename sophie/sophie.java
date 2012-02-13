import java.util.HashMap;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.DecimalFormat;

public class sophie {

  private static int size;
  private static double[] P;
  private static double[][] adjMatrix;
  private static HashMap<String, Integer> names;
  private static double best;
  private static DecimalFormat df;
  private static boolean[] visited;

  public static void main(String[] args) throws IOException {
    if (args.length == 0) {
      System.out.println("usage: ./sophie <file>");
      System.exit(0);
    }

    BufferedReader file = new BufferedReader(
      new FileReader(args[0]));

    df = new DecimalFormat("#.00");
    best = Double.POSITIVE_INFINITY;
    size = Integer.parseInt(file.readLine());
    P = new double[size];
    adjMatrix = new double[size][size];
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size; j++) {
        adjMatrix[i][j] = Double.POSITIVE_INFINITY;
      }
    }

    names = new HashMap<String, Integer>();
    for (int i = 0; i < size; i++) {
      String[] words = (file.readLine()).split("\\s+");
      names.put(words[0], i);
      double p = Double.parseDouble(words[1]);
      P[i] = p;
      adjMatrix[i][i] = 0;
    }
    int count = Integer.parseInt(file.readLine());
    for (int i = 0; i < count; i++) {
      String[] words = (file.readLine()).split("\\s+");
      int a = names.get(words[0]);
      int b = names.get(words[1]);
      int cost = Integer.parseInt(words[2]);
      adjMatrix[a][b] = adjMatrix[b][a] = cost;
    }

    /* All-pairs shortest paths */
    floydWarshall();

    /* Check for any unreachable locations */
    for (int i = 0; i < size; i++) {
      for (int j = i; j < size; j++) {
        if(adjMatrix[i][j] == Double.POSITIVE_INFINITY) {
          System.out.println("-1.00");
          System.exit(0);
        }
      }
    }

    /* Initialize visited vector */
    visited = new boolean[size];
    for (int i = 0; i < size; i++)
      visited[i] = false;
    visit(0, 0, 1);
    System.out.println(df.format(best));
  }

  private static double min(double a, double b) {
    if (b < a)
      return b;
    return a;
  }

  /*
  * Floyd-Warshall algorithm for all-pairs shortest pathes. This
  * unfortunately runs in O(n^3) time, however, actually performs better than
  * n consecutive calls to Dijkstra's algorithm because of its tight-looped
  * and short construction. (Source: Skiena - The Algorithm Design Manual 2e)
  */
  private static void floydWarshall() {
    for (int k = 0; k < size; k++) {
      for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
          if (i != j) {
            adjMatrix[i][j] = min(adjMatrix[i][j], 
            adjMatrix[i][k] + adjMatrix[k][j]);
          }
        }
      }
    }
  }

  private static void visit(int node, double ev, double probability) {
    visited[node] = true;
    probability -= P[node];
    boolean end = true;
    for (int i = 1; i < size; i++) {
      if (visited[i] == false) {
        end = false;
        if ((ev + (probability*adjMatrix[node][i])) < best)
          visit(i, ev + (probability*adjMatrix[node][i]) , probability);
      }
    }
    visited[node] = false;

    if (end == true) {
      if (((ev < best) && (best != -1)) || (best < 0))
        best = ev;
    }
  }
}
