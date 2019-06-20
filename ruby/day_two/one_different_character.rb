require_relative 'box'

input = ARGV.first

boxes = input.split("\n").map { |id| Box.new(id) }
different_character_position = -1

one_of_boxes = boxes.find do |box|
  boxes.each do |other_box|
    different_character_position = box.find_different_character_in(other_box.id)
    break if different_character_position > -1
  end

  different_character_position > -1
end

common_letters = one_of_boxes.id
common_letters.delete_at(different_character_position)

puts "COMMON LETTERS: #{common_letters.join}"

