# This function takes a start time, a duration, and an optional day parameter. If no day is provided, it defaults to None.
def add_time(start, duration, day=None):
  # The function then splits the start time into hours and minutes, and converts it to 24 hour time if it is PM.
  # Next, the function does the same with the duration.
  time_elements = start.split()
  current_time = time_elements[0].split(":")
  if time_elements[1].upper() == "PM":
    current_time[0] = str(eval(current_time[0] + "+" + "12"))

  duraction_time = duration.split(":")
  future_hour = int(current_time[0], 10) + int(duraction_time[0], 10)
  future_minutes = int(current_time[1], 10) + int(duraction_time[1], 10)

  # Finally, it calculates the future hour and minutes by adding the start time and duration, and formats it into 12 hour time.
  if future_minutes >= 60:
    future_hour += 1
    future_minutes -= 60

  minutes_string = str(future_minutes)
  if future_minutes < 10:
    minutes_string = "0" + minutes_string

  future_days = future_hour // 24
  aux = future_hour // 12
  aux_2 = future_hour % 24
  future_hour -= aux * 12 
  if future_hour == 0:
    future_hour = 12

  if aux_2 >= 12:
    new_time = str(future_hour) + ":" + minutes_string + " PM"
  else:
    new_time = str(future_hour) + ":" + minutes_string + " AM"

  # If a day is provided, it calculates how many days in the future the new time will be, and returns the new time along with the day.
  if day != None:
    days = [
      "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
      "Sunday"
    ]
    index = days.index(day.capitalize())
    if index + future_days > len(days) - 1:
      index += future_days % len(days)
      if index > 6:
        index -= 7
    else:
      index += future_days
    new_time += ", " + days[index] 
  # If more than one day is calculated, it adds a message indicating how many days later the new time is.
  message = ""
  if future_days > 1:
    message += " (" + str(future_days) + " days later)"
  elif future_days == 1:
    message += " (next day)"
  new_time += message

  return new_time


print(add_time("11:40 AM", "0:25"))
print(add_time("8:16 PM", "466:02", "tuesday"))


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM
print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
