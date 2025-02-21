import json
from datetime import datetime, timedelta

# Создание данных, связанных с датами
date_data = {
    "current_date": datetime.now().isoformat(),
    "subtract_five_days": (datetime.now() - timedelta(days=5)).isoformat(),
    "yesterday": (datetime.now() - timedelta(days=1)).isoformat(),
    "today": datetime.now().isoformat(),
    "tomorrow": (datetime.now() + timedelta(days=1)).isoformat(),
    "date1": datetime(2025, 2, 20, 14, 30, 0).isoformat(),
    "date2": datetime(2025, 2, 21, 16, 45, 0).isoformat()
}

# Сохранение данных в JSON файл
with open('date_data.json', 'w') as json_file:
    json.dump(date_data, json_file, indent=4)

