package battle;
import java.util.Random;
import battle.AttackResult.*;
import battle.Battleship.*;
import battle.Coordinate.*;
import battle.DuplicateEmailException.*;
import battle.GameOverException.*;
import battle.NoMovesMadeException.*;
import battle.Ship.*;
import battle.UnregisteredException.*;
import org.apache.thrift.*;
import org.apache.thrift.protocol.*;
import org.apache.thrift.transport.*;

public class BattleshipClient {
  public static int[] size = {5,4,3,3,2};
  public static final int port = 9031;
  public static final String server = "thriftpuzzle.facebook.com";
  public static Client client;

  public static int[][] boardClient;
  public static int[][] boardServer;

  public static void main(String[] args) throws TException, UnregisteredException, GameOverException, NoMovesMadeException, DuplicateEmailException {
    if (args.length < 1) {
      System.out.println("usage: ./battleship <email>");
    }
    TTransport transport;
    try {
      boardClient = new int[10][10];
      boardServer = new int[10][10];

      transport = new TSocket(server, port);
      TProtocol protocol = new TBinaryProtocol(transport);
      client = new Client(protocol);
      transport.open();

      if (args.length == 2)
        System.out.println("joining: " + args[1] + ", " + client.join(Integer.parseInt(args[1]), args[0]) + ", user: " + args[0]);
      else
        System.out.println("game id: " + client.registerClient(args[0]) + ", user: " + args[0]);

      placePieces();
      printGame();

      int sunk = 0, x = 0, y = 0;
      do {
        while(!client.isMyTurn());

        int result = client.attack(new Coordinate(x,y));
        if (result > 0 && result < 6) {
          sunk++;
          boardServer[x][y] = 1;
        }
        else if (result == 6) {
          boardServer[x][y] = 1;
        }
        else if (result == 7) {
          boardServer[x][y] = -1;
        }
        if (x == 9)
          y++;
        x = (x+1)%10;
        printGame();
      } while (sunk < 5);

      System.out.println(client.winGame());
      transport.close();
    }
    catch (TTransportException e) {
      System.out.println("Encountered TTransportException: " + e);
      System.exit(1);
    }
    catch (UnregisteredException e) {
      System.out.println("Encountered UnregisteredException: " + e);
      System.exit(1);
    }		
    catch (GameOverException e) {
      System.out.println("Encountered GameOverException: " + e);
      System.exit(1);
    }
    catch (DuplicateEmailException e) {
      System.out.println("Encountered DuplicateEmailException: " + e);
      System.exit(1);
    }
  }

  private static boolean overlap(boolean orientation, int x, int y, int length) {
    for (int i = 0; i < length; i++) {
      if (!orientation) {
        if (boardClient[x+i][y] != 0)
          return true;
      }
      else {
        if (boardClient[x][y+i] != 0)
          return true;
      }
    }
    return false;
  }

  private static void printGame() {
    System.out.println("Client:\t\t     Server:");
    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < 10; j++) {
        if (boardClient[i][j] == 0) {
          System.out.print("- ");
        } else if (boardClient[i][j] == -1) {
          System.out.print("x ");
        } else {
          System.out.print(boardClient[i][j] + " ");
        }
      }

      System.out.print("\t");

      for (int j = 0; j < 10; j++) {
        if (boardServer[i][j] == 0) {
          System.out.print("- ");
        } else if (boardServer[i][j] == -1) {
          System.out.print("x ");
        } else if (boardServer[i][j] == 1) {
          System.out.print("* ");
        } else {
          System.out.print(boardServer[i][j] + " ");
        }
      }
      System.out.print("\n");
    }
    System.out.println();
  }

  private static void placePieces() throws TException, UnregisteredException {
    System.out.println();
    Random z = new Random(System.currentTimeMillis());
    for (int i = 0; i < 5; i++) {
      boolean orientation;
      int x = 0, y = 0;
      do {
        orientation = z.nextBoolean();
        x = z.nextInt(10 - size[i]);
        y = z.nextInt(10);
        if (orientation) {
          y = x;
          x = z.nextInt(10);
        }
      } while (overlap(orientation, x, y, size[i]));
      for (int a = 0; a < size[i]; a++) {
        if (!orientation) {
          boardClient[x + a][y] = i + 1;
        } else {
          boardClient[x][y + a] = i + 1;
        }
      }
      System.out.println("placePiece " + i + ": " + client.placePiece(i+1, new Coordinate(x,y), orientation));
    }
    System.out.println();
  }
}
