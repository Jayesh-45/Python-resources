import time
# This is the function that checks and displays the local time.

local_time = time.asctime(time.localtime(time.time()))
print(local_time)

initial = time.time()

for i in range(45):
     print("Hello..")
print("The execution time was", time.time() - initial, "Seconds.")

initial2 = time.time()
k = 0
while(k<10):
    print("Hello")
    time.sleep(1)
    k = k + 1
print("The execution time was", time.time() - initial2, "Seconds.")
