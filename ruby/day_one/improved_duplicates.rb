input = ARGV.first

frequency_changes = input.split("\n").map(&:to_i)
frequencies_history = [0]
frequencies_by_modulo = {}

frequency_changes.each do |change|
  frequencies_history << frequencies_history.last + change
end

step = frequencies_history.pop

frequencies_history.each_with_index do |frequency, index|
  frequencies_by_modulo[frequency % step] ||= []
  frequencies_by_modulo[frequency % step] << [frequency, index]
end

puts frequencies_by_modulo.inspect


