/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package battle;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;
import org.apache.thrift.IntRangeSet;
import java.util.Map;
import java.util.HashMap;

public class Ship {
  public static final int CARRIER = 1;
  public static final int BATTLESHIP = 2;
  public static final int DESTROYER = 3;
  public static final int SUBMARINE = 4;
  public static final int PATROL = 5;

  public static final IntRangeSet VALID_VALUES = new IntRangeSet(
    CARRIER, 
    BATTLESHIP, 
    DESTROYER, 
    SUBMARINE, 
    PATROL );

  public static final Map<Integer, String> VALUES_TO_NAMES = new HashMap<Integer, String>() {{
    put(CARRIER, "CARRIER");
    put(BATTLESHIP, "BATTLESHIP");
    put(DESTROYER, "DESTROYER");
    put(SUBMARINE, "SUBMARINE");
    put(PATROL, "PATROL");
  }};
}