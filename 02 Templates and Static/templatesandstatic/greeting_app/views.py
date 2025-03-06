from django.shortcuts import render
import datetime
# Create your views here.
def wish1(request):
    time = datetime.datetime.now()
    msg = "Hello friends, Very very good "
    h = int(time.strftime("%H"))
    if h < 12:
        msg += "norning!"
    elif h < 16:
        msg += "noon!"
    elif h < 21:
        msg += "Evening!"
    else:
        msg = "Hello guest, Good Night"
    my_dict = {'insert_time':time, "insert_data":msg}
    return render(request, 'wish1.html', context=my_dict)


def greet(request):
    now = datetime.datetime.now()
    current_time = now.strftime("%H %M %S")

    if now.hour < 12:
        greeting = "Good morning!"
    elif now.hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    return render(request, 'greet.html', {'greeting':greeting, 'current_time':current_time})
