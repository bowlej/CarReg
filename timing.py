import time

def doathing():
    start = time.time()
    doasum = 100 + 100
    time.sleep(1.4)
    print(doasum)
    stop = time.time()
    print(stop)
    timetaken = (time.time() - start)
    rounded = (round(timetaken))
    rounded = str(rounded)
    print(rounded + 's')
    """justwholeseconds = rounded.replace(".0")"""

    """timetaken = print("%s" % (time.time() - start))"""

