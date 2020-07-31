# time_usage
A small python script to measure the time needed for a block of code to complete

code example:

###\#python
from time import sleep

@time_usage\
def function():\
    &emsp;sleep(2)\
    &emsp;return 1 + 1

function()

\# prints: elapsed time: 2.000295