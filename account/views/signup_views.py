import logging
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from account.forms import SignUpForm
from account.models import User
from account.lib.ident_icon_generator import IdentIconGenerator

logger = logging.getLogger("account.signup")

class SignUpView(TemplateView):
    """ ユーザー登録用ビュー """
    template_name = "account/signup-form.html"
    success_url = reverse_lazy("profile")
    
    def get_context_data(self, **kwargs):
        logger.debug(f"{self.__class__.__name__}の処理を開始します")
        context = super().get_context_data(**kwargs)
        logger.debug(f"コンテキストデータ\n\t{context}")
        context["form"] = SignUpForm()
        logger.debug(f"フォームデータ挿入後のコンテキストデータ\n\t{context}")
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        """フォームの送信を処理"""
        logger.info("ユーザ登録処理開始")
        form = SignUpForm(request.POST)

        if form.is_valid():
            logger.info("ユーザ登録フォームバリデーションが成功しました")
            # ユーザーオブジェクトを保存するが、パスワードは保存せず
            user: User = form.save(commit=False)
            password = form.cleaned_data["password"]
            
            # パスワードをハッシュ化
            user.set_password(password)
            
            # ハッシュ化したパスワードでユーザーを保存
            user.save()
            logger.debug("ユーザ情報が登録されました")

            logger.info("ユーザアイコン自動生成開始")
            ident_icon = IdentIconGenerator(user.id)
            image_io = ident_icon.generate_on_memory()
            logger.info("ユーザアイコン生成完了")

            # 生成したアイコンをユーザーに紐付けて保存
            user.icon.save(f"{user.id}_icon.png", image_io, save=True)
            logger.info("ユーザテーブルにアイコンを保存")
            user.save()
            logger.debug("ユーザ情報が更新されました")

            # ログイン処理
            logger.info("新規作成されたユーザでログイン")
            login(request, user)
            logger.info("ログインが完了しました")
            return HttpResponseRedirect(self.success_url)
        else:
            logger.info("ユーザ登録フォームバリデーションが失敗しました")
            return self.render_to_response({"form": form})


    def dispatch(self, request, *args, **kwargs):
        # ユーザーがログインしている場合、リダイレクト
        if request.user.is_authenticated:
            logger.info("既にログイン済のユーザです")
            return HttpResponseRedirect(reverse('task_list'))
        return super().dispatch(request, *args, **kwargs)
