require_relative 'fabric'
require_relative 'claim'

inputs = ARGV.first.split("\n")
claims = inputs.map { |input| Claim.create_from(input) }
fabric = Fabric.new(claims)

fabric.draw

puts "NUMBER OF OVERLAPPED POINTS: #{fabric.number_of_overlapped_points}"
