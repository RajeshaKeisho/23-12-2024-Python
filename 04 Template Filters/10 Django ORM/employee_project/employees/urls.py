from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_employees, name='all_employees'),
    path('js/', views.js_department_employees, name='js_department_employees'),
    path('highest_salary/', views.highest_salary_employees, name='highest_salary_employees'),
    path('python/highest_salary/', views.py_dept_highest_salary_employees, name='py_dept_highest_salary_employees'),
    path('exclude_highest_salary/', views.exclude_highest_salary_employees, name='exclude_highest_salary_employees'),
    path('avg_salary/', views.avg_salary, name='avg_salary'),
    path('avg_salary_per_department/', views.avg_salary_per_department, name='avg_salary_per_department'),
    path('departments/num_employees/', views.num_employees_per_department, name='num_employees_per_department'),
    path('departments/most_employees/', views.dept_with_most_employees, name='dept_with_most_employees'),
    path('python_and_js/', views.py_and_js_employees, name='py_and_js_employees'),
    path('filter_salary_or_name/', views.salary_or_name_contains, name='salary_or_name_contains'),
    path('high_paid/', views.high_paid_employees, name='high_paid_employees'),
]