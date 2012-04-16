## Problem C. Recycled Numbers

### Problem

Do you ever become frustrated with television because you keep seeing the same things, recycled over and over again? Well I personally don't care about television, but I do sometimes feel that way about numbers.

Let's say a pair of distinct positive integers (*n*, *m*) is recycled if you can obtain *m* by moving some digits from the back of *n* to the front without changing their order. For example, (12345, 34512) is a recycled pair since you can obtain 34512 by moving 345 from the end of 12345 to the front. Note that *n* and *m* must have the same number of digits (excluding leading zeros) in order to be a recycled pair.

Given integers **A** and **B** with the same number of digits, how many distinct recycled pairs (*n*, *m*) are there with **A** ≤ *n* < *m* ≤ **B**?

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each test case consists of a single line containing the integers **A** and **B**.

### Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is the number of recycled pairs (*n*, *m*) with **A** ≤ *n* < *m* ≤ **B**.

### Limits

1 ≤ **T** ≤ 50.
**A** and **B** have the same number of digits.

### Small dataset

1 ≤ A ≤ B ≤ 1000.

### Large dataset

1 ≤ A ≤ B ≤ 2000000.

### Sample Input

<pre>
4
1 9
10 40
100 500
1111 2222
</pre>

### Sample Output

<pre>
Case #1: 0
Case #2: 3
Case #3: 156
Case #4: 287
</pre>

### Are we sure about the output to Case #4?

Yes, we're sure about the output to Case #4.