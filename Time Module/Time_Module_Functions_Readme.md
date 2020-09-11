> # This Readme Contains all the explainations for the functions in the Time module.

- First we import the time module for the inbuilt python libraries.

        import time
- Then we start the time clock from absolute 0 as initial using time.time() function.
   
        initial = time.time()

- The time() function returns the number of seconds passed since each point where time starts.
- Here the time counter starts from 0.
- Then after printing the Hello statement for 45 times, we then find out the execution time by..


        print("The execution time was", time.time() - initial, "Seconds.").
   
- Hence, the execution time for printing a statement for N number of times(Just used for example), was determined.
