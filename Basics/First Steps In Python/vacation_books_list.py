# Vacation books list

pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_time = pages / pages_per_hour
hours_per_day = total_time / days

print(hours_per_day)
