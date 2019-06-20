class Polymer
  attr_reader :units

  def initialize(units)
    @units = units
  end

  def reduce
    stack = []

    0.upto(units.count - 1) do |index|
      if stack.last != units[index] && stack.last&.downcase == units[index].downcase
        stack.pop
      else
        stack.push(units[index])
      end
    end

    stack
  end
end
