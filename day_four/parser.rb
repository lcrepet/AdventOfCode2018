require_relative 'guard'
require_relative 'timestamp'

class Parser
  def parse_guards(records_by_hour)
    guards_hash = {}
    guard_id = nil
    timestamps = []

    records_by_hour.each do |hour, record|
      id = record.include?('#') ? record.split('#').last.split.first : nil
      if id
        unless guard_id.nil?
          if guards_hash[guard_id]
            guards_hash[guard_id].add(timestamps)
          else
            guards_hash[guard_id] =  Guard.new(guard_id, timestamps)
          end
        end

        guard_id = id
        timestamps = []
        record = 'begins shift'
      end

      timestamps << Timestamp.new(hour, record)
    end
    if guards_hash[guard_id]
      guards_hash[guard_id].add(timestamps)
    else
      guards_hash[guard_id] =  Guard.new(guard_id, timestamps)
    end

    guards_hash.values
  end
end
