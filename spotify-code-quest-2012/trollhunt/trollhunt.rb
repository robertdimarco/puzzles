#!/usr/bin/env ruby -n

# b - the number of bridges
# k - the number of knights
# g - min knights per group

b, k, g = $_.chop.split(" ").map { |i| i.to_f }
groups = (k / g).floor
days = ((b - 1) / groups).ceil
puts days
