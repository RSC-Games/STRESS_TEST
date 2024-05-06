# STRESS_TEST: Stresses the CPU of your PC.
from multiprocessing import Process
import multiprocessing as mp
import random
import time
import math
import sys
import os

# Use at least double the available cores as threads. Comes at the cost of higher memory use.
CORE_MULT = 2

# Here lies the actual math that burns the CPU.
def cpuburn():
    while True:
        op = random.randint(0, 6)
        operand = random.randint(1283901827894, 12803803952045394850949045)
        if (op == 0):
            math.acosh(operand)
        elif (op == 1):
            math.factorial(math.min(operand, 2147483647))
        elif (op == 2):
            math.sqrt(operand)
        elif (op == 3):
            math.log(operand)
        elif (op == 4):
            math.cos(operand)
        elif (op == 5):
            math.pow(operand, 512)


# Prevent subprocess modules from executing this code block.
if __name__ == "__main__" and not os.path.exists("STRESS_TEST.exe.lock"):
    dur_time = float(input("How long do you want to run the stress test?\n> "))

    # Hacky lazy way to avoid using IPC and ensure the subprocesses know what to execute.
    file = open("STRESS_TEST.exe.lock", "w")
    file.close()

    cores = os.cpu_count()
    print("Your device has " + str(cores) + " CPU cores available.")

    # Prepare the stress threads.
    current_time = time.time()
    end_time = current_time + dur_time
    cores *= CORE_MULT  # Threads to spawn.
    mp.set_start_method("spawn")
    threads = []
    print("Creating " + str(cores) + " threads.")

    for core in range(0, cores):
        threads.append(Process(target=cpuburn, args=()))

    # Start the threads.
    print("Created " + str(cores * core_mult) + " threads.")
    print("Starting CPU stress threads.")

    for thread in threads:
        #print("Started " + thread.name)
        thread.start()

    # Stress time!
    print("Executing CPU stress threads.")
    time.sleep(dur_time)

    # Now get rid of the stress threads.
    if time.time() >= end_time:
        print("Stress test complete.")
        for thread in threads:
            thread.kill()

    # Get rid of the fake lock.
    os.unlink("STRESS_TEST.exe.lock")

# Pyinstaller threads ignore the launch arg, so the "lockfile" is used instead.
else:
    cpuburn()
