input = ARGV.first

frequency_changes = input.split("\n").map(&:to_i)
frequencies_history = [0]
index = 0
changes_count = frequency_changes.count
current_frequency = 0

frequency_changes.each do |change|
  frequencies_history << frequencies_history.last + change
end

while frequencies_history.index(current_frequency).nil?
  index += 1
  frequencies_history << current_frequency
  current_frequency += frequency_changes[index % changes_count]
end

puts "DUPLICATE FREQUENCY: {duplicated_frequency}"
