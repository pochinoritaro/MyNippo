"""
共通設定ファイル

環境依存の設定は下記のフォルダに追加および追記し、本ファイルにはプロジェクト共通の設定のみ記入してください。
・/local/settings.py
・/dev/settings.py
・/prod/settings.py
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 秘密鍵
# TODO: 生成した秘密鍵を環境変数から読み込む形に修正する
SECRET_KEY = "django-insecure-vm3y=nsigr_5bm8^3k2!7w)f#n6kz#=$eyi_nnrw9t1d+5ry0i"

# 接続を許可するIPアドレスorドメイン
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split() if os.environ.get("ALLOWED_HOSTS") is not None else [] 

# インストールアプリ
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_bootstrap5",
    "account",
    "task",
    "nippo",
]

# ミドルウェア
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ルートのurls.py
ROOT_URLCONF = "config.urls"

# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} {name}: {message}",
            "style": "{",
        },
    },
}

# テンプレートエンジン設定
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            Path(BASE_DIR, "templates")
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# パスワードバリデーション
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# 言語設定
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

# デフォルトPK設定
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 認証に使用するユーザモデル
AUTH_USER_MODEL = "account.User"

# 認証バックエンド
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

# ログイン用URL
LOGIN_URL = "/account/login/"
# ログアウト後、リダイレクトURL
LOGOUT_REDIRECT_URL = LOGIN_URL
