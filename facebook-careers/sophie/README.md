## Find Sophie

  * Keyword:     `sophie`
  * Difficulty:  `Buffet`

### Input specifications

The input file starts with a single number, **m**, followed by a newline. **m** is the number of locations available for Sophie to hide in your apartment. This line is followed by **m** lines, each containing information for a single location of the form (brackets for clarity):

<pre>
[location name] [probability]
</pre>

**probability** is the probability that Sophie is hiding in the location indicated. The sum of all the probabilities is always 1. The contents of these lines are separated by whitespace. Names will only contain alphanumeric characters and underscores ('_'), and there will be no duplicate names. All input is guaranteed to be well-formed. Your starting point is the first location to be listed, and in effect it costs you no time to check if Sophie is there.

The file continues with a single number, **c**, followed by a newline. **c** is the number of connections that exist between the various locations. This line is followed by **c** lines, each of the form:

<pre>
[location name] [location name] [seconds]
</pre>

The first two entries are the names of locations and **seconds** is the number of seconds it takes you to walk between the them. Again these lines are whitespace-delimited. Note that the locations are unordered; you can walk between them in either direction and it will take the same amount of time. No duplicate pairs will be included in the input file, and all location names will match one described earlier in the file.

Example input file:
<pre>
4
front_door .2
in_cabinet .3
under_bed .4
behind_blinds .1
5
front_door under_bed 5
under_bed behind_blinds 9
front_door behind_blinds 5
front_door in_cabinet 2
in_cabinet behind_blinds 6
</pre>

### Output specifications

Your output must consist of a single number followed by a newline, printed to standard out. The number is the minimum expected time in seconds it takes to find Sophie, rounded to the nearest hundredth. Make sure that the number printed has exactly two digits after the decimal point (even if they are zeroes). If it is impossible to guarantee that you will find Sophie, print "-1.00" followed by a newline instead.

Example output:
<pre>
6.00
</pre>

Originally published at [http://www.facebook.com/careers/puzzles.php?puzzle_id=11](http://www.facebook.com/careers/puzzles.php?puzzle_id=11).
