import datetime

def current_day():

    today = datetime.datetime.now().strftime("%A")
    print("Today is:", today)


current_day()