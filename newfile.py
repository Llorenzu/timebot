import datetime

def tell_time():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    print(f"The time is {time}")

tell_time()
