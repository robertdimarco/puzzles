#!/usr/bin/env ruby -n

require 'date'

def best_before(str)
  valid_dates = []
  input = str.split("/").map { |x| x.to_i }
  input.permutation { |perm|
    begin
      year, month, day = perm
      year = (year < 1000) ? year + 2000 : year
      date = Date.new(year, month, day)
      valid_dates << date
    rescue ArgumentError
    end
  }
  return (valid_dates.length == 0) ? "#{str} is illegal" : valid_dates.min().to_s
end

puts best_before($_.chop)

