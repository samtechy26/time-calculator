def add_time(start, duration, day=None):
  # Split the string to useful data
  start_hour = int(start.split(' ')[0].split(':')[0])
  start_minute = int(start.split(' ')[0].split(':')[1])
  duration_hour = int(duration.split(':')[0])
  duration_minute = int(duration.split(':')[1])
  con = start.split(' ')[1]

  week_days = {
      0: "Monday",
      1: "Tuesday",
      2: "Wednesday",
      3: "Thursday",
      4: "Friday",
      5: "Saturday",
      6: "Sunday"
  }

  if con == 'AM':
    start_hour -= 12

  # implement conversions
  total_minutes = (start_hour * 60) + start_minute + (duration_hour *
                                                      60) + duration_minute
  total_hour = start_hour + duration_hour + (
      (start_minute + duration_minute) // 60)
  new_con = 'PM' if total_hour < 12 else 'AM'
  new_hour = (total_minutes // 60) % 12
  new_minutes = total_minutes % 60

  if new_hour == 0:
    new_hour = 12

  total_day = (total_hour // 24) + (1 if total_hour >= 12 else 0)

  if new_minutes < 10:
    new_minutes = '0' + str(new_minutes)
  if duration_hour == 0 and duration_minute == 0:
    new_time = str(new_hour) + ':' + str(new_minutes) + ' ' + con
    return new_time
  new_time = str(new_hour) + ':' + str(new_minutes) + ' ' + new_con

  # Check if a particular day is provided
  if (day == None):
    if total_day == 0:
      return new_time
    if total_day == 1:
      new_time = new_time + ' ' + '(next day)'
      return new_time
    return new_time + ' ' + '(' + str(total_day) + ' days later)'
  else:
    day_list = list(week_days.values())
    current_day_no = day_list.index(day.capitalize())
    expected_day_no = (current_day_no + total_day) % 7
    expected_day = week_days[expected_day_no]

    if total_day == 0:
      new_time = new_time + ', ' + expected_day
      return new_time
    if total_day == 1:
      new_time = new_time + ', ' + expected_day + ' (next day)'
      return new_time
    return new_time + ', ' + expected_day + ' (' + str(
        total_day) + ' days later)'
