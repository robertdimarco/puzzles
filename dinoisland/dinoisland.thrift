/**
 * Dinosaur Island
 *
 * Dinosaur Island is meant to be an open-ended game/puzzle where authors can
 * write their own dinosaur logic and attempt to thrive and/or dominate on the
 * eponymous island. Dinosaur Island features two types of dinosaurs,
 * herbivores and carnivores. You start the game by implementing a dinosaur
 * client using the Thrift open-source RPC framework. Your client must provide
 * an email address which is used to generate a unique identifier for your
 * newly created species of dinosaur. As the game progresses, your dinosaur
 * may be able to lay an egg, allowing you to connect an additional client to
 * the server, and take control of newly created instance of your species.
 *
 * Your dinosaur starts off with a limited calorie pool and must spend them
 * wisely, moving around the island, detecting danger, growing in size, and
 * eating things (either plants or other dinosaurs).
 *
 * Dinosaur Island features arcade style scoring, where your species (i.e. all
 * clients under your control, representing all instances of your dinosaur
 * species) has a fixed time limit to accumulate points by performing actions
 * appropriate to its species type. At the end of that time limit, all
 * instances of your species will die (i.e. an extinction event). Regardless of
 * how this happens, either through species time limit being reached, or your
 * dinosaur goes extinct from predation or lack of food, your species will be
 * given a score. If your species scored above a certain threshold
 * (even if it's not in the top 10 scores), you will be given a hash string.
 * Send an email to puzzles@facebook.com, attach your code, and use that string
 * code as the subject line in order to receive credit for solving Dinosaur
 * Island.
 *
 */

/**
 * Recommended Java namespace
 */
namespace java com.facebook.puzzles.dinoisland.thrift


/**
 * Entity types
 *
 * Entities are things that your dinosaur can see and possibly interact with.
 * Your dinosaur is able to interact with Plants, Herbivore dinosaurs, and
 * Carnivore dinosaurs. Your dinosaur can see impassable terrain, but cannot
 * interact with it.
 */
enum EntityType {
    PLANT = 0,
    HERBIVORE = 1,
    CARNIVORE = 2,
    IMPASSABLE = 3
}

/**
 * Directions
 *
 * These enums define directions used on the grid based map of Dinosaur Island.
 * In order for your dinosaur to lay an egg, look, or move, it must supply one
 * of these enums.
 */
enum Direction {
    N  = 0,
    NE = 1,
    E  = 2,
    SE = 3,
    S  = 4,
    SW = 5,
    W  = 6,
    NW = 7
}

/**
 * Coordinate struct
 *
 * This structure is intended to explicitly define how the coordinate system of
 * Dinosaur Island is set up.
 */
struct Coordinate {
    1:i32 row,
    2:i32 column
}

/**
 * Dinosaur State
 *
 * This structure contains all pertinent data regarding your dinosaur instance,
 * including its available calories to spend, its current size, and how many
 * calories it will cost to lay an egg, grow one size, look in a direction,
 * and move in a direction.
 */
struct DinosaurState {
    1:i32 calories,
    2:i32 size,
    3:i32 eggCost,
    4:i32 growCost,
    5:i32 lookCost,
    6:i32 moveCost
}

/**
 * Sighting struct
 *
 * This structure represents your dinosaur sighting something interesting, be
 * it plants to eat, dinosaurs to eat, or fearsome carnivores to avoid. Lastly,
 * this struct is also used to tell your dinosaur when it sees impassable
 * terrain.
 *
 * Each sighting includes coordinates of the sighting (coordinates are always
 * relative to your own dinosaur's position), what kind of entity was spotted,
 * as well as the species string and what size the entity is. In the case of
 * impassable terrain, species will be blank and size will be 0.
 */
struct Sighting {
    1:Coordinate coordinate,
    2:EntityType type,
    3:string species,
    4:i32 size
}

/**
 * Register Client results
 *
 * This structure is returned to your client after it calls the registerClient
 * function. It includes a string message welcoming you to Dinosaur Island,
 * as well as your randomly generated species name. It is important to note
 * that this randomly generated species name is how other clients will see your
 * dinosaur, and this is different from the highScoreName you chose originally
 * if your dinosaur makes it into the evolutionary hall of fame. Lastly, it
 * includes an integer egg ID which your client can then use to take over
 * control of the very first instance of your dinosaur species.
 */
struct RegisterClientResults {
    1:string message,
    2:string species,
    3:i64 eggID
}

