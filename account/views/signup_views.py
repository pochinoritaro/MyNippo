from django.conf import settings
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from account.forms import SignUpForm
from account.models import User
from account.lib.ident_icon_generator import IdentIconGenerator


class SignUpView(TemplateView):
    """ ユーザー登録用ビュー """
    template_name = "account/signup-form.html"
    success_url = reverse_lazy("profile")
    
    def get_context_data(selfm, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SignUpForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        """フォームの送信を処理"""
        form = SignUpForm(request.POST)
        if form.is_valid():
            # ユーザーオブジェクトを保存するが、パスワードは保存せず
            user: User = form.save(commit=False)
            password = form.cleaned_data["password"]
            
            # パスワードをハッシュ化
            user.set_password(password)
            
            # ハッシュ化したパスワードでユーザーを保存
            user.save()
            ident_icon = IdentIconGenerator(user.id)
            image_io = ident_icon.generate_on_memory()
            # 生成したアイコンをユーザーに紐付けて保存
            user.icon.save(f"{user.id}_icon.png", image_io, save=True)
            user.save()
            
            # ログイン処理
            login(request, user)
            
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response({"form": form})

    def dispatch(self, request, *args, **kwargs):
        # ユーザーがログインしている場合、リダイレクト
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('task_list'))  # 任意のリダイレクト先
        return super().dispatch(request, *args, **kwargs)
