import logging
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from account.forms import LoginForm
from account.models import User

logger = logging.getLogger("account.login")

class LoginView(TemplateView):
    """ ユーザー登録用ビュー """
    template_name = "account/login-form.html"
    success_url = reverse_lazy("profile")
    
    def get_context_data(self, **kwargs):
        logger.debug(f"{self.__class__.__name__}の処理を開始します")
        context = super().get_context_data(**kwargs)
        logger.debug(f"コンテキストデータ\n\t{context}")
        context["form"] = LoginForm()
        logger.debug(f"フォームデータ挿入後のコンテキストデータ\n\t{context}")
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        logger.info("ログイン処理開始")
        """フォームの送信を処理"""
        form = LoginForm(request.POST)

        if form.is_valid():
            logger.info("ログインフォームバリデーション成功")
            user_email: str = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:
                logger.info("ログインフォーム情報からユーザ名を取得")
                username = User.objects.get(email=user_email.lower()).username

            except User.DoesNotExist as e:
                logger.exception(f"ユーザが存在しません\n{e}")
                messages.error(request, "ユーザーが存在しません。")
                return HttpResponseRedirect(reverse_lazy("signup"))
            
            else:
                logger.info("ユーザ認証処理を開始します")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    logger.info("ユーザ認証が成功しました")
                    logger.debug(f"承認されたユーザ: {user}")
                    login(request, user)
                    logger.info("ログインが完了しました")
                
                    return HttpResponseRedirect(self.success_url)
                
                else:
                    logger.info("ユーザ認証が失敗しました")
                    return self.render_to_response({"form": form})

        else:
            logger.info("ユーザ登録フォームバリデーションが失敗しました")
            return self.render_to_response({"form": form})