/**
 * Look action results
 *
 * This structure is returned to your client after it calls the look function.
 * It includes a string message (useful for debugging), a boolean indicating
 * action success, as well as the new state for your dinosaur, and a list of
 * Sighting structs (see above).
 */
struct LookResults {
    1:string message,
    2:bool succeeded,
    3:DinosaurState myState,
    4:list<Sighting> thingsSeen
}

/**
 * Grow action results
 *
 * This structure is returned to your client after it calls the grow function.
 * It includes a string message (useful for debugging), a boolean indicating
 * action success, as well as the new state for your dinosaur.
 */
struct GrowResults {
    1:string message,
    2:bool succeeded,
    3:DinosaurState myState
}

/**
 * Move action results
 *
 * This structure is returned to your client after it calls the move function.
 * It includes a string message (useful for debugging), a boolean indicating
 * action success, as well as the new state for your dinosaur. The most common
 * reason for the boolean succeeded returning False is your dinosaur attempted
 * to move into impassable terrain.
 */
struct MoveResults {
    1:string message,
    2:bool succeeded,
    3:DinosaurState myState
}

/**
 * Lay an Egg action results
 *
 * This structure is returned to your client after it calls the egg function.
 * It includes a string message (useful for debugging), a boolean indicating
 * action success, the new state of your dinosaur, and the integer egg ID of
 * your newly created egg if the action was successful. If the egg function
 * fails, the egg ID will be 0.
 */
struct EggResults {
    1:string message,
    2:bool succeeded,
    3:DinosaurState parentDinoState,
    4:i64 eggID
}

/**
 * Bad egg exception
 *
 * This exception is thrown if a client attempts to take control of a newly
 * hatched dinosaur egg but fails. The string contains a description of the
 * failure, which may include incorrect egg ID or trying to take over an egg
 * of a different species (i.e. a dinosaur that does not belong to your email
 * address).
 */
exception BadEggException {
    1:string description
}

/**
 * You are dead exception
 *
 * This exception is thrown if a client attempts to call an action function,
 * but the dinosaur controlled turns out to be already dead. This can happen if
 * the dinosaur your client controls is eaten by a predator, or has exceeded
 * its real time lifespan. The string will contain useful information about the
 * cause of death for your dinosaur.
 */
exception YouAreDeadException {
    1:string description
}

/**
 * Already registered exception
 *
 * This exception is thrown if a client that is already controlling a dinosaur
 * attempts to call registerClient().
 */
exception AlreadyRegisteredException {
    1:string description
}

/**
 * Game over exception
 *
 * This exception is thrown if a client attempts to call an action function,
 * but the species has already died out, either due to having all of the
 * dinosaurs die of natural causes or due to the species time limit being
 * reached. The wonGame field will be true if your species scored high enough
 * to win the game. The score field will provide your total score. The message
 * field will contain instructions for how to get credit for winning the game
 * if your species scored high enough to win, and will also contain the reason
 * your species went extinct. The highScoreTable field will contain the top 10
 * high scores since the server was started. Note that the highScoreTable
 * does not list dinosaur species names, instead it users the chosen
 * highScoreNames provided by each puzzler's registerClient() call to register
 * their species.
 */
exception GameOverException {
    1:bool wonGame,
    2:i32 score
    3:string message,
    4:string highScoreTable,
}


/**
 * Dinosaur Island service
 *
 * This is the API used by clients to interact with the Dinosaur Island
 * server. Functions have two attributes, whether they are actual game
 * functions which cost calories to use, and whether they take up a dinosaur's
 * turn, causing that connection thread to sleep until the next game turn.
 *
 * All dinosaurs have two resources, their size and their available calories.
 * In addition, all dinosaurs have an individual lifespan before that
 * particular instance of the dinosaur will die of old age. In order for your
 * species to survive and score points, it must eventually lay eggs.
 *
 * Should your dinosaur not have enough calories to perform a given action, it
 * will die of starvation. If your dinosaur simply idles, it will eventually
 * die of old age.
 *
 * Eventually, your species time limit will expire, and all instances of your
 * dinosaur species will die off at the same time. One of your client(s) will
 * call an action API and the GameOverException will be returned, informing you
 * that your species died off, what your high score is, and whether your
 * species scored high enough to "solve" the puzzle, and what the top 10 scores
 * are for this island.
 */
