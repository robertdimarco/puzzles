package simon;
import java.util.*;
import simon.SimonSays.*;
import simon.Color.*;
import org.apache.thrift.*;
import org.apache.thrift.protocol.*;
import org.apache.thrift.transport.*;

public class SimonSaysClient {

  public static final String email = "user@domain.com";

  public static void main(String[] args) throws TException {
    if (args.length < 2) {
      System.exit(0);
    }

    TTransport transport;
    try {
      transport = new TSocket(args[0], Integer.parseInt(args[1]));
      TProtocol protocol = new TBinaryProtocol(transport);
      Client client = new Client(protocol);
      transport.open();

      client.registerClient(email);
      do {

        List<Integer> colors = client.startTurn();
        Iterator<Integer> i = colors.iterator();
        while (i.hasNext()) {
          int x = i.next();
          client.chooseColor(x);
        }
        } while (!client.endTurn());
        System.out.println(client.winGame());
        transport.close();

      }
    catch (TTransportException e) {
      System.exit(1);
    }
  }
}
