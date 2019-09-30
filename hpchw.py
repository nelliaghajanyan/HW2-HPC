import os
import shutil
# import shutil module that offers many operations on files and collections of files, like#
# manipulating the filesystem, making archives and etc.
import time
# to keep track of execution times
from concurrent.futures import ThreadPoolExecutor
# to provide a high-level interface for asynchronously executing callables
# The asynchronous execution can be performed with threads, using ThreadPoolExecutor, 
from concurrent.futures import ProcessPoolExecutor
# or separate processes, using ProcessPoolExecutor.
# Both implement the same interface, which is defined by the abstract Executor class.
# (took from docs.python.org)


# 1. 
# fix current time
currentTime1 = time.time()
# inspect where are you
#os.getcwd()
# change directory
#cd C:\Users\aghajanyann\Desktop
# copytree recursively copies an entire directory tree, and importantly, the destination # #directory, must not already exist; it will be created
shutil.copytree("./oneDirectory","./anotherDirectory")
# calculate the time required to execute this task
print("Without threading: ", time.time() - currentTime1)

# Result: This python script copies all files from one directory to another one, without threading


# 2.
# fix current time
currentTime2 = time.time()
# instance of ThreadPoolExecutor that has 3 concurrent threads 
executor = ThreadPoolExecutor(5)
# move files from one directory to another
executor.submit(shutil.copytree("./oneDirectory",'./otherDirectory'))
# calculate the time required to execute 2nd task
print("With threading: ", time.time() - currentTime2)


#3.
# fix current time
currentTime3 = time.time()
# instance of ProcessPoolExecutor that has 3 concurrent threads
executor1 = ProcessPoolExecutor(5)
# move files from one directory to another
executor1.submit(shutil.copytree("./oneDirectory",'./oneOtherDirectory'))
# calculate the time required to execute 3rd task
print("With processing", time.time()-currentTime3)
