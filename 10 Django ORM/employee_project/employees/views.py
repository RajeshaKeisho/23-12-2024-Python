from django.shortcuts import render
from django.db.models import Avg, Count 
from django.db.models import Q 
from .models import Employee, Department 
from django.db import connection
 
# View to fetch all employees
def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/all.html', {'employees': employees})

# View to fetch employees in the JavaScript department
def js_department_employees(request):
    js_employees = Employee.objects.filter(department__name="Javascript")
    return render(request, 'employees/js_employees.html', {'js_employees': js_employees})

# View to fetch employees with a salary greater than 50,000
def highest_salary_employees(request):
    highest_salary_employees = Employee.objects.filter(salary__gt=50000)
    return render(request, 'employees/highest_salary_employees.html', {'highest_salary_employees': highest_salary_employees})

# View to fetch employees in the Python department with a salary >= 50,000
def py_dept_highest_salary_employees(request):
    py_dept_highest_salary_employees = Employee.objects.filter(department__name="Python", salary__gte=50000)
    return render(request, 'employees/py_dept_highest_salary_employees.html', {'py_dept_highest_salary_employees': py_dept_highest_salary_employees})

# View to exclude employees with a salary >= 60,000
def exclude_highest_salary_employees(request):
    exclude_highest_salary_employees = Employee.objects.exclude(salary__gte=60000)
    return render(request, 'employees/exclude_highest_salary_employees.html', {'exclude_highest_salary_employees': exclude_highest_salary_employees})

# View to get the average salary of all employees
def avg_salary(request):
    avg_salary = Employee.objects.aggregate(avg_salary=Avg('salary'))
    return render(request, 'employees/avg_salary.html', {'avg_salary': avg_salary})

# View to get the average salary per department
def avg_salary_per_department(request):
    departments = Department.objects.annotate(avg_salary=Avg('employee__salary'))
    return render(request, 'employees/avg_salary_per_department.html', {'departments': departments})

# View to count employees in each department
def num_employees_per_department(request):
    departments = Department.objects.annotate(num_employees=Count('employee'))
    return render(request, 'employees/num_employees_per_department.html', {'departments': departments})

# View to find the department with the most employees
def dept_with_most_employees(request):
    department = Department.objects.annotate(num_employees=Count('employee')).order_by('-num_employees').first()
    return render(request, 'employees/dept_with_most_employees.html', {'department': department})

# View to find employees in both Python and JavaScript departments
def py_and_js_employees(request):
    employees = Employee.objects.filter(department__name__in=["Python", "Javascript"])
    return render(request, 'employees/py_and_js_employees.html', {'employees': employees})

# View to filter employees with a name containing "Python" or salary >= 60,000
def salary_or_name_contains(request):
    employees = Employee.objects.filter(Q(name__icontains="Python") | Q(salary__gte=60000))
    return render(request, 'employees/employees_list.html', {'employees': employees})

# View to fetch employees earning more than 60,000 using raw SQL
def high_paid_employees(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, salary, department_id FROM employees_employee WHERE salary > 60000")
        employees = cursor.fetchall()

    employee_objects = [Employee(id=row[0], name=row[1], salary=row[2], department_id=row[3]) for row in employees]
    return render(request, 'employees/employees_list.html', {'employees': employee_objects})