import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        m, s = divmod(seconds, 60)
        timer = f'{m:02d}:{s:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

print("Time's up!")
