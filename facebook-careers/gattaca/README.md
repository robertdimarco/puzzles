#Gattaca#

* Difficulty:  Snack
* Keyword:     gattaca
* Completed:   2009-09-02 [C]

You have a DNA string that you wish to analyze. Of particular interest is which intervals of the string represent individual genes. You have a number of “gene predictions”, each of which assigns a score to an interval within the DNA string, and you want to find the subset of predictions such that the total score is maximized while avoiding overlaps. A gene prediction is a triple of the form (**start**, **stop**, **score**). **start** is the zero-based index of the first character in the DNA string contained in the gene. **stop** is the index of the last character contained in the gene. **score** is the score for the gene.

**Input specifications**

Your program will be passed the name of an input file on the command line. The contents of that file are as follows. The first line of the input contains only **n**, the length of the DNA string you will be given. The next ceiling(**n** / 80) lines each contain string of length 80 (or **n** % 80 for the last line) containing only the characters ‘A’, ‘C’, ‘G’, and ‘T’. Concatenate these lines to get the entire DNA strand. The next line contains only **g**, the number of gene predictions you will be given. The next **g** lines each contain a whitespace-delimited triple of integers of the form:

<pre>
[start] [stop] [score]
</pre>

representing a single gene prediction. No gene predictions will exceed the bounds of the DNA string or be malformed (**start** is non-negative and no more than **stop**, **stop** never exceeds **n** – 1).

Example input:
<pre>
100
GAACTATCGCCCGTGCGCATCGCCCGTCCGACCGGCCGTAAGTCTATCTCCCGAGCGGGCGCCCGATCTCAAGTGCACCT
CACGGCCTCACGACCGTGAG
8
43  70  27
3   18  24
65  99  45
20  39  26
45  74  26
10  28  20
78  97  23
0   9   22
</pre>

**Output specifications**

Print to standard out the score of the best possible subset of the gene predictions you are given such that no single index in the DNA string is contained in more than one gene prediction, followed by a newline. The total score is simply the sum of the scores of the gene predictions included in your final result.

When constructing your output, you may only consider genes exactly as they are described in the input. If you find the contents of a gene replicated elsewhere in the DNA string, you are not allowed to treat the second copy as a viable gene. Your solution must be fast and efficient to be considered correct by the robot.
Example output (newline after integer):

<pre>
100
</pre>

Originally published at http://www.facebook.com/careers/puzzles.php?puzzle_id=15.