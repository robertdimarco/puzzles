#!/usr/bin/env ruby -n

# binomial coefficient
def nchoosek(n, k)
  if k < 0 or k > n
    return 0
  elsif k > (n - k)
    k = n - k
  end
  c = 1
  (0...k).each { |i|
    c = c * (n - (k - (i+1)))
    c = (c / (i+1))
  }
  return c
end

# hypergeometric distribution
def hypergeometric(r, m, n, k)
  return nchoosek(m,k) * nchoosek(r-m, n-k) / nchoosek(r, n)
end


# m the total number of people who entered the lottery
# n the total number of winners drawn
# t the number of tickets each winner is allowed to buy
# p the number of people in your group

m, n, t, p = $_.chop.split(" ").map { |i| i.to_f }
min_wins = (p / t).ceil.to_i
prob = 0.0
if min_wins <= n
  prob = 1.0
  (0...min_wins).each { |i|
    prob -= hypergeometric(m, p, n, i)
  }
end
puts "%.10f" % prob
