from io import BytesIO
import uuid
from PIL import Image
from .core.color import RGBGenerator
from .core.pattern import PatternGenerator


class IdentIconGenerator:
    def __init__(self, unique_uuid: uuid.UUID):
        """UUID からアイデンティコンを生成"""
        self._identicon_pattern = PatternGenerator(unique_uuid.hex[:15])
        self._color = RGBGenerator(unique_uuid.hex[25:])

    def generate_on_memory(self) -> BytesIO:
        """メモリ上にアイデンティコン画像を生成"""
        IMAGE_NEAREST = 0
        colored_pattern = self._identicon_pattern.apply_color(self._color.rgb)
        
        # 画像作成
        img = Image.fromarray(colored_pattern.astype("uint8"))
        img = img.resize((600, 600), resample=IMAGE_NEAREST)

        # メモリに保存
        img_io = BytesIO()
        img.save(img_io, "PNG")
        img_io.seek(0)
        
        return img_io


if __name__ == "__main__":
    ...
