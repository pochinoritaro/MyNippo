from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView
from task.models import Task

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task-detail.html'
    context_object_name = 'task'
