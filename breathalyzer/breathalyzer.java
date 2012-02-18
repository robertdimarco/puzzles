import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;

public class breathalyzer {

  private static int[] lengths;
  private static ArrayList<char[]> post;
  private static ArrayList<char[]> wordList;
  private static ArrayList<char[]> wordListSub4;
  private static ArrayList<char[]> wordList10;
  private static final String dictFile = "/var/tmp/twl06.txt";

  private static final void getWordList() throws IOException {
    lengths = new int[25];
    for (int i = 0; i < 25; i++)
      lengths[i] = 0;

    BufferedReader input = new BufferedReader(
      new FileReader(dictFile));
    wordList = new ArrayList<char[]>();
    wordListSub4 = new ArrayList<char[]>();
    wordList10 = new ArrayList<char[]>();
    String temp = input.readLine();
    while (temp != null) {
      wordList.add(temp.toCharArray());
      if (temp.length() < 5) {
        wordListSub4.add(temp.toCharArray());
      }
      if (temp.length() < 10) {
        wordList10.add(temp.toCharArray());
      }

      temp = input.readLine();
    }
    input.close();
  }

  private static final void getPost(String fileName) throws IOException {
    BufferedReader input = new BufferedReader(
      new FileReader(fileName));
    post = new ArrayList<char[]>();
    String temp = input.readLine();
    while (temp != null) {
      StringTokenizer st = new StringTokenizer(temp);
      while (st.hasMoreTokens()) {
        post.add(st.nextToken().toUpperCase().toCharArray());
      }
      temp = input.readLine();
    }
    input.close();
  }

  private static final int compute(char[] word, char[] dict, int[][] memo, int start) {
    for (int i = 0; i <= word.length; i++) {
      for (int j = start; j <= dict.length; j++) {
        if (i == 0) {
          if (j == 0) {
            memo[i][j] = 0;
          } else {
            memo[i][j] = 1 + memo[i][j - 1];
          }
        }
        else if (j == 0) {
          memo[i][j] = 1 + memo[i - 1][j];
        } else {
          if (word[i - 1] == dict[j - 1]) {
            memo[i][j] = memo[i - 1][j - 1];
          } else {
            int c = 1 + memo[i - 1][j - 1];
            int a = 1 + memo[i - 1][j];
            int b = 1 + memo[i][j - 1];
            a = (a < b) ? a : b;
            memo[i][j] = (a < c) ? a : c;
          }
        }
      }
    }
    return memo[word.length][dict.length];
  }

  public static void main(String[] args) throws IOException {
    getWordList();
    getPost(args[0]);
    int total = 0;
    char[] oldWord = {' '};
    int[][] memo = new int[25][25];
    for (char[] word : post) {
      int score = Integer.MAX_VALUE;
      int length = word.length;

      if (length < 4) {
        for (char[] dict : wordListSub4) {
          if (Math.abs(length - dict.length) < score) {
            int start = 0;
            while ((start < dict.length && start < oldWord.length) && dict[start] == oldWord[start]) {
              start++;
            }

            if (score == 1 && word[0] < dict[0]) {
              break;
            }
            int temp = compute(word, dict, memo, start);
            score = (score < temp) ? score : temp;
            if (score == 0) {
              break;
            }
            oldWord = dict;
          }
        }
      } else if (length < 8) {
        for (char[] dict : wordList10) {
          if (Math.abs(length - dict.length) < score) {
            int start = 0;
            while ((start < dict.length && start < oldWord.length) && dict[start] == oldWord[start]) {
              start++;
            }

            if (score == 1 && word[0] < dict[0]) {
              break;
            }
            int temp = compute(word, dict, memo, start);
            score = (score < temp) ? score : temp;
            if (score == 0) {
              break;
            }
            oldWord = dict;
          }
        }
      } else {
        for (char[] dict : wordList) {
          if (Math.abs(length - dict.length) < score) {
            int start = 0;
            while ((start < dict.length && start < oldWord.length) && dict[start] == oldWord[start]) {
              start++;
            }

            if (score == 1 && word[0] < dict[0]) {
              break;
            }
            int temp = compute(word, dict, memo, start);
            score = (score < temp) ? score : temp;
            if (score == 0) {
              break;
            }
            oldWord = dict;
          }
        }
      }
      total += score;
      oldWord = new char[]{'='};
    }
    System.out.println(total);
  }
}
