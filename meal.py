def main():
    user_time = convert(input("What time is it? "))

    if user_time >= 7 and user_time <= 8:
        print("Breakfast time")
    elif user_time >= 12 and user_time <= 13:
        print("Lunch time")
    elif user_time >= 18 and user_time <= 19:
        print("Dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    time = hours + minutes
    return time

if __name__ == "__main__":
    main()

