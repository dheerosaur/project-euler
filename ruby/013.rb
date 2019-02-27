
File.open('data/013') do |file|
  sum = 0
  file.each_line do |line|
    sum += line.to_i
  end
  puts sum.to_s[0..9]
end
