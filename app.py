import os
import time
import keyboard

def main():
    print("How many hours until shut-down?")
    usrInput = ""
    while True:
        usrInput = input("Time (Hour): ")
        if not usrInput.isdigit():
            print("Sorry, please enter a valid integer.")
            continue
        else:
            break

    usrTime = int(usrInput) * 3600
    
    for i in range(usrTime):
        remaining_seconds = usrTime - i
        hours = remaining_seconds // 3600
        minutes = (remaining_seconds % 3600) // 60
        seconds = remaining_seconds % 60
        print(f"Remaining time: {hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)
    
    print()
    
    keyboard.press('cmd+q')
    time.sleep(1)
    keyboard.release('cmd+q')
    print("Closed App")

if __name__ == "__main__":
    main()