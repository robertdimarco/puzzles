import java.util.HashMap;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class liarliar {

  private static int size;
  private static int count;
  private static GraphNode[] nodes;
  private static HashMap<String, Integer> names;

  private static int getN(String name) {
    if (!names.containsKey(name)) {
      names.put(name, count);
      nodes[count] = new GraphNode();
      count++;
    }
    return names.get(name);
  }

  private static void search(int root, boolean parity) {
    if (parity == false)
      count++;
    ArrayList<Integer> E = nodes[root].visit();
    for (int i = 0; i < E.size(); i++) {
      if (nodes[E.get(i)].visited == false) {
        search(E.get(i), !parity);
      }
    }
  }

  public static void main(String[] args) throws IOException {
    if (args.length == 0) {
      System.out.println("usage: ./liarliar <file>");
      System.exit(0);
    }
    BufferedReader file = new BufferedReader(
      new FileReader(args[0]));

    count = 0;
    names = new HashMap<String, Integer>();
    size = Integer.parseInt(file.readLine());
    nodes = new GraphNode[size];

    for (int i = 0; i < size; i++) {
      String[] words = (file.readLine()).split("\\s+");
      int x = getN(words[0]);
      for (int j = 0; j < Integer.parseInt(words[1]); j++) {
        int y = getN(file.readLine());
        nodes[x].add(y);
        nodes[y].add(x);
      }
    }
    file.close();
    count = 0;
    search(0, false);
    count = (count < (size-count)) ? size-count:count;
    System.out.println(count + " " + (size-count));
  }

  static class GraphNode {
    private boolean visited;
    private ArrayList<Integer> V;

    public GraphNode() {
      visited = false;
      V = new ArrayList<Integer>();
    }

    public void add(int node) {
      V.add(node);
    }

    public ArrayList<Integer> visit() {
      visited = true;
      return V;
    }
  }
}
