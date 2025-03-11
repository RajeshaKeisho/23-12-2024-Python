from django.shortcuts import render
from .models import Employee
# Create your views here.

def employee_view(request):
    emp_data = Employee.objects.all()
    my_dict = {'emp_data':emp_data}
    return render(request, 'home.html', context=my_dict)