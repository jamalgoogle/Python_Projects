import time
import winsound

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("00:00")

    # Loop sound until user stops program
    while True:
        winsound.Beep(1000, 1000)  # 1 second beep
        time.sleep(0.5)

countdown(3)
