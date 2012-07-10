## Best Before

  * Problem ID: `bestbefore`
  * Difficulty: `Reggae`

Just about any product found in a grocery store has a "best before" date printed on it. Unfortunately, the format for these dates can vary quite a bit: what is it supposed to mean that the bread you bought yesterday is "best before 12/11/10"? It could mean that the bread expires on November 10, 2012 (now that's a suspiciously durable bread and probably it is not healthy for you for other reasons!), or it could mean that the bread expired on December 11, 2010 (d'oh!), or a variety of other options. To be safe, the truly paranoid (or healthily skeptic, depending on who you ask) person would assume that it means "best before November 12, 2010", since that is the earliest possible date. On the other hand, seeing "31/5/2012" even the truly paranoid person knows that this must mean May 31, 2012 since that is the only possible real date using these three numbers.

Given a possibly ambiguous date "A/B/C", where A,B,C are integers between 0 and 2999, output the earliest possible legal date between Jan 1, 2000 and Dec 31, 2999 (inclusive) using them as day, month and year (but not necessarily in that order).

Recall that a year is a leap year (has 366 days) if the year is divisible by 4, unless it is divisible also by 100 but not by 400 (so 2000 is a leap year, 2100 is not a leap year, and 2012 is a leap year).

### Input

The input file consists of a single line containing three integers separated by "/". There are no extra spaces around the "/". Years may be truncated to two digits and may in that case also omit the leading 0 (if there is one), so 2000 could be given as "2000", "00" or "0" (but not as an empty string). Months and days may be zero-padded. You may assume that the year, when given with four digits, is between 2000 and 2999. At most one of the integers has four digits, and the others have one or two digits.

### Output

Output a single line giving the earliest legal date possible given the above constraints. The output should be formatted as year-month-day, where year has four digits, and month and day have two digits each (zero padding), for example "2011-07-15". If there is no legal date (subject to the above constraints) then output a single line with the original string followed by the words "is illegal".

#### Sample input 1
<pre>
02/4/67
</pre>

#### Sample output 1
<pre>
2067-02-04
</pre>

#### Sample input 2
<pre>
31/9/73
</pre>

#### Sample output 2
<pre>
31/9/73 is illegal
</pre>

Originally posted at [http://www.spotify.com/us/jobs/tech/best-before/](http://www.spotify.com/us/jobs/tech/best-before/).
