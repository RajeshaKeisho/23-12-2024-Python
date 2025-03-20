from django.urls import path
from .views import task_list_create, update_task, delete_task, TaskListCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", task_list_create, name="task_list"),
    path("update/<int:pk>/", update_task, name="task_update"),
    path("delete/<int:pk>/", delete_task, name="task_delete"),

    path('cbv/', TaskListCreateView.as_view(), name="cbv_task_list"),
    path('cbv/update/<int:pk>/', TaskUpdateView.as_view(), name="cbv_task_update"),
    path('cbv/delete/<int:pk>/', TaskDeleteView.as_view(), name="cbv_task_delete"),

]