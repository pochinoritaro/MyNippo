from django.views.generic import TemplateView

class ProfileView(TemplateView):
    """ ユーザー登録用ビュー """
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user
        return context
