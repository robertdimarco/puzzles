## Battleship

  * Keyword:     `battleship`
  * Difficulty:  `Meal`

Prepare for war! Your nostalgia for games from your childhood has finally boiled over into an all-out lust for nautical combat, and the only cure is a good, old-fashioned game of Battleship. Well, sort of old-fashioned; instead of sitting opposite a friend shouting letter-number pairs at each other, you've decided to write a computer program to play the game for you. Taking advantage of Thrift, you will be able to write your program in any of a number of popular languages and be able to challenge your friends leagues - nay, *kiloleagues* - away at the speed of light.

### Game Rules

Each player is given a 10x10 unit area in which to place 5 ships of different size: an aircraft carrier (length 5), a battleship (length 4), a submarine and a destroyer (both length 3), and a patrol boat (length 2). Vital to the game is that players keep the placements they have chosen secret from the other player. Players place their pieces anywhere on the board such that the endpoints of each piece reside at integer coordinates on the board, and each piece resides either completely within a single row or within a single column. Row and column indices are zero-based, so all legal values for each are integers in [0,9]. Ships owned by a single player are not allowed to overlap and ships must be contained entirely within the legal boundaries of the board.

Once all pieces are placed, players take turns "bombing" each other's ships by specifying a coordinate they would like to attack. If any of the ships owned by the defending player occupies the position under attack, and the same position has not been attacked before, it is considered a hit. The player being bombed must truthfully indicate the result of the attack, replying "hit" if the attack hit a ship but did not sink it, "miss" if the attack didn't hit anything, or stating the phrase "you sunk my &lt;shipname&gt;", with the name of the ship that was sunk. A ship sinks when every point it occupies has been hit, so for example the aircraft carrier requires five hits to sink while the patrol boat requires only two. The game continues until one player has sunken all their opponent's ships; that player is then the winner.

For your Thrift-based implementation of Battleship, you will be responsible to implement a client to play the game as described in this specification. Your client must be able to, given a host name and port number, be able to establish a connection with a Battleship server, register as a player, then defeat your opponent in a reasonable number of moves (naively bombing every point in sequence won't be good enough). All the interactions required to play the game are described in the client specification.

### Special Submission Directions

If you wish to receive credit for solving the puzzle, make sure your client calls **registerClient(1:string email)** using an email address that you control and can send email from.

To solve the puzzle, build and run your client on your own host and have it connect to our Public Thrift Puzzle Server. This server has further instructions on how to use it as both a testing and evaluation tool. You are free to put any desired debugging output in your client; the server evaluates correctness only based upon your client's interactions with the remote server, not its local output.

Your client may be written in any accepted language that works with the provided Thrift library (see link below or on right side of page).

### Resources

You can get the version of Thrift used by the Puzzle Master by visiting the Thrift web site and downloading the appropriate archived release.

The Battleship Thrift service file can be downloaded from Facebook's site.

The Public Thrift Test Server is available for your use in developing your client.

Originally published at [http://www.facebook.com/careers/puzzles.php?puzzle_id=14](http://www.facebook.com/careers/puzzles.php?puzzle_id=14).
