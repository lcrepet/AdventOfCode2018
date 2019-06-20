require_relative 'box'

input = ARGV.first

boxes = input.split("\n").map { |id| Box.new(id) }

puts "CHECKSUM: #{boxes.select(&:id_contains_two_duplicates?).count * boxes.select(&:id_contains_three_duplicates?).count}"

