from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.views.generic import ListView
from task.models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task-list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        # ログイン中のユーザーが作成者、レビュワー、またはメンバーとして関連するタスクを取得
        user = self.request.user
        queryset = Task.objects.filter(
            models.Q(is_public=True) |  # 公開タスク
            (models.Q(is_public=False) & (models.Q(author=user) | models.Q(reviewer=user) | models.Q(members=user)))  # 非公開タスクで作成者、レビュワー、メンバーの場合
        )
        return queryset.distinct()
