#Simon Says#

* Difficulty:  Snack
* Keyword:     simonsays
* Completed:   2009-06-27 [Java]

Simon Says is intended to be a relatively simple introduction to use the Thrift remote-procedure call framework to easily write server/client software. This eponymous puzzle follows the rules for Simon (the electronic toy) by Milton Bradley (now Hasbro). Thrift's purpose is to allow authors to create very simple files called service specifications, that can be compiled via the Thrift compiler into actual code in almost any programming language. Thrift thus removes the need for developers to write their own networking code, including transport and error checking; all the developer needs to write is the actual functionality, as Thrift takes care of all the networking code for you.

**Game Rules**

The service specification for this puzzle, (simonsays.thrift), can be compiled via the Thrift compiler into client and server skeleton code, classes, and/or stubs depending on the target language of choice.

Your client begins the game by connecting to a Simon Says Thrift server and invoking the **registerClient(1:string email)** API first. Once that has been done successfully, your client will iterate through a series of turns until the game is won.

The client must call the **startTurn()** API to receive a list of colors from the server. The client must then play back these colors in the correct order to the server using the **chooseColor(1:color colorChosen)** API. Once done, the client must then call **endTurn()**.

If **endTurn()** returns false, the game has not yet been won. The client should repeat the process of calling **startTurn(), chooseColor(1:color colorChosen)** several times, and then **endTurn()**. Once **endTurn()** returns true, the client is in a win-ready state, and may win the game by calling the **winGame()** API. Make sure you save the string returned by the **winGame()** call, as you will be required to send an email to the puzzle robot using this string as the subject line. Also make sure you send the email from the same address used with your **registerClient(1:string email)** call. Once the client has received the string from **winGame()**, the client may then safely terminate the connection and shut down. You do not have to send an email to the puzzle robot before shutting down your client.

If the client chooses the wrong color, calls an extra color when it should have called **endTurn()**, or calls **endTurn()** prematurely, the server will restart its state. The server resets the color sequence back to the starting length of one and will return this new color sequence at the next **startTurn()** call. If your client detects this error, it should stop and immediately start over by calling **startTurn()**.

**Special Submission Directions**

If you wish to receive credit for solving the puzzle, make sure your client calls **registerClient(1:string email)** using an email address that you control and can send email from.

To solve the puzzle, build and run your client on your own host and have it connect to our Public Thrift Puzzle Server. This server has further instructions on how to use it as both a testing and evaluation tool. You are free to put any desired debugging output in your client; the server evaluates correctness only based upon your client's interactions with the remote server, not its local output.

Your client may be written in any accepted language that works with the provided Thrift library (see link below or on right side of page).

**Resources**

You can get the version of Thrift used by the Puzzle Master by visiting the Facebook Developers web site and downloading the current archived release.

The Simon Says Thrift service file can be downloaded from Facebook's site.

The Public Thrift Puzzle Server is available for your use in developing and evaluating your client.

Originally published at http://www.facebook.com/careers/puzzles.php?puzzle_id=13.