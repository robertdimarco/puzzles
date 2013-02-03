## Card Game

  * Points: `20`

John is playing a game with his friends. The game's rules are as follows: There is deck of **N** cards from which each person is dealt a hand of **K** cards. Each card has an integer value representing its strength. A hand's strength is determined by the value of the highest card in the hand. The person with the strongest hand wins the round. Bets are placed before each player reveals the strength of their hand.

John needs your help to decide when to bet. He decides he wants to bet when the strength of his hand is higher than the average hand strength. Hence John wants to calculate the average strength of ALL possible sets of hands. John is very good at division, but he needs your help in calculating the sum of the strengths of all possible hands.

### Problem

You are given an array a with **N** ≤ 10000 different integer numbers and a number, **K**, where **1 ≤ K ≤ N**. For all possible subsets of a of size **K** find the sum of their maximal elements modulo 1000000007.

### Input

The first line contains the number of test cases **T**, where **1 ≤ T ≤ 25**.

Each case begins with a line containing integers **N** and **K**. The next line contains N space-separated numbers **0 ≤ a[i] ≤ 2000000000**, which describe the array **a**.

### Output

For test case **i**, numbered from 1 to **T**, output "Case #i: ", followed by a single integer, the sum of maximal elements for all subsets of size **K** modulo 1000000007.

### Example

For **a = [3, 6, 2, 8]** and **N = 4** and **K = 3**, the maximal numbers among all triples are **6, 8, 8, 8** and the sum is **30**.

1 ≤ length of **s** ≤ 100

### Example Input

    5
    4 3
    3 6 2 8
    5 2
    10 20 30 40 50
    6 4
    0 1 2 3 5 8
    2 2
    1069 1122
    10 5
    10386 10257 10432 10087 10381 10035 10167 10206 10347 10088

### Example Output

    Case #1: 30
    Case #2: 400
    Case #3: 103
    Case #4: 1122
    Case #5: 2621483

Originally published at [https://www.facebook.com/hackercup/problems.php?pid=321892127915788&round=189890111155691](https://www.facebook.com/hackercup/problems.php?pid=321892127915788&round=189890111155691).