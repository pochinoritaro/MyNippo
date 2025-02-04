import logging
from django.views.generic import TemplateView

logger = logging.getLogger("account.profile")

class ProfileView(TemplateView):
    """ ユーザー登録用ビュー """
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        logger.debug(f"{self.__class__.__name__}の処理を開始します")
        context = super().get_context_data(**kwargs)
        logger.debug(f"コンテキストデータ\n\t{context}")
        context["profile"] = self.request.user
        logger.debug(f"プロフィールデータ挿入後のコンテキストデータ\n\t{context}")
        return context
