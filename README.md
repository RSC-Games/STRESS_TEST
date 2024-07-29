# STRESS_TEST
An open source torture test that works pretty well.

This stress test was designed to help overclockers and PC enthusiasts test their overclock stability and their new systems they got. Prime95 was and is still the golden standard, but this is a more tame test that fits in a couple kB of space.

Since the stress test was written in Python it is cross platform. However, to prevent problems with Python installations, it is compiled into binary files for each of the major operating systems. It is currently only available for Windows x86_64..

# Program Functionality
I decided to write a small easily-usable stress-test program that could easily be deployed across large amounts of systems and took minimal time to set up. While prime95 and other stress tools exist, they do not run on the Python interpreter. While they can force the CPU to run AVX operations and other x64-specific extensions, they didn't offer the portability and ease of testing I was looking for.

So I wrote this program. Its job, typical of stress-testing utilities, is to max out your processor's clock speed and utilization. Frequently this also coincides with large amounts of heat generation. I have used this to test RPi overclocks and cooler performance, and it has helped in resolving many of those issues. So if your laptop/desktop cooler does not function properly, this could give you some valuable insights without driving your temperatures as high as AVX512 often can.

This program works by spawning double the amount of processes that the processor can handle at once. They all do intense math (like 2 to the power of 256 and calculating the factorial of MAX_SIGNED_INT32). This way the load is maintained at max speeds without slight hiccups due to deciding what operation to do next. Afterward, the program throws away the result. This continues until the main thread kills the rest of the threads, which then of course the stress test is over.

# Use Cases

Torture testing is good for identifying stable overclocks (systems often lock up the second they reach their overclock speed if it not stable). This can be run on Raspberry Pis, x64 Desktops/Laptops and eventually Macs. It's also good for testing your cooling system and potentially identifying if your system is running way too hot without forcing your CPU to endure Prime95.

# Compiling instructions (Last tested with Python 3.9!)

**Windows 10/11**

If you don't already have Python, install the latest version from [python.org](url). Once the install is complete, open Windows Powershell run this command: 
_pip3 install pyinstaller_ 

Wait for it to install, then type this:
_cd C:\Users\user\Downloads_
_pyinstaller --onefile STRESS_TEST.py_

Now look in the dist folder in your current working directory and there is your executable. Feel free to do anything you want with it (except you must credit the original writers/maintainers).


**Linux (Debian based)**

You should already have Python installed on Debian. But, if you don't, then open bash and type this:
_sudo apt install python3_

Wait for it to finish, then enter this:
_pip3 install pyinstaller_

Then, type this:
_cd /home/<user>/Downloads_
_pyinstaller --onefile STRESS_TEST.py_

Now look in the dist folder. Alternatively, you could download the executable from the releases page.


**MacOS**

I don't know since I do not have any Apple hardware (except for a barely working MacBook Air 13 2013, which I don't care to set up).
