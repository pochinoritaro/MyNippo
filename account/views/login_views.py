from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from account.forms import LoginForm
from account.models import User


class LoginView(TemplateView):
    """ ユーザー登録用ビュー """
    template_name = "account/login-form.html"
    success_url = reverse_lazy("profile")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        """フォームの送信を処理"""
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email: str = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:
                username = User.objects.get(email=user_email.lower()).username

            except User.DoesNotExist:
                messages.error(request, "ユーザーが存在しません。")
                return HttpResponseRedirect(reverse_lazy("signup"))
            
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    print("passed")
                
                    return HttpResponseRedirect(self.success_url)
                
                else:
                    return self.render_to_response({"form": form})

        else:
            return self.render_to_response({"form": form})
