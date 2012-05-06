## Safety in Numbers

### Problem

There are **N** contestants in a reality TV show. Each contestant is assigned a point value by the judges and receives votes from the audience. The point value given by the judges and the audience's votes are combined to form a *final* score for the contestant, in the following way:

Let X be the sum of the judge-assigned point values of all contestants. Suppose contestant i got Ji points from the judges, and received a fraction Yi (between 0 and 1, inclusive) of the audience's votes (Yi might be, for example, 0.3). Then, the final score for contestant i is J<sub>i</sub>+X*Y<sub>i</sub>. Note that a participant from the audience can vote for at most one contestant, so the sum of Y<sub>i</sub>s is at most 1.

The contestant with the lowest score is eliminated.

Given the points contestants got from judges, your job is to find out, for each contestant, the minimum percentage of audience votes he/she must receive in order for him/her to be guaranteed **not to be eliminated**, no matter how the rest of the audience's votes are distributed.

If the lowest score is shared by multiple contestants, no contestants will be eliminated.

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow, one per line. Each line starts with an integer **N**, the number of contestants, followed by a space, followed by **N** integers **s**<sub>0</sub>, **s**<sub>1</sub>, ..., **s**<sub>N-1</sub>, separated by single spaces. The integer s<sub>i</sub> is the point value assigned to contestant i by the judges.

### Output

For each test case, output one line containing "Case #x: " followed by **N** real numbers: **m**<sub>i</sub>s. The value x is the case number (starting from 1). The value **m**<sub>i</sub> is the smallest percentage of audience votes required for contestant i to definitely avoid elimination.

Answers within an absolute or relative error of 10<sup>-5</sup> of the correct answer will be accepted.

### Limits

0 ≤ **s**<sub>i</sub> ≤ 100.
**s**<sub>i</sub> > 0 for some i. This means at least one contestant will have a point value greater than 0.

### Small dataset

1 ≤ **T** ≤ 20.
2 ≤ **N** ≤ 10.

### Large dataset

1 ≤ **T** ≤ 50.
2 ≤ **N** ≤ 200.

### Sample Input

<pre>
4
2 20 10
2 10 0
4 25 25 25 25
3 24 30 21
</pre>
  	
### Sample Output

<pre>
Case #1: 33.333333 66.666667
Case #2: 0.000000 100.000000
Case #3: 25.0 25.0 25.0 25.0
Case #4: 34.666667 26.666667 38.666667
</pre>

Originally posted at [https://code.google.com/codejam/contest/1836486/dashboard#s=p0](https://code.google.com/codejam/contest/1836486/dashboard#s=p0).
