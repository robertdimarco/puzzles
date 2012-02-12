import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.Math.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Comparator;

public class swarm {

  private static int capacity;
  private static Tbase[] feasible;
  private static int size;
  private static HashMap dataset;

  /*
  *  E(mineral profit) = m*P(z,s)
  *     m*e^(-63*s+10) = E*(e^(-63*s+10)+e^(-21*z))
  *        E*e^(-21*z) = e^(-63*s+10)*(m-E)
  *    ln(m-g)-63*s+10 = ln(E)-21*z
  *      ln(E)-ln(m-E) = -63*s+10+21*z
  *            E/(m-E) = e^(-63*s+10+21*z)
  *                  a = -63*s+10+21*z
  *                  b = e^(a)
  *                  E = (b*m)/(b+1)
  *
  *  a           e^a    round(5000*e^(a))/(1+e^(a))
  *------------------------------------------------
  * 01          2.72                          3,655
  * 02          7.39                          4,404
  * 03         20.09                          4,763
  * 04         54.60                          4,910
  * 05        148.41                          4,967
  * 06        403.43                          4,988
  * 07      1,096.63                          4,995
  * 08      2,980.96                          4,998
  * 09      8,103.08                          4,999
  * 10     22,026.47                          5,000
  * 11     59,874.14                          5,000
  * 12    162,754.79                          5,000
  *
  */
  private static int expectedProfit (int z, int s, int m) {
    long a = (-63*s + 10 + 21*z);
    if (m == 1) return m;
    if (a > 9) return m;
    if (a < 0) return 0;
    double b = Math.exp(a);
    return (int)Math.round((b*m)/(b+1));
  }

  /*
  * In order to be profitable, m*P(z,s) >= 1
  *
  * min = 1 = m*P(z,s)
  * 1 <= m*e^(-63*s+10)/(e^(-63*s+10)+e^(-21*z))
  * e^(-63*s+10)+e^(-21*z) <= m*e^(-63*s+10)
  * e^(-21*z) <= (m-1)*e^(-63*s+10)
  * ln(e^(-21*z)) <= ln((m-1)*e^(-63*s+10))
  * -21*z <= ln(m-1)-63*s+10
  *
  */
  private static boolean profitable (int z, int s, int m) {
    return ((Math.log(m-1)+(-63*s+10))/(-21) <= (z));
  }

  private static int minimum (int s, int m) {
    return (int)Math.ceil((Math.log(m-1) + (-63*s+10))/(-21));
  }

  public static void main(String[] args) throws IOException {
    long t0 = System.currentTimeMillis();

    if (args.length == 0) {
      System.out.println("usage: ./swarm <file>");
      System.exit(0);
    }

    BufferedReader file = new BufferedReader(
      new FileReader(args[0]));

    String line = file.readLine();
    int P = Integer.parseInt(line);
    for (int i = 0; i < P; i++) {
      String[] temp = (file.readLine()).split("\\s+");
      int t = Integer.parseInt(temp[0]);
      int z = Integer.parseInt(temp[1]);


      capacity = 1000;
      size = 1;
      feasible = new Tbase[capacity];
      feasible[0] = new Tbase(0,0,0);

      dataset = new HashMap();

      for (int j = 0; j < t; j++) {
        temp = (file.readLine()).split("\\s+");
        int s = Integer.parseInt(temp[0]);
        int m = Integer.parseInt(temp[1]);
        if(profitable(z,s,m)) {

          int prev = Integer.MIN_VALUE;
          int min = minimum(s,m);
          int last = expectedProfit(min,s,m);
          while (true) {
            if (prev == last)
              break;
            addTbase(j,min,s,m);
            prev = last;
            last = expectedProfit(min++,s,m);
          }
        }

      }
      ks(feasible,size,z);
    }

    file.close();
  }

  private static void addTbase(int index, int z,int s,int m) {
    if (size == capacity) {
      feasible = expandArray(feasible);
    }
    Tbase x = new Tbase(index,z,expectedProfit(z,s,m));
    dataset.put(index,z);
    feasible[size] = x;
    size++;
  }

  private static void ks(Tbase[] data, int N, int Z) {
    if (N == 0) {
      System.out.println("0 0\n");
      return;
    }

    int[][] c = new int[N][Z+1];
    for (int i=0;i < N; i++) {
      c[i][0] = 0;
    }
    for (int i=0;i < Z+1; i++) {
      c[0][i] = 0;
    }
    for (int i=1; i < N; i++) {
      for (int j=0; j < Z+1; j++) {
        if (data[i].z > j) {
          c[i][j] = c[i-1][j];
        }
        else {
          if((c[i-1][j]) == (data[i].m + c[i-1][j-data[i].z]))
            c[i][j] = c[i-1][j];
          else
            c[i][j] = Math.max(c[i-1][j], data[i].m + c[i-1][j-data[i].z]);
        }
      }
    }

    int solz = 0;
    int i = c.length -1 ;
    int[] solution = new int[i];
    int solsize = 0;

    int w = c[0].length -1;
    int[] marked = new int[i+1];

    for (int j=0; j<= i; j++) {
      while ((i >= 1) && (w >= 0)) {
        if (((i == 0) && (c[i][w] > 0)) || ((c[i][w] != c[i-1][w]))) {

          marked[i] = 1;
          w -= data[i].z;
          solz += data[i].z;
          solution[solsize] = data[i].i;
          solsize++;

        }
        else {
          marked[i] = 0;
        }
        i--;
      }
    }
    System.out.println(solz + " " + c[N-1][Z]);
    Arrays.sort(solution);
    for (int x = solution.length - solsize; x < solution.length; x++) {
      System.out.print(solution[x] + " " + dataset.get(solution[x]));
      if (x != solution.length-1) System.out.print(" ");
    }
    System.out.print("\n");  
  }

  /*
  * Double array size
  */
  private static Tbase[] expandArray(Tbase[] oldArray) {
    Tbase[] newArray = new Tbase[capacity*2];
    for(int i=0; i<capacity; i++) {
      newArray[i] = oldArray[i];
    }
    capacity *= 2;
    return newArray;
  }

  static class Tbase {

    private int i; //base index
    private int z; //Zerg cost
    private int m; //expected reward

    private Tbase(int i, int z, int m) {
      this.i = i;
      this.z = z;
      this.m = m;
    }
  }
}
