## Dinosaur Island

  * Keyword:     `dinoisland`
  * Difficulty:  `Buffet`

Dinosaur Island is meant to be an open-ended game/puzzle where authors can write their own dinosaur logic and attempt to thrive and/or dominate on the eponymous island. Dinosaur Island features two types of dinosaurs, herbivores and carnivores. You start the game by implementing a dinosaur client using the Thrift open-source RPC framework. Your client must provide an email address which is used to generate a unique identifier for your newly created species of dinosaur. As the game progresses, your dinosaur may be able to lay an egg, allowing you to connect an additional client to the server, and take control of newly created instance of your species.

Your dinosaur starts off with a limited calorie pool and must spend them wisely, moving around the island, detecting danger, growing in size, and eating things (either plants or other dinosaurs). Hopefully it will gain enough calories that it can begin to lay eggs, increasing its numbers and beginning its ascent to evolutionary dominance.

### Game Rules

The service specification for this puzzle, (dinoisland.thrift), can be compiled via the Thrift compiler into client and server skeleton code, classes, and/or stubs depending on the target language of choice.

Your client begins the game by connecting to the Dinosaur Island Thrift server (see below) and invoking the **registerClient(1:string email, 2:string highScoreName, 3:EntityType type)** API first. This function takes the place of the simpler **registerClient(1:string email)** function described on the Public Thrift Puzzle Server. Once that has been done successfully, your client will given an integer ID of the first egg put into the world for your newly created dinosaur species. This first egg marks the beginning of your species; your species has a fixed time limit where it may thrive and grow, accumulating points.

At this point, your client may call the **hatch(1:i64 eggID)** API and take control of the newly hatched dinosaur. This function returns a DinosaurState struct which contains information about your new dinosaur, such as its size, calorie pool, and the costs for the various actions the dinosaur can perform.

All dinosaur action APIs (see the dinoisland.thrift file for more details) consume calories, and take time to execute. The results of an action API will not return to your client until the action executes. If your dinosaur attempts to perform an action it does not have the calories for, it will starve to death. In addition, dinosaurs have individual lifespans, which are shorter and independent of the species time limit. Any dinosaur which exceeds its lifespan will die. Lifespans are not known to the dinosaur client.

One action API allows your dinosaur to lay another egg, allowing another client to connect to the Dinosaur Island server and begin controlling a new instance of your dinosaur. So long as one instance of your dinosaur is alive, your species is considered non-extinct. Should the species go extinct (i.e. all instances of your dinosaur are dead), either through predation, lack of food, or the extinction event at the end of the species lifetime, the last client connection will receive a special **GameOverException**. This exception takes the place of the **winGame()** API indicated by the directions on the Public Thrift Puzzle Server and is identical to the more common **YouAreDeadException**, except it contains your integer score and if your score is high enough, the hash string you can use to receive full credit for your submission (see full submission directions below).

Dinosaur Island features arcade style scoring, where your species (i.e. all clients under your control, representing all instances of your dinosaur species) has a fixed time limit to accumulate points by performing actions appropriate to its species type. At the end of that time limit, all instances of your species will die (i.e. an extinction event). Regardless of how this happens, either through species time limit being reached, or your dinosaur goes extinct from predation or lack of food, your species will be given a score. If your species scored above a certain threshold (even if it's not in the top 10 scores), you will be given a hash string. See the submission directions below for full details on what to do with this hash string.

### Useful Facts About Dinosaur Island

There are three types of life forms on dinosaur island: plants, herbivores, and carnivores. Each type gains calories and staves off starvation in a different way. Plants simply gain calories from sunlight, herbivores gain calories by moving into (and thus eating) plants, and carnivores gain calories by moving into (and thus eating) herbivores.

All actions (including looking) take calories, your client must strategize its calorie use to ensure it can find food before it starves to death.

Carnivores have a slight speed advantage over herbivores in that their turns take slightly less time to execute; however, both carnivores and herbivores have individual lifespans that ensure they get roughly the same number of turns.

When eating something (either plants, herbivore, or other carnivores), the bigger the prey, the more calories gained. In addition, a fraction of the prey's calorie pool is given to the victor as a bonus.

Growing is an important part of survival and alters the behavior of the other actions. Growing allows your dinosaur to see slightly further, but also makes your dinosaur able to be seen further away. One of the most important aspects of your dinosaur's size is that it allows it to win in battles with other dinosaurs, a must have for carnivores.

When two dinosaurs fight, their sizes are compared to determine the odds of either one winning. For example, if a size 3 herbivore fights a size 5 herbivore, the smaller dinosaur has a 3/(3+5) chance of winning, and the larger has a 5/(3+5) chance of winning. Carnivores have a significant increase in effective size when fighting other herbivores.

Plants are not evenly distributed about the island, there will be regions of the randomly generated island that have denser foiliage to feast upon. These regions will not change so long as that island exists, but a server restart will cause an entirely new island to be generated.

Be on the look out for anything strange on the island. There should be some very rare surprises your dinosaurs may encounter, make sure to check all data returned to your client!

### Special Submission Directions

If you wish to receive credit for solving the puzzle, make sure your client calls **registerClient(1:string email, 2:string highScoreName, 3:EntityType type)** using an email address that you control and can send email from.

To solve the puzzle, build and run your client on your own host and have it connect to our Public Thrift Puzzle Server. This server has further instructions on how to use it as both a testing and evaluation tool. One change to note is that this puzzle does not have a **winGame()** API to call; instead you receive your hash code from the final GameOverException thrown when the last instance of your species dies.

You are free to put any desired debugging output in your client; the server evaluates correctness only based upon your client's interactions with the remote server, not its local output. Your client may be written in any accepted language that works with the provided Thrift library (see link below or on right side of page).

### Resources

You can get the version of Thrift used by the Puzzle Master by visiting the Thrift web site and downloading the appropriate archived release.

The Dinosaur Island Thrift service file can be downloaded from Facebook's site.

The Public Thrift Puzzle Server is available for your use in developing and evaluating your client.

Originally published at [http://www.facebook.com/careers/puzzles.php?puzzle_id=19](http://www.facebook.com/careers/puzzles.php?puzzle_id=19).
