# STRESS_TEST
An open source torture test that works pretty well.

This stress test was designed to help overclockers and PC enthusiasts test their overclock stability and their new systems they got. 

Since the stress test was written in Python it is cross platform. However, to prevent problems with Python installations, it is compiled into binary files for each of the major Operating Systems and Instruction Set Architectures. It is currently only available for Windows x86_64, and soon for Linux x86_64/ARM64.

# Program Functionality
One day I was bored and I had Python open. I was running sync operations for a local disk to a network drive, and noticed that the fan was getting louder. I also remembered that quite a few stress test programs require administrator install. I was not using my personal laptop, so an install was impossible (no employer is going to let you install a stress test so that you can make their laptop/desktop burn up).

So then I started writing this program. Its job is to max out your processor's clock speed and utilization. Frequently this also coincides with large amounts of heat generation. So if your laptop/desktop cooler does not function properly, this could give you some insight into that.

This program works by spawning double the amount of processes that the processor can handle at once. They all do intense math (like 2 to the power of 256 and calculating the factorial of MAX_SIGNED_INT32). This way the load is maintained at max speeds without slight hiccups due to deciding what operation to do next. Afterward, the program throws away the result. This continues until the main thread kills the rest of the threads, which then of course the stress test is over.

# Use Cases

Torture testing is good for identifying stable overclocks (systems often lock up the second they reach their overclock speed if it not stable). This can be run on Raspberry Pis, x64 Desktops/Laptops and eventually Macs (though whether you can overclock a Mac is unknown to me). It's also good for cooling tests, so if you think you have cooling problems, run this. It should help you identify and possibly fix the problem.

# Compiling instructions 

**Windows (NT 10.0)**

If you don't already have Python, install the latest version from [python.org](url). Once the install is complete, open Windows Powershell run this command: 
_pip3 install pyinstaller_ 

Wait for it to install, then type this:
_cd C:\Users\user\Downloads_
_pyinstaller --onefile STRESS_TEST.py_

Now look in the dist folder in your current working directory and there is your executable. Feel free to do anything you want with it (except you must credit the original writers/maintainers).


**Linux (Debian based)**

You should already have Python installed on Debian. But, if you don't, then open bash and type this:
_sudo apt-get install python3_

Wait for it to finish, then enter this:
_pip3 install pyinstaller_

Then, type this:
_cd /home/user/Downloads_
_pyinstaller --onefile STRESS_TEST.py_

Now look in the dist folder. Alternatively, you could download the executable from the releases page.
