class Claim
  attr_reader :id, :x, :y, :width, :length

  def initialize(id, x, y, width, length)
    @id = id
    @x = x.to_i
    @y = y.to_i
    @width = width.to_i
    @length = length.to_i
  end

  def self.create_from(claim_str)
    id, start_point, measurements = claim_str.gsub(/[#@:]/, '').split
    x, y = start_point.split(',')
    width, length = measurements.split('x')

    new(id, x, y, width, length)
  end
end
