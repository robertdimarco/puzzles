/* Simon Says
 * Puzzle Master (puzzles@facebook.com)
 *
 * This file describes the game interface for your Simon Says client to
 * interact with the Simon Says server. Compile this file using a Thrift
 * compiler to generate skeleton code or stubs in the language(s) of your
 * choice.
 *
 * The rules of Simon Says are simple:
 *
 * 1. Connecting to the Simon Says server automatically starts a game.
 *
 * 2. Call the registerClient(1:String email) function to start a game. Use an
 *    email you own to get credit for completing the puzzle. You'll need to
 *    send an email from the address you provide to complete the process.
 *
 * 3. Your client should call startTurn() to begin a turn, receiving a list of
 *    colors.
 *
 * 4. Your client must then call chooseColor() multiple times, once for each
 *    color in the returned list. This must be done in order, with the correct
 *    colors. If a false value is ever returned for chooseColor(), it means
 *    you have chosen the wrong color, and your client has reset the game,
 *    call startTurn() to continue again.
 *
 * 5. Once finished, call endTurn() and check the return value. False means the
 *    game is not yet over, and your client should call startTurn() again to
 *    get the next list of colors. If endTurn() ever returns true, it means
 *    you are ready to win! Invoke winGame() to win the game!
 *
 * 6. Calling the wrong color, calling endTurn() prematurely, or calling excess
 *    colors will all fail. The server will reset the color sequence back to
 *    length 1 and your client is required to call startTurn() again to start
 *    over.
 */

enum Color {
  RED    = 1,
  YELLOW = 2,
  GREEN  = 3,
  BLUE   = 4
}

service SimonSays {
  /* Register the client
   *
   * This starts a Simon Says game using your email address as the unique
   * identifier to identify your game (keeping your game state separate from
   * any other players on the same server). Returns true if successful, returns
   * false if there was an error (such as the same email address already
   * playing).
   */
  bool registerClient(1:string email);

  /* Start your turn
   *
   * Returns a list of colors that your client must then choose appropriately
   * using the chooseColor() API (see below). Each time you successfully
   * complete a turn, the list returned will have one additional color to call
   * until you win the game.
   */
  list<Color> startTurn();

  /* Choose a color
   *
   * Sends one color choice to the server. This must be done in order of the
   * list of colors given to your client via the startTurn() API. The function
   * returns true if you have chosen correctly, and false if you have chosen
   * incorrectly.
   */
  bool chooseColor(1:Color colorChosen);

  /* End your turn
   *
   * Ends your turn; if the function returns false, it means the game has not
   * yet been won and your client should call startTurn() again. If the
   * function returns true, your client should call winGame() to register
   * your win.
   */
  bool endTurn();

  /* Win the game and register your score
   *
   * When you have won the game, call this function to register your win and
   * close the connection to the server.
   *
   * IMPORTANT: This function returns a string that should be used as the
   * subject line of an email you send to puzzles@facebook.com. In order to be
   * fully credited with solving the puzzle, you must send the email from the
   * address you called registerClient() with, and us this EXACT string as the
   * subject line. The next time the grading robot processes emails, you
   * will be given credit, and the Facebook Puzzles application will display
   * your successful solve.
   */
  string winGame();
}
