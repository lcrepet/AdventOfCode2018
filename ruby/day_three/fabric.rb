class Fabric
  def initialize(claims)
    @claims = claims
    @area = {}
  end

  def draw
    @claims.each do |claim|
      claim.x.upto(claim.x + claim.width - 1) do |i|
        claim.y.upto(claim.y + claim.length - 1) do |j|
            @area[[i, j]] ||= []
            @area[[i, j]] << claim.id
        end
      end
    end
  end

  def overlapping_points
    @area.select { |_, ids| ids.count > 1 }
  end

  def number_of_overlapped_points
    overlapping_points.count
  end

  def not_overlapped_claim
    @claims.find do |claim|
      overlapping_points.values.none? { |ids| ids.include?(claim.id) }
    end
  end

  def to_s
    max_i = @area.keys.map(&:first).max
    max_j = @area.keys.map { |k| k[1] }.max

    0.upto(max_i) do |i|
      str = ''
      0.upto(max_j) do |j|
        str += (@area[[i, j]] || [0]).join.to_s
        str += "\t"
      end
      puts str
    end
  end
end
