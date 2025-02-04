from django.urls import path
from task.views import CreateTaskView, TaskDetailView, TaskListView

urlpatterns = [
    path("create/", CreateTaskView.as_view(), name="task_create"),
    path("", TaskListView.as_view(), name="task_list"),
    path("<str:pk>", TaskDetailView.as_view(), name="task_detail")
]
