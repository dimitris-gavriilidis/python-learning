'''
CS50P Week 1 - Meal Time
A program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.

HOURS:
| 12-hour | 24-hour |
|---------|---------|
| 12:00 a.m. | 0:00 |
| 1:00 a.m. | 1:00 |
| 2:00 a.m. | 2:00 |
| ... | ... |
| 11:00 a.m. | 11:00 |
| 12:00 p.m. | 12:00 |
| 1:00 p.m. | 13:00 |
| 2:00 p.m. | 14:00 |
| ... | ... |
| 11:00 p.m. | 23:00 |

The two edge cases that break naive logic:
- **12 a.m.** → 0 (not 12)
- **12 p.m.** → 12 (not 24)

Everything else is simple: a.m. = same, p.m. = +12. Now write it.

'''

def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    if converted_time >=7 and converted_time <=8:
        print("breakfast time")
    elif converted_time >=12 and converted_time <=13:
        print("lunch time")
    elif converted_time >= 18 and converted_time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    if len(minute) == 7:
        minute, am_pm = minute.split()
        minute = int(minute) / 60
        if am_pm == "a.m." and hour == 12:
            hour -= 12
        elif am_pm == "p.m." and hour != 12:
            hour += 12
    elif len(minute) == 2:
        minute = int(minute) / 60
    converted_time = hour + minute
    return converted_time


if __name__ == "__main__":
    main()