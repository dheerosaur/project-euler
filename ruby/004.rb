#!/usr/bin/env ruby

m = 0
901.upto(999) { |a|
    901.upto(999){ |b|
        s = (a * b).to_s
        m = [m, a * b].max if s == s.reverse
    }
}
puts m
