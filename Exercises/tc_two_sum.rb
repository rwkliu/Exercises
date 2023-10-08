require_relative "two_sum.rb"
require "test/unit"

class TestTwoSum < Test::Unit::TestCase
  def test_simple
    assert_equal([0,1], two_sum([2,7,11,15],9))
    assert_equal([1,2], two_sum([3,2,4],6))
    assert_equal([0,1], two_sum([3,3], 6))
  end
end