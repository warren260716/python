import time as T
timer = T.localtime()
# print(type(timer))
year = timer.tm_year
month = timer.tm_mon
day = timer.tm_mday
hour = timer.tm_hour
minute = timer.tm_min
second = timer.tm_sec
print(f"{year}-{month}-{day} {hour}:{minute}:{second}")
# 2026-8-3 14:37:48