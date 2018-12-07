require_relative 'action'

class Guard
  attr_reader :id, :schedule

  def initialize(id, timestamps)
    @id = id
    @timestamps_by_day = timestamps.group_by(&:day)
    @schedule = {}
  end

  def add(timestamps)
    new_timestamps_by_day = timestamps.group_by(&:day)
    new_timestamps_by_day.each do |day, new_timestamps|
      @timestamps_by_day[day] ||= []
      @timestamps_by_day[day] += new_timestamps
    end
  end

  def number_of_sleeping_minutes
    @schedule.values.sum
  end

  def schedule_entry_of_max_sleeping
    max = @schedule.values.max
    @schedule.find { |_, count| count == max }
  end

  def build_schedule
    '00'.upto('59') { |minutes| @schedule[minutes] = 0 }

    @timestamps_by_day.each do |day, timestamps|
      timestamp_index = 0
      timestamp = timestamps[timestamp_index]
      is_asleep = false

      '00'.upto('59') do |minutes|
        unless minutes < timestamp.minutes
          is_asleep = timestamp.sleeping_time
          timestamp_index += 1
          timestamp = timestamps[timestamp_index]
        end

        @schedule[minutes] += 1 if is_asleep
        break unless timestamp
      end
    end
  end
end
