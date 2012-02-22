import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class usrbincrash {

  private static int capacity;
  private static int size;
  private static int[] cost;
  private static int[] weight;

  public static void main(String[] args) throws IOException {
    capacity = 50;
    if (args.length == 0) {
      System.out.println("usage: ./usrbincrash <file>");
      System.exit(0);
    }

    BufferedReader file = new BufferedReader(
      new FileReader(args[0]));

    String temp;
    size = 0;
    int target = Integer.parseInt(file.readLine());
    cost = new int[capacity];
    weight = new int[capacity];

    while((temp=file.readLine()) != null) {
      if (size == capacity) {
        cost = expandArray(cost);
        weight = expandArray(weight);
        capacity *= 2;
      }
      String[] tempa = temp.split("\\s+");
      weight[size] = Integer.parseInt(tempa[1]);
      cost[size] = Integer.parseInt(tempa[2]);
      size++;
    }

    int g = gcd(target,weight[0]);
    for (int i = 1; i < size; i++) {
      g = gcd(g, weight[i]);
    }

    if (g > 1) {
      for (int i = 0; i < size; i++) {
        weight[i] /= g;
      }
      target /= g;
    }

    int best = -1;
    int c;
    int[] table = new int[target];
    for (int i = 0; i < target; i++) {
      best = -1;
      for (int j = 0; j < size; j++) {
        c = cost[j];
        if (weight[j] <= i) {
          c += table[i - weight[j]];
        }
        if ((c < best) || (best == -1)) {
          best = c;
        }
      }
      table[i] = best;
    }
    System.out.println(table[target-1]);
  }

  /*
  *  Euclidean algorithm for GCD
  */
  private static int gcd (int a, int b) {
    int t = 0;
    while (b != 0) {
      t = b;
      b = a % b;
      a = t;
    }
    return a;
  }

  /*
  * expandArray doubles array length if necessary
  */
  private static int[] expandArray(int[] oldArray) {
    int[] newArray = new int[capacity*2];
    for (int i = 0; i < size; i++) {
      newArray[i] = oldArray[i];
    }
    return newArray;
  }
}
