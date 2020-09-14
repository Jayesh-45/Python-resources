> # This Readme Contains all the explainations for the functions in the Time module.

- First we import the time module for the inbuilt python libraries.

        import time
- Then we start the time clock from absolute 0 as initial using time.time() function.
  > ## time.time() Function
  
        initial = time.time()

- The time() function returns the number of seconds passed since each point where time starts.
- Here the time counter starts from 0.
- Then after printing the Hello statement for 45 times, we then find out the execution time by..


        print("The execution time was", time.time() - initial, "Seconds.").
   
- Hence, the execution time for printing a statement for N number of times(Just used for example), was determined.
----
> ## time.sleep() Function

         time.sleep(1)
                
- The sleep() function delays execution of the current task for the given number of seconds in the parentheses brackets.

        print("This is first print statement.")
        time.sleep(6)
        print("This is printed after 6 seconds.")
