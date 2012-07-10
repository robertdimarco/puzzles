## We Are The Swarm

  * Keyword:     `swarm`
  * Difficulty:  `Meal`

Everyone you know anticipates the release of StarCraft 2 with vast eagerness. To help get back in the saddle of the greatest RTS game ever, you decide to use programming to help practice your decision making.

You are the Zerg Queen in command of the 654195331th legion of Zerg forces, the only side worth playing in StarCraft. The wise Overmind has given you the important task of cleaning up some remote planets for mineral mining operations. Apparently, some pesky Terran forces have decided to set up base defenses in these locations, prior to your arrival. With your limited forces, you must determine which Terran bases to attack. Your Zerg forces on each planet have free movement over that one planet, and may split up to attack any number of Terran bases on that planet. However, your Zerg ground forces have not yet evolved space flight and thus cannot travel from planet to planet to assist each other.

The Overmind has provided you with some valuable information about each base. For each Terran base, you are given the amount of minerals, and the strength of the Terran forces at that base. Terran communication channels have been disrupted so you do not have to worry about forces from one base aiding another. You know from past experiences that your odds of victory over a particular Terran base are equal to:

<pre>
P(z,s) = e^(-63s+10)/(e^(-63s+10)+e^(-21z)) 
</pre>

Where **z** is the strength of the Zerg forces, s is the strength of the Terran base, **P(z,s)** is the probability from (0-1) that the base will be taken over, and **e** is Euler's number. The expected amount of minerals gained from an attack on a Terran base is therefore equal to **round(P(z,s) * m)** where **m** is the amount of minerals at the Terran base. Use these probabilities to attack Terran forces that will likely result in the maximum amount of minerals available for mining. Mineral gains are considered significant enough to commit Zerg units if the expected gain is 1 or more minerals. Any extra forces should not be allocated to attack a base so that the Overmind may use them for other nefarious purposes.

Write a program that takes a single argument on the command line. This argument must be a file name, which contains the input data. The program should output to standard out the deployment orders of your Zerg horde. Your program must be robust and fast enough to be able to handle large inputs (within the below bounds) within a matter of minutes.

### Input specifications

The input file starts out with a single line with an integer number of planets (**P**). Subsequent lines represent data blocks on each planet. The first line of a data block is two integers separated by single space character. The first integer is the number of Terran bases on the planet (**T**), followed by the number of Zerg forces available on the planet (**Z**). Following that, each subsequent line in the data block contains two integers separated by a single space character. These numbers are the strength of the Terran forces at the base (**s**) and the minerals at the base (**m**). There will be one subsequent line per base on the planet. All values in the input are integers.

The following bounds are observed for **P**, **T**, **Z**, **s**, and **m**:
* **1 <= P <= 1000**
* **1 <= T <= 1000**
* **1 <= Z <= 1000**
* **1 <= s <= 100000**
* **1 <= m <= 5000**

Example input file:
<pre>
2
5 1000
1143 234
2349 2
234 455
39843 323
83834 4284
2 23
7 2000
40 5
</pre>

### Output specifications

For each planet (in order of appearance in the input file), output two lines of text. The first line of text should be the total amount of Zerg forces utilized on the planet, followed by the probable number of minerals captured, separated by a single space character.

The second line of text should consist of pairs of numbers separated by single space characters. The first number in a pair is the index of the base attacked (indexes start at zero for each planet, and are in order of appearance in the input file), followed by the number of Zerg forces used, separated by a single space. These pairs should be ordered by base index, in ascending order. There should be no trailing space after the last number of any line; but there must be a new line at the end of every line, including the last line.

Example output:

<pre>
702 455
2 702
21 2000
0 21
</pre>

Originally published at [http://www.facebook.com/careers/puzzles.php?puzzle_id=5](http://www.facebook.com/careers/puzzles.php?puzzle_id=5).
