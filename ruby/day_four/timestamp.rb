class Timestamp
  attr_reader :day, :minutes, :sleeping_time

  def initialize(time, record)
    @time = time
    @day = time.split.first
    @minutes = time.split(':').last
    @sleeping_time = record == 'falls asleep'
  end
end
