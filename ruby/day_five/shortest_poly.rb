require_relative 'polymer'

input = ARGV.first

reduced_polymers = {}
units = input.split('')
units_types = units.map(&:downcase).uniq


units_types.each do |unit_type|
  reduced_polymers[unit_type] = Polymer.new(input.gsub(/#{unit_type}/i, '').split('')).reduce
end
shortest_polymer = reduced_polymers.sort_by{ |polymer| polymer.last.count }.first

puts "NUMBER OF REMAINING UNITS: #{shortest_polymer.last.count}"

