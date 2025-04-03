import os
import time

def shutdown():
    print("Shutting down in 10 seconds...")
    time.sleep(10)
    os.system("shutdown /s /t 1 ")

shutdown()