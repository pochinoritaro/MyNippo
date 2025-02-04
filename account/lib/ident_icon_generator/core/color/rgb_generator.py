import colorsys
import math
from .hsl_converter import HSLConverter


class RGBGenerator:
    def __init__(self, color_pattern: str):
        hue, saturation, luminance = HSLConverter.from_pattern(color_pattern)

        # HLS を RGB に変換
        icon_rgb = colorsys.hls_to_rgb(
            h=hue / 360,
            l=luminance / 100,
            s=saturation / 100,
        )

        # RGB の 0-255 変換
        self.rgb = [math.floor(c * 255) for c in icon_rgb]
        self.red, self.green, self.blue = self.rgb
