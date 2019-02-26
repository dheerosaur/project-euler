#!/usr/bin/env ruby

sum, sum_of_squares = 0, 0
1.upto(100) { |n|
  sum_of_squares += n * n
  sum += n
}
puts (sum * sum) - sum_of_squares
