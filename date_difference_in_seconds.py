from datetime import datetime

date1 = datetime(2025, 2, 20, 14, 30, 0)
date2 = datetime(2025, 2, 21, 16, 45, 0)

difference_in_seconds = (date2 - date1).total_seconds()

print("Difference in Seconds:", difference_in_seconds)
