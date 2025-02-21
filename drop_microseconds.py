from datetime import datetime

current_datetime = datetime.now()

datetime_no_microseconds = current_datetime.replace(microsecond=0)

print("Datetime with Microseconds:", current_datetime)
print("Datetime without Microseconds:", datetime_no_microseconds)