service Dinosaur {

  /**
   * Register Client
   *
   * Costs calories: No
   * Uses up turn: No
   *
   * This function must be the very first thing called by the first client that
   * connects to the Dinosaur Island server. This function is slightly
   * different from the instructions on the Public Thrift Server, but serves an
   * identical purpose. In addition to the required email, it also requires
   * a string of what to display in the high score table should your species
   * rank in the top 10, as well as a chosen dinosaur type (herbivore or
   * carnivore).
   */
  RegisterClientResults registerClient(string email, string highScoreName, EntityType type)
    throws (AlreadyRegisteredException alreadyRegistered);

  /**
   * Hatch an egg (take over a previously laid egg)
   *
   * Costs calories: No
   * Uses up turn: No
   *
   * Allows a client connection to take control of an egg, identified by the
   * egg ID parameter. Returns the DinosaurState of the newly controlled
   * dinosaur if successful, throws an exception otherwise.
   */
  DinosaurState hatch(i64 eggID)
    throws (BadEggException badEgg, YouAreDeadException youAreDead,
            GameOverException gameOver);

  /**
   * Lay an egg
   *
   * Costs calories: Yes
   * Uses up turn: Yes
   *
   * Lays an egg in the specified direction, in addition to giving the new
   * egg some calories to help it survive. This function costs calories to use
   * and your dinosaur is responsible for ensuring it has enough to call this
   * function without starving to death. The cost of this function is equal to
   * the eggCost value (found in any DinosaurState struct returned) plus the
   * calories given to the egg. The newly hatched dinosaur will not gain all
   * of these calories, up to 20% of them will be lost in the transfer.
   *
   * This function returns an EggResults on success that contains useful
   * information, such as the current state of the egg laying dinosaur, the
   * egg ID of the newly laid egg, among other info. Another Dinosaur Island
   * client can then connect and start playing after calling the hatch func
   * with the egg ID. This function throws an exception otherwise.
   */
  EggResults egg(Direction direction, i32 calories_given)
    throws (YouAreDeadException youAreDead, GameOverException gameOver);

  /**
   * Look (in a direction)
   *
   * Costs calories: Yes
   * Uses up turn: Yes
   *
   * If successful, the dinosaur will use up a number of calories (found in any
   * DinosaurState struct returned) and return an list of Sighting structs
   * representing things the dinosaur saw in that direction. Sight is treated
   * as a cone radiating out from the dinosaur in question.
   *
   * How far a dinosaur can see is dependent on how big the actual dinosaur
   * is, and the sizes of the objects in the cone.
   *
   * Two examples of cone shapes are given below:
   *
   *              +                  +
   *             ++                  ++
   *            +++                  +++
   *           D+++                  ++++
   *            +++                  +++++
   *             ++                  ++++++
   *              +                  D++++++
   */
  LookResults look(Direction direction)
    throws (YouAreDeadException youAreDead, GameOverException gameOver);

  /**
   * Grow
   *
   * Costs calories: Yes
   * Uses up turn: Yes
   *
   * If successful, the dinosaur will increments its size by one. All dinosaurs
   * start with a size of one. Size is used in determining how far a dinosaur
   * can see (or how easily your dinosaur can be seen), as well as how likely
   * a dinosaur is in winning a fight with another dinosaur. Lastly, if your
   * dinosaur is eaten, it will be worth more calories the bigger it is.
   *
   * This function returns a GrowResults struct upon success and throws an
   * exception otherwise.
   */
  GrowResults grow()
    throws (YouAreDeadException youAreDead, GameOverException gameOver);

  /**
   * Move
   *
   * Costs calories: Yes
   * Uses up turn: Yes
   *
   * Moves the dinosaur in the direction specified; if an entity exists in the
   * target square, the dinosaur will fight with that entity.
   *
   * Plants always lose battles, no matter what moves into their square. If the
   * attacker is an herbivore, it will gain calories based upon the plant's
   * size. Carnivores merely destroy the plant with no calories gained.
   *
   * If one dinosaur moves into another, they will fight. Carnivores gain a
   * significant boost to their odds of victory when fighting herbivores. If
   * a carnivore wins over an herbivore, it will gain calories based upon the
   * size of the herbivore, and how many calories the herbivore had at time of
   * death.
   *
   * If your dinosaur attempts to move into impassable terrain, the
   * MoveResults struct will contain a success boolean of false, indicating
   * the dinosaur did not actually change positions.
   */
  MoveResults move(Direction direction)
    throws (YouAreDeadException youAreDead, GameOverException gameOver);
}
