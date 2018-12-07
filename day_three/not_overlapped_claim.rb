require_relative 'fabric'
require_relative 'claim'

inputs = ARGV.first.split("\n")
claims = inputs.map { |input| Claim.create_from(input) }
fabric = Fabric.new(claims)

fabric.draw

puts "NOT OVERLAPPED CLAIM: #{fabric.not_overlapped_claim.id}"
