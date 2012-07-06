## Ticket Lottery

### Problem ID: lottery
### Difficulty: Funk

You and your friends are in New York and are planning to go see a Broadway musical. Unfortunately, New York being New York, the tickets are just a tiny bit expensive. But one of the shows has a ticket lottery each night where impecunious people such as you have a chance to win the right to buy slightly less expensive tickets to good seats. The lottery operates as follows. First, everyone interested enters the lottery. Then, **n** lucky winners are drawn, and each of these is offered to buy up to **t** tickets. Given the number of people **p** in your group (all of which entered the lottery) and the total number of people **m** that entered the lottery, what is the probability that you will be able to get tickets for your entire group? Assume that the **n** lucky winners are chosen uniformly at random from the **m** people that entered the lottery, and that each person can win at most once.

### Input

The input consists of a single line containing four integers:

  * 1 ≤ **m** ≤ 1000: the total number of people who entered the lottery.
  * 1 ≤ **n** ≤ **m**: the total number of winners drawn.
  * 1 ≤ **t** ≤ 100: the number of tickets each winner is allowed to buy.
  * 1 ≤ **p** ≤ **m**: the number of people in your group.

### Output

Output a single line containing the probability that your entire group can get tickets to the show. This probability should be given with an absolute error of at most 10<sup>−9</sup>.

#### Sample input 1
<pre>
100 10 2 1
</pre>

#### Sample output 1
<pre>
0.1
</pre>

#### Sample input 2
<pre>
100 10 2 2
</pre>

#### Sample output 2.
<pre>
0.1909090909
</pre>

#### Sample input 3
<pre>
10 10 5 1
</pre>

#### Sample output 3
<pre>
1.0000000000
</pre>

Originally posted at [http://www.spotify.com/us/jobs/tech/ticket-lottery/](http://www.spotify.com/us/jobs/tech/ticket-lottery/).
