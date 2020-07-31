from time import sleep
from time_usage.time_usage import *


@time_usage
def test():
    sleep(2)
    return 1 + 1


test()
