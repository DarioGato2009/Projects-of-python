import os
from logging import shutdown
import time
a = 10
print("Deleting SYSTEM 32...",(a))
time.sleep(1)
while True == True:
    a = a - 1
    print("Deleting SYSTEM 32...",(a))
    time.sleep(1)
    if a <= 1:
        print("Goodbye:)")
        time.sleep(1)
        os.system("shutdown/p")
        break