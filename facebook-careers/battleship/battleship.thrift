/* Thrift Battleship
 * Puzzle Master (1051962371@facebook.com)
 * This file describes the game interface for your Battleship client to interact
 * with the Battleship server.  Compile this file using the Thrift compiler to
 * generate skeleton code or stubs in the language(s) of your choice.
 * The rules of the Battleship are simple and are explained in the problem
 * statement on the Puzzles page.  In terms of running a client to successfully
 * play the game, your code should loosely follow this pseudocode:
 * registerClient()
 * for each ship
 *   placePiece(ship, some_location, some_orientation)
 * while game not over
 *   isMyTurn()
 *   attack(some_location)
 * If you are interested in the moves being made by the opponent, you can also
 * call getOpponentsLastAttack() after each of their turns.
 * Once the game is over (ie. some player's ships have all been sunk), the
 * will throw GameOverExceptions on calls to functions involving the completed
 * game.  Check below for specific documentation of the
 * available calls your client may make to the server.

 * All references to specific ships are made by integer ID as specified
 * by this enumeration.  This is used on calls to placePiece().
 */

/* All references to specific ships are made by integer ID as specified
 * by this enumeration.  This is used on calls to placePiece().
 */
enum Ship {
  CARRIER = 1,
  BATTLESHIP = 2,
  DESTROYER = 3,
  SUBMARINE = 4,
  PATROL = 5
}

/* The attack() method returns an integer, the value of which is defined
 * in this enumeration.
 * HIT implies a hit on a ship in a location that hasn't been hit before,
 *   not resulting in sinking the ship.
 * Miss implies a total miss (including attacking a point outside the 10x10
 *  board, or an attack on a point that has already been hit.
 * A ship name (the id's correspond to the ids in the Ship enum) implies that
 * your attack sunk the indicated ship.
 * NOT_YOUR_TURN means you tried to make an attack out of turn.  Cut that out.
 */
enum AttackResult {
  SUNK_CARRIER = 1,
  SUNK_BATTLESHIP = 2,
  SUNK_DESTROYER = 3,
  SUNK_SUBMARINE = 4,
  SUNK_PATROL = 5,
  HIT = 6,
  MISS = 7,
  NOT_YOUR_TURN = 8
}

struct Coordinate {
  1:i32 row,
  2:i32 column
}

/* This exception is thrown if a call to getOpponentsLastAttack is
 * made before the opponent has made an attack.
 */
exception NoMovesMadeException {
}

/* Thrown if any calls to isMyTurn() or attack() are made after a victor has
 * been decided.
 */
exception GameOverException {
}

/* Thrown if any calls are made to gameplay functions before registering
 * or joining the game.
 */
 exception UnregisteredException {
 }

/* Thrown when a player attempts to join() using an email that is
 * already registered to a particular game.
 */
exception DuplicateEmailException {
}

service Battleship2 {

/* Registers a player in the game, returning the game ID they have been
 * assigned or -1 if game creation fails.  The server will report victory in
 * in terms of the email address provided.
 * After this call is made, the client can begin placing pieces on the board.
 * Once all pieces are placed, the second player to join will recieve
 * the first move of the game.
 */
  i32 registerClient(1:string email);

/* Joins an existing game using game's ID, as provided by register().  Returns
 * true if joining was successful, false if not due to some failure or the
 * game being full.
 */
   bool join(1:i32 gameID, 2:string email) throws (1:DuplicateEmailException dee);
   

/* Blocks until it is the calling player's turn, then returns true.
 * Returns false if an error occurs, which likely means the server has
 * died.
 */
  bool isMyTurn() throws (1:GameOverException goe, 2:UnregisteredException ue);


/* Places a piece on the board with its upper-leftmost point at
 * the coordinate provided and oriented according to the horizontal param.
 * A piece placed with horizontal set to true will entirely reside in a single
 * row, a piece placed with horizontal set to false will entirely reside
 * in a single column.
 * Returns true if the placement was successful - you must recieve a
 * "true" response from this function for each piece before the game
 * can begin.
 */
  bool placePiece(1:i32 piece, 2:Coordinate coord, 3:bool horizontal) throws (1:UnregisteredException ue);

/* Drops a bomb at the designated coordinate.  Results of this function
 * are described in the enum AttackResult.
 */
  AttackResult attack(1:Coordinate coord) throws (1: GameOverException goe, 2:UnregisteredException ue);

/* Returns a coordinate indicating the position attacked on the opponent's
 * last turn, or throws a NoMovesMadeException if your opponent has not
 * taken a turn yet.
 */
  Coordinate getOpponentsLastAttack() throws (1:NoMovesMadeException nmme, 2:UnregisteredException ue);
  
/* Call this when you've won the game to get credit.  It will return
 * a secret code to register your victory with us if you've won the
 * game, and will return "Nope!" otherwise.
 */
   string winGame() throws (1:UnregisteredException ue);

/* Adds a computer opponent to the game you are currently registered to.
 * Calls to this function in a full game will have no effect.  The computer
 * opponent is too smart to use random or sequential targeting, but is
 * not exactly a hunter-killer deathbot.
 */
   void spawnAI();
}
