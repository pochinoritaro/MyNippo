from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import TemplateView
from task.forms import CreateTaskForm
from task.models import Task


class CreateTaskView(LoginRequiredMixin, TemplateView):
    """ ユーザー登録用ビュー """
    template_name = "task/create-task.html"
    #success_url = reverse_lazy("signup")
    
    def get_context_data(selfm, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CreateTaskForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        """フォームの送信を処理"""
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            print("Members:", [user.id for user in form.cleaned_data.get("members")])
            task: CreateTaskForm = form.save(commit=False)  # 一旦コミットせずに保存
            task.author = request.user  # 現在のユーザーを設定
            task.save()  # Taskを保存
            form.save_m2m()  # 多対多のフィールドを保存
            return redirect("task_list")  # 適切なリダイレクト先に変更

        return self.render_to_response({"form": form})