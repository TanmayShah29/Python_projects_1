from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"  # fixed here

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        print(CLEAR + CLEAR_AND_RETURN, end='')  # clear and reset cursor

        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")

minutes=int(input("Enter the minutes for the alarm "))
seconds=int(input("Enter the seconds for the alarm "))
total_seconds=minutes*60 + seconds
alarm(total_seconds)
