import json
from datetime import datetime, timedelta

with open('date_data.json', 'r') as json_file:
    date_data = json.load(json_file)

current_date = datetime.fromisoformat(date_data['current_date'])
subtract_five_days = datetime.fromisoformat(date_data['subtract_five_days'])
yesterday = datetime.fromisoformat(date_data['yesterday'])
today = datetime.fromisoformat(date_data['today'])
tomorrow = datetime.fromisoformat(date_data['tomorrow'])
date1 = datetime.fromisoformat(date_data['date1'])
date2 = datetime.fromisoformat(date_data['date2'])

# 1. Print the current date and date after subtracting five days
print("Current Date:", current_date)
print("Five Days Ago:", subtract_five_days)

# 2. Print yesterday, today, and tomorrow
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# 3. Drop microseconds
current_date_no_microseconds = current_date.replace(microsecond=0)
print("Current Date without Microseconds:", current_date_no_microseconds)

# 4. Calculate difference between two dates in seconds
difference_in_seconds = (date2 - date1).total_seconds()
print("Difference in Seconds:", difference_in_seconds)
