#!/usr/bin/env ruby

# n - number of islands
# t - island survival threshold
# k - number of receiving islands
# j - list of receiving islands with quantity

Pair = Struct.new(:to, :amount)

while input = gets
  n = input.chomp!.to_i

  surplus, from_to = Array.new(n + 1, 0), Array.new(n + 1)

  # initialize list of islands
  (1..n).each do |idx|
    from_to[idx] = []
  end

  # load islands thresholds and set up resource dependencies
  (1..n).each do |idx|
    t, k, *j = gets.chomp!.split(" ").map { |token| token.to_i }
    (1..k).each do |ji|
      pair = Pair.new(idx, j[2*ji-1])
      surplus[idx] += pair.amount
      from_to[j[2*ji-2]] << pair
    end
    surplus[idx] -= t
  end

  # queue first isle, and remove resources until queue is empty
  dead, dead_queue, surplus[1] = 0, [1], -1
  while !dead_queue.empty?
    dead += 1
    dead_isle_id = dead_queue.pop
    from_to[dead_isle_id].each do |pair|
      if surplus[pair.to] >= 0
        surplus[pair.to] -= pair.amount
        if surplus[pair.to] < 0
          dead_queue << pair.to
        end
      end
    end
  end
  puts n - dead
end
