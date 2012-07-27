## Problem H: Collapse

  * Problem ID: `collapse`
  * Time limit: 3 seconds
  * Memory limit: 2048 MB

Trouble has come to the remote group of islands known as Insumulia. Due to an unfortunate combination of over-consumption, natural climate variations, and generally difficult conditions, the island of Incunabula has run out of trees. Because several other Insumulian islands depended on trees from Incunabula through trade, its collapse will have repercussions all over Insumulia. In this problem, we’ll simulate a (highly oversimplified) model of the situation to determine the effects of the collapse of Incunabula.

We model the situation as follows. Each island has a *threshold T<sub>i</sub>* on the amount of incoming goods (for simplicity we assume that there is only a single commodity of goods) it needs to receive per lunar cycle in order for the society of the island to sustain itself. If the amount of incoming goods drops below the threshold, society on the island will collapse and die out, and the island will no longer provide goods to other islands, thereby potentially causing them to collapse as well. Each island provides some amount of goods to a number of other islands. If an island collapses, we assume that goods that would have been delivered to that island is effectively lost; it does not get redistributed and delivered to other islands instead. Also, once an island dies out it is not repopulated (until possibly long after the ongoing collapses have finished).

Your job is to write a program to compute the number of islands that survive after the potential chain reaction of collapses that is caused by the collapse of Incunabula.

### Input

The first line of input contains one integer *N* (1 ≤ *N* ≤ 100000), the number of islands in Insumulia.

Then follow *N* lines, describing each island. The *i*’th such description starts with two integers *T<sub>i</sub>*, *K<sub>i</sub>*, where 0 ≤ *T<sub>i</sub>* ≤ 50000 is the amount of goods the *i*’th island needs to receive in order to survive, and 0 ≤ *K<sub>i</sub>* ≤ *N*−1 is the number of other islands the *i*’th islands receives goods from. The remainder of the description of the *i*’th island is a list of *K<sub>i</sub>* pairs of integers. The *j*’th such pair, *S<sub>ij</sub>*, *V<sub>ij</sub>*, indicates that island *i* receives *V<sub>ij</sub>* units of goods from island *S<sub>ij</sub>* each lunar cycle. You may assume that the *S<sub>ij</sub>*’s are distinct and between 1 and *N* (inclusive), and that none of them equals i. The values *V<sub>ij</sub>* satisfy 1 ≤ *V<sub>ij</sub>* ≤ 1000 and their sum is at least *T<sub>i</sub>*. The sum of all the *K<sub>i</sub>*’s for all the *N* islands is at most 500000.

Islands are numbered from 1 to *N*, and Incunabula is island number 1.

### Output

Output a single integer, the number of islands surviving the collapses.

<table>
  <thead>
    <tr>
      <th>Sample Input</th>
      <th>Sample Output</th>
  </thead>
  <tbody>
    <tr>
      <td>
        <pre>
          4
          0 0
          25 3 1 10 3 10 4 10
          10 1 2 10
          10 1 2 10
        </pre>
      </td>
      <td>0</td>
    </tr>
    <tr>
      <td>
        <pre>
          4
          0 0
          20 3 1 10 3 10 4 10
          10 1 2 10
          10 1 2 10
        </pre>
      </td>
      <td>3</td>
    </tr>
  </tbody>
</table>

Originally posted at [https://contest.codequest.spotify.com/problems/collapse](https://contest.codequest.spotify.com/problems/collapse).

Author: Per Austrin. License: [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)](http://creativecommons.org/licenses/by-sa/3.0/).
