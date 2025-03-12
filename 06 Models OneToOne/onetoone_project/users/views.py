from django.shortcuts import render
from .models import User
# Create your views here.
def user_profile(request):
    users = User.objects.all()
    return render(request, 'users/user_profile.html', {'users':users})