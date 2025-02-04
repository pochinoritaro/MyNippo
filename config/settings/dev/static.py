from config.settings.base import BASE_DIR


# メディアファイルの保存先
MEDIA_ROOT = BASE_DIR.joinpath("media")

# 静的ファイルパス
STATIC_URL = "/static/"
#メディアファイルパス
MEDIA_URL = "/media/"
