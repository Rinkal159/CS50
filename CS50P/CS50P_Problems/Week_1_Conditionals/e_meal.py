def main():
    time = input("What time is it? ")
    timeInFloat = convert(time)

    if( timeInFloat >= 7 and timeInFloat <= 8):
        print("breakfast time")
    elif ( timeInFloat >= 12 and timeInFloat <= 13):
        print("lunch time")
    elif ( timeInFloat >= 18 and timeInFloat <= 19):
        print("dinner time")


def convert(time):
    hour = time[0 : time.find(":")]
    minute = time[time.find(":") + 1 : ]
    
    return int(hour) + int(minute)/60


if __name__ == "__main__":
    main()