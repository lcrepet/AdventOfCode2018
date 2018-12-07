input = ARGV.first

frequency_changes = input.split("\n").map(&:to_i)

puts "FINAL FREQUENCY: #{frequency_changes.sum}"


