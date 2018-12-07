require_relative 'parser'

inputs = ARGV.first.split("\n")

records_by_hour = inputs.map do |input|
  dirty_hour, record = input.split('] ')
  hour = dirty_hour.gsub('[1518-', '')
  [hour, record]
end

records_by_hour = records_by_hour.sort_by { |pair| pair.first }.to_h
guards = Parser.new.parse_guards(records_by_hour)

guards.each(&:build_schedule)
sleeper = guards.sort_by { |guard| guard.number_of_sleeping_minutes }.last

puts "GUARD #{sleeper.id} SLEPT THE MOST ON #{sleeper.schedule_entry_of_max_sleeping[0]}MIN"
