import os
import time
import keyboard

def main():
    print("How many hours until shut-down?")
    usrTime = int(input("Time (Hour): ")) * 3600
    
    time.sleep(usrTime)
    
    keyboard.press('cmd+q')
    time.sleep(1)
    keyboard.release('cmd+q')
    print("Closed App")

if __name__ == "__main__":
    main()