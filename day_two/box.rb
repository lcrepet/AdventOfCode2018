class Box
  attr_reader :id

  def initialize(id)
    @id = id.split('')
  end

  def id_contains_two_duplicates?
    @id.find { |character| @id.count(character) == 2 }
  end

  def id_contains_three_duplicates?
    @id.find { |character| @id.count(character) == 3 }
  end

  def find_different_character_in(other_id)
    diff_position = -1
    current_position = 0

    return diff_position if @id == other_id
    return diff_position if @id.count != other_id.count

    @id.zip(other_id).each do |character, other_character|
      if character != other_character
        if diff_position > -1
          diff_position = -1
          break
        end
        diff_position = current_position
      end

      current_position += 1
    end

    diff_position
  end
end
