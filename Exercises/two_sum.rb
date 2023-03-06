#!/usr/bin/env ruby

def two_sum(input, target)
  map = {}

  input.each_with_index do |num, i|
    complement = target - num
    if map.key?(complement)
      return [map.fetch(complement), i]
    end
    map[num] = i
  end
  return nil
end

p two_sum([2,7,11,15], 9)
p two_sum([3,2,4], 6)
p two_sum([3,3], 6)
