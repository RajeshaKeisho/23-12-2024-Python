from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from django.contrib import messages

# Create your views here.

USERS = {
    'admin':'password123',
    'user':'user123',
}

def home(request):
    username = request.session.get('username', "Guest")
    theme = request.COOKIES.get('theme', 'light')
    last_activity = request.session.get('last_activity', "No activity Recorded")

    return render(request, 'home.html', {
        'username':username,
        'theme':theme,
        'last_activity':last_activity
    })


def set_cookie(request):
    response = HttpResponse('cookie has been set!')
    response.set_cookie('username', "Ganesh", max_age=60)
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', "Guest")
    return HttpResponse(f"Hello - {username}!")

def set_session(request):
    request.session['user_id'] = 123
    request.session['last-activity'] = str(timezone.now())
    return HttpResponse("Session has been set!")

def get_session(request):
    user_id = request.session.get("user_id", "Not Loggedin")
    last_activity = request.session.get('last_activity', "NO activity Recorded")
    return HttpResponse(f"User ID: {user_id} - Last Activity: {last_activity}")

def clear_session(request):
    request.session.flush()
    return HttpResponse("Session has been cleared!")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username in USERS and USERS[username] == password:
            request.session['username'] = username
            request.session['last_activity'] = str(timezone.now())
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out!")
    return redirect("home")

def set_theme(request):
    if request.method == "POST":
        theme = request.POSt.get('theme')
        response = redirect('home')
        response.set_cookie('theme', theme, max_age= 30 * 24 * 60 * 60)
        messages.success(request, f"The theme has been set to {theme}")
        return response
    return render(request, 'set_theme.html')

def protected_view(request):
    if 'username' not in request.session:
        messages.error(request, "You must be logged in!")
        return redirect('login')
    return HttpResponse("This is a protecte View. Only for LoggedIn Users")