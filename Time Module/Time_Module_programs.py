import time
# This is the function that checks and displays the local time.

local_time = time.asctime(time.localtime(time.time()))
print(local_time)
