## Equal Sums

### Problem

I have a set of positive integers **S**. Can you find two non-empty, distinct subsets with the same sum?

Note: A subset is a set that contains only elements from **S**, and two subsets are distinct if they do not have exactly the same elements.

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow, one per line. Each test case begins with **N**, the number of positive integers in **S**. It is followed by **N** distinct positive integers, all on the same line.

### Output

For each test case, first output one line containing "Case #x:", where x is the case number (starting from 1).

  * If there are two different subsets of **S** that have the same sum, then output these subsets, one per line. Each line should contain the numbers in one subset, separated by spaces.
  * If it is impossible, then you should output the string "Impossible" on a single line.

If there are multiple ways of choosing two subsets with the same sum, any choice is acceptable.

### Limits

No two numbers in **S** will be equal.
1 ≤ **T** ≤ 10.

### Small dataset

**N** is exactly equal to 20.
Each number in **S** will be a positive integer less than 10<sup>5</sup>.

### Large dataset

**N** is exactly equal to 500.
Each number in **S** will be a positive integer less than 10<sup>12</sup>.

### Sample Input

<pre>
2
20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
20 120 266 858 1243 1657 1771 2328 2490 2665 2894 3117 4210 4454 4943 5690 6170 7048 7125 9512 9600
</pre>

### Sample Output

<pre>
Case #1:
1 2
3
Case #2:
3117 4210 4943
2328 2894 7048
</pre>

Originally posted at [https://code.google.com/codejam/contest/1836486/dashboard#s=p2](https://code.google.com/codejam/contest/1836486/dashboard#s=p2).
