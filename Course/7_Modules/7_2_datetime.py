import datetime

# Aktuális dátum és idő
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# Aktuális dátum
current_date = datetime.date.today()
print("Current date:", current_date)

# Aktuális idő
current_time = datetime.datetime.now().time()
print("Current time:", current_time)

# Dátum és idő formázása
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_datetime)

# Dátum és idő létrehozása manuálisan
manual_datetime = datetime.datetime(2021, 12, 31, 23, 59, 59)
print("Manual date and time:", manual_datetime)

# Időkülönbség kiszámítása (timedelta)
start_date = datetime.datetime(2023, 7, 1)
end_date = datetime.datetime(2023, 7, 6)
difference = end_date - start_date
print("Difference:", difference)
print("Days:", difference.days)
print("Seconds:", difference.seconds)

# stringből dátum és idő létrehozása
date_str = "2023-07-01 12:43"
date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
print("Date:", date)

# Jövőbeli vagy múltbéli dátum kiszámítása
future_date = current_date + datetime.timedelta(days=7)
print("Future date:", future_date)
past_date = current_date - datetime.timedelta(days=7)
print("Past date:", past_date)
