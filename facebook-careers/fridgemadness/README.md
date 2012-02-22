#Refrigerator Madness#

* Difficulty:  Meal
* Keyword:     fridgemadness
* Completed:   2009-07-05 [Python]

Facebook is always looking for ways to make its engineers happier and work faster. The free food and drinks at Facebook have revealed a surprising empirical fact: the drinks an engineer prefers determines who they are best at working with. In an attempt to capitalize on this fact, Facebook is implementing extreme programming in its engineers as a way to maximize productivity.
 
As a growing company, Facebook has many engineers and determining the assignment can no longer be done by hand. By analyzing a list of available drinks in the refrigerator, and a table of employee drink preferences, you wish to provide the company with the arrangement that benefits everyone the most with happy and productive engineers. Being an engineer of some repute, you realize this is best done with a clever program.

**Input specifications**

The input file consists of a multi-line file that is divided into three sections. The first line of the file contains two positive integers separated by a single space character. These two numbers are the number of engineers in the file, and the number of drinks defined by the file (in that order). The number of engineers in the company will always be even.
 
Following that line are a number of lines defining the drinks available at Facebook. These drink lines start with a unique integer drink id, followed by a variable amount of white space (spaces and/or tabs), followed by string representing the human readable name of the drink. All drink lines end with a single new line. Drink ids start at 0 and increment by 1 for each new drink.
 
Following the drink definitions, are a number of lines declaring engineers and their drink preferences. Each engineer line starts with a unique engineer id, followed by a variable amount of white space (spaces and/or tabs), followed by a comma separated list of drink ids. All engineer lines end with a single new line. Engineer ids start at 0 and increment by 1 for each new engineer.
 
Every engineer's drink list will contain the N most preferred drinks for that engineer where N is less than or equal to the total number of drinks defined by the input file. The drink lists are ordered, with the first drink listed being the most preferred by the engineer, and so on.

Example input file:
<pre>
6 3
0       Black Coffee
1       Green Tea
2       Gatorade
0       0,2,1
1       1,2,0
2       2,1,0
3       1,0,2
4       2,0,1
5       0,1,2
</pre>

You are guaranteed that your program will run against well-formed input files, and that the number of drink definitions, and engineer definitions, will match the summary provided in the first line of the input file. 

**Output specifications**

To maximize the effectiveness, Facebook wants the engineers from its upper 50th percentile to only be assigned with engineers from its lower 50th percentile. To assist in this, Facebook has sorted its employee ids so that employee 0 is the most effective engineer, and progressing down to the last employee who is the least effective engineer.
 
An engineer's preference to work with another engineer can be calculated by comparing the drink preferences of each engineer. An engineer prefers to work with one engineer over another if the preference score is higher. For example, if engineer **A** prefers engineer **B** with a preference score of 100 and engineer **C** with a preference score of 200, then engineer **A** prefers to work with **C** compared to engineer **B**. Preferences are one-directional, and just because engineer **A** prefers engineer **C** does not mean that **C** shares the exact same preference to work with **A**.
 
To calculate how much an engineer **A** prefers to work with another engineer **B**, calculate a value for every drink in **A**'s list and sum the total.

  * If there are N drinks in an **A**'s drink list, the first (and most) preferred drink has a base value of N points, the second drink is worth N-1 points, and so on until the last drink, which has a base value of 1 point.
  * If both **A** and **B** have the same drink in their list, and *it is in the same position in both lists*, square the base value for this drink because these two engineers have so much more in common.
  * Otherwise, if **A** likes a drink more (e.g. the drink appears sooner in **A**'s list or does not appear at all in **B**'s list), only use the base value of the drink, because at least **A** may be able to convince B of the merits of the drink in question.
  * If **B** happens to like the drink more than **A** (e.g. the drink appears sooner in **B**'s list), ignore the base value and add nothing to the sum. In this case, **A** is distrustful and dubious of **B**'s taste in liquid refreshment.

If this is done for every drink in **A**'s list, the sum is the total preference level which with **A** prefers to work with engineer **B**. Ties in preference levels are settled with engineers always preferring less effective engineers over more effective engineers. This is because good engineers enjoy helping other engineers, and lesser engineers enjoy hanging out with engineers that are more like them.
 
Your program must pair up every engineer from the upper 50th percentile with an engineer from the lower 50th percentile such that there are no two engineers in both sets that would prefer each other over their current assignment. To keep the upper 50th percentile engineers happy, they must be assigned to the highest possible preferred lower 50th percentile engineer while still maintaining the above condition. Your output must contain newline-separated pairs of engineer ids, where the contents of each pair are in ascending order and separated by a single space. The pairs must appear in the output in ascending order of the first id they contain.

Example output (newline at end of every file):

<pre>
0 5
1 3
2 4
</pre>

Originally published at http://www.facebook.com/careers/puzzles.php?puzzle_id=10.