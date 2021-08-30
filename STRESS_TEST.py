# STRESS_TEST: Stresses the CPU of your PC.

# Import utils for use
import os, sys, time, math, random, multiprocessing as mp
from multiprocessing import Process

# Define CPU Stress code block..
def cpuburn():
    while True:
        op = random.randint(0, 6)
        if (op == 0):
            math.acosh(9223372036854775807)
        elif (op == 1):
            math.factorial(2147483647)
        elif (op == 2):
            math.sqrt(9223372036854775807)
        elif (op == 3):
            math.log(9223372036854775807)
        elif (op == 4):
            math.cos(9223372036854775807)
        elif (op == 5):
            math.pow(2, 256)

# Prevent subprocess modules from executing this code block.
if __name__ == "__main__" and not os.path.exists("STRESS_TEST.exe.lock"):
    
    # Get initialization parameters from the user.
    dur_time = float(input("How long do you want to run the stress test?\n> "))

    # Acquire artificial file lock. Since this resource will have multiple processes utilizing it, we do not want to acquire a real lock.
    file = open("STRESS_TEST.exe.lock", "w")
    file.close()


    # Initialize use variables
    current_time = time.time()
    end_time = current_time + dur_time
    cores = os.cpu_count()
    core_mult = 2
    mp.set_start_method("spawn")

    # Create n threads to tax the CPU as much as possible.

    print("Your device has " + str(cores) + " CPU cores available.")

    # Create CPU hogs and allocate space for them.
    threads = []
    print("Creating " + str(cores * core_mult) + " threads.")

    for core in range(0, cores * core_mult):
        threads.append(Process(target=cpuburn, args=()))

    # Inform user of threads.
    print("Created " + str(cores * core_mult) + " threads.")
    print("Starting CPU stress threads.")

    for thread in threads:
        #print("Started " + thread.name)
        thread.start()
        
    print("Executing CPU stress threads.")
        
    # Announce presence of threads and wait for threads to exit.

    time.sleep(dur_time)

    if time.time() >= end_time:
        print("Stress test complete.")
        for thread in threads:
            #print("Terminating " + thread.name)
            thread.kill()

    # Release lock after code execution complete.
    os.unlink("STRESS_TEST.exe.lock")

# The compiled binary makes all of the python subprocesses think that they are the main thread.
else:
    while True:
        op = random.randint(0, 6)
        if (op == 0):
            math.acosh(9223372036854775807)
        elif (op == 1):
            math.factorial(2147483647)
        elif (op == 2):
            math.sqrt(9223372036854775807)
        elif (op == 3):
            math.log(9223372036854775807)
        elif (op == 4):
            math.cos(9223372036854775807)
        elif (op == 5):
            math.pow(2, 256)
    

