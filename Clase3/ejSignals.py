import signal
import time
import traceback

def handler(sig, frame):
    print("Signal Number:", sig, "Frame", frame)
    traceback.print_stack(frame)

signal.signal(signal.SIGINT, handler)

while True:
    print("press ctrl + c")
    time.sleep(10)