import time
# time_object = time.localtime()
# time_object = time.gmtime # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)

# time_string = "20 April, 2023"
# time_object = time.strptime(time_string, "%d %B, %Y")
#

# (year, month, day, hours, minutes, secs, # ody of the week, # day of the year, dst)
time_tuple = (2023, 4, 20, 4, 20, 0, 0, 0, 0)

time_string = time.asctime(time_tuple)
print(time_string)
