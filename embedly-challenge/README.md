# Embed.ly Challenge

Howdy! This little challenge is meant to be fun and still pertain to the work we do at [Embedly](http://embed.ly/company/jobs).

All these problems are designed to be solved with less than 20 lines of code.

If you have any questions, hit us up: [@embedly](http://twitter.com/embedly).

This challenge is based off of [Greplin's](http://challenge.greplin.com/) back in 2010.

## Problem 1 of 3: Math

<pre>
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800

Let R(n) equal the sum of the digits in the number n!

For example, R(10) is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
</pre>

Find the lowest value for n where R(n) is 8001.

## Problem 2 of 3: HTML

One way to exclude miscellaneous text from an article is to find the [standard deviation](http://en.wikipedia.org/wiki/Standard_deviation) of the depth of the <p> tags for the <article>. For the following HTML we can draw a depth tree like so.

<pre><code>
<article>
 <p>Sign Up Today</p>
 <div>
   <p>Content</p>
   <div>
    <img />
    <p>Img Caption</p>
   </div>
   <p>Content</p>
 </div>
</article>
</code></pre>

<pre>
article - 0
  p - 1
  div - 1
    p - 2
    div - 2
      img - 3
      p - 3
    p - 2
</pre>

For [http://apply.embed.ly/static/data/2.html](https://github.com/robertdimarco/engineering-puzzles/raw/master/embedly-challenge/2.html) find the standard deviation of all the <p> tags within the <article> tag. Round to the nearest tenth: X.X.

## Problem 3 of 3: Zipf's law

A simplified version of [Zipf's law](http://en.wikipedia.org/wiki/Zipf%27s_law):

> For a given body of text, the most frequent word will occur approximately twice as often as the second most frequent word, three times as often as the third most frequent word, etc.
> <pre>[x, x/2, x/3, x/4, x/5, ...]</pre>

The following is a frequency set of words in a body of text that follows Zipf's law:

<pre>
[
  ('the', 2520),
  ('of', 1260),
  ('and', 840),
  ('a', 630),
  ('to', 504)
  ...
]
</pre>

Given that the text has 900 unique words, how many unique words, starting with the most frequently used word, make up half the text?

Originally posted at [http://apply.embed.ly/](http://apply.embed.ly/).
