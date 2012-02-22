import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Hashtable;
import java.util.TreeSet;
import java.util.Iterator;

public class peaktraffic {

  private static int size;
  private static byte[][] connected;

  private static String[] email;
  private static Hashtable<String,Integer> address;

  private static int compsize;
  private static int[] compsub;
  private static int solution_size;
  private static TreeSet<String> solution;

  private static final int MAXSIZE = 8000;

  public static void main(String[] args) throws IOException {
    if (args.length == 0) {
      System.out.println("usage: ./peaktraffic <file>");
      System.exit(0);
    }

    BufferedReader file = new BufferedReader(
      new FileReader(args[0]));

    email = new String[MAXSIZE];

    address = new Hashtable<String, Integer>();
    connected = new byte[MAXSIZE][MAXSIZE];
    size = 0;

    String line; int a,b;
    while ((line = file.readLine()) != null) {
      a = b = 0;
      String[] temp = line.split("\t");

      // First see if we've seen e-mail before
      if (!address.containsKey(temp[1])) {
        email[a=size] = temp[1];
        address.put(temp[1],size);
        size++;
      }
      else {
        a = address.get(temp[1]);
      }
      if (!address.containsKey(temp[2])) {
        email[b=size] = temp[2];
        address.put(temp[2],size);
        size++;
      }
      else {
        b = address.get(temp[2]);
      }

      if ((connected[b][a] != 0))
        connected[a][b] = connected[b][a] = 1;
      else
        connected[a][b] = -1;
    }
    file.close();

    // Initialize diagonal & create number array
    int[] x = new int[size];
    for (int i = 0; i < size; i++) {
      x[i] = i;
      connected[i][i] = 1;
    }

    solution_size = 0;
    solution = new TreeSet<String>();

    compsize = 0;
    compsub = new int[size];

    bkv2(x, 0, size);

    Iterator i = solution.iterator();
    while (i.hasNext()){
      System.out.println(i.next());
    }
  }

  /*
  * Straightforward implementation of the Bron-Kerbosch "Algorithm 457 :: v2"
  * as designed in the cited paper using pivot-select. optimization. Takes a
  * boolean adjacency matrix and finds all maximal cliques.
  */
  private static void bkv2(int[] oldSet, int ne, int ce) {
    int minnod = ce;
    int nod = 0, pos = 0, s = 0, fixp = 0;
    int newne, newce, i, j, count, p, sel;
    int[] newSet = new int[ce];

    // Determine each counter value and look for a minimum
    for (i = 0; (i < ce) && (minnod != 0); i++) {
      p = oldSet[i];
      count = 0;

      // Count disconnections
      for (j = ne; (j < ce) && (count < minnod); j++) {
        if (connected[p][oldSet[j]] != 1) {
          count++;
          // Save position of potential candidate
          pos = j;
        }
      }

      // Test new minimum
      if (count < minnod) {
        fixp = p;
        minnod = count;
        if (i < ne) {
          s = pos;
        }
        else {
          s = i;
          // Pre-increment
          nod = 1;
        }
      }

      // Backtrack cycle
      for (nod = minnod + nod; nod >= 1; nod--) {
        p = oldSet[s];
        oldSet[s] = oldSet[ne];
        sel = oldSet[ne] = p;

        // Fill new set "not"
        newne = 0;
        for (i = 0; i < ne; i++) {
          if (connected[sel][oldSet[i]] == 1) {
            newSet[newne] = oldSet[i];
            newne++;
          }
        }

        // File new set "cand"
        newce = newne;
        for (i = ne + 1; i < ce; i++) {
          if (connected[sel][oldSet[i]] == 1) {
            newSet[newce] = oldSet[i];
            newce++;
          }
        }

        compsub[compsize] = sel;
        compsize++;

        if (newce == 0) {
          // Found clique with k >= 3
          if (compsize >= 3) {                         
            String[] clique = new String[compsize];
            for (int z = 0; z < compsize; z++) {
              clique[z] = email[compsub[z]];
            }
            Arrays.sort(clique);
            String current = "";
            for (int z = 0; z < compsize - 1; z++) {
              current += clique[z] + ", ";
            }
            current += clique[compsize-1];
            solution.add(current);
            solution_size++;
          }
        }
        else if (newne < newce) {
          bkv2(newSet, newne, newce);
        }

        // Remove from compsub
        compsize--;

        // Add to "not"
        ne++;
        if (nod > 1) {
          // Select a candidate disconnected to the fixed point
          for (s = ne; connected[fixp][oldSet[s]] == 1; s++);
        }
        newSet = new int[ce];
      }
    }
  }
}
