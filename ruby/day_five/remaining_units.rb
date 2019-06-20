require_relative 'polymer'

input = ARGV.first
units = input.split('')

reduced_polymer = Polymer.new(units).reduce

puts "NUMBER OF REMAINING UNITS: #{reduced_polymer.count}"
