package com.facebook.puzzles.dinoisland.thrift;
import org.apache.thrift.*;
import org.apache.thrift.protocol.*;
import org.apache.thrift.meta_data.*;
import org.apache.thrift.transport.*;
import com.facebook.puzzles.dinoisland.thrift.AlreadyRegisteredException.*;
import com.facebook.puzzles.dinoisland.thrift.BadEggException.*;
import com.facebook.puzzles.dinoisland.thrift.Coordinate.*;
import com.facebook.puzzles.dinoisland.thrift.Dinosaur.*;
import com.facebook.puzzles.dinoisland.thrift.DinosaurState.*;
import com.facebook.puzzles.dinoisland.thrift.Direction.*;
import com.facebook.puzzles.dinoisland.thrift.EggResults.*;
import com.facebook.puzzles.dinoisland.thrift.EntityType.*;
import com.facebook.puzzles.dinoisland.thrift.GameOverException.*;
import com.facebook.puzzles.dinoisland.thrift.GrowResults.*;
import com.facebook.puzzles.dinoisland.thrift.LookResults.*;
import com.facebook.puzzles.dinoisland.thrift.MoveResults.*;
import com.facebook.puzzles.dinoisland.thrift.RegisterClientResults.*;
import com.facebook.puzzles.dinoisland.thrift.Sighting.*;
import com.facebook.puzzles.dinoisland.thrift.YouAreDeadException.*;
import java.util.List;
import java.lang.Thread;
import java.util.HashMap;
import java.util.Iterator;

public class DinoislandClient {
  public static void main(String[] args) {
    Data.killers = new HashMap<String, Integer>();
    new myDino(0);
  }
}

class Data {
  public static int eggs = 0;
  public static int starved = 0;
  public static int killed = 0;
  public static HashMap<String, Integer> killers;
  public static boolean semaphore = true;
}

class myDino implements Runnable {
  private long eggID;
  private Client client;
  private static TTransport transport;
  private static DinosaurState state;
  public static final int port = 9033;
  public static final String server = "thriftpuzzle.facebook.com";

  public myDino(long eggID) {
    this.eggID = eggID;
    new Thread(this).start();
  }

  public void run() {
    try {
      TTransport transport = new TSocket(server, port);
      TProtocol protocol = new TBinaryProtocol(transport);
      transport.open();
      client = new Client(protocol);
      RegisterClientResults result = client.registerClient("dimarco.robert@gmail.com", "Rob DiMarco", 1);
      if (eggID == 0)
        eggID = result.getEggID();
      state = client.hatch(eggID);
      Data.eggs++;

      int next = 4;

      while (true) {
        if ((state.getCalories() > 3*state.growCost) && (state.getSize() < 5)) {
          state = client.grow().getMyState();
        }
        else if (state.getCalories() > (3*state.eggCost + 2000)) {
          new myDino(client.egg(0, 2000).getEggID());
        }

        LookResults look = client.look(next);
        List<Sighting> plants = look.getThingsSeen();
        state = look.getMyState();

        Sighting closest = null;
        double minDistance = Double.MAX_VALUE;

        for (int k = 0; k < plants.size(); k++) {
          Sighting z = plants.get(k);
          if (z.type == 0) {

            if (distance(z.getCoordinate()) < minDistance) {
              minDistance = distance(z.getCoordinate());
              closest = z;
            }
          }
        }

        if (minDistance == Double.MAX_VALUE) {
          next--;
          if (next < 0)
            next = 7;
          continue;
        }

        next = moveTowards(closest.getCoordinate());
        state = client.move(next).getMyState();
      }

    } catch (TException e) {
      System.out.println(e);
      gameOver();
    } catch (AlreadyRegisteredException e) {
    } catch (BadEggException e) {
    } catch (YouAreDeadException e) {
      System.out.println(e);
      if ((e != null) && (e.description != null)) {
        if (e.description.indexOf("Starved") != -1) {
          Data.starved++;
        } else {
          Data.killed++;
          String killer = e.description.substring(e.description.indexOf("by a") + 5);
          if (Data.killers.containsKey(killer)) {
            Data.killers.put(killer, Data.killers.get(killer) + 1);
          } else {
            Data.killers.put(killer, 1);
          }
        }
      }
    } catch (GameOverException e) {
      if (Data.semaphore == true) {
        Data.semaphore = false;
        System.out.println();
        System.out.println(e.getMessage());
        System.out.println("Score: " + e.getScore());
        System.out.println("Highscores:\n" + e.getHighScoreTable());

        gameOver();
      }
    }
  }

  private static void gameOver() {
    System.out.println(Data.eggs + " eggs hatched, " + Data.starved + " starved to death, " + Data.killed + " killed");
    Iterator<String> i = Data.killers.keySet().iterator();
    while (i.hasNext()) {
      String killer = i.next();
      System.out.println(killer + " " + Data.killers.get(killer));
    }
    System.exit(0);
  }

  private double distance(Coordinate a) {
    int x = a.getColumn();
    int y = a.getRow();
    return Math.sqrt(x * x + y * y);
  }

  private int moveTowards(Coordinate a) {
    int x = a.getColumn();
    int y = a.getRow();
    if ((x < 0) && (y < 0)) {
      return 7 ;
    }
    if ((x > 0) && (y < 0)) {
      return 1;
    }
    if ((x < 0) && (y > 0)) {
      return 5;
    }
    if ((x > 0) && (y > 0)) {
      return 3;
    }
    if ((x < 0) && (y == 0)) {
      return 6;
    }
    if ((x > 0) && (y == 0)) {
      return 2;
    }
    if ((x == 0) && (y > 0)) {
      return 4;
    }
    return 0;
  }
}
