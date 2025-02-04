class HSLConverter:
    """Color pattern から HSL 値を生成するクラス"""

    MAX_HUE = 360
    MAX_SATURATION = 65
    MAX_LUMINANCE = 75

    HUE_SCALE = MAX_HUE / 0x0FFF  # 0x0FFF (4095) を 360 にスケール
    SATURATION_SCALE = 20 / 0x00FF  # 255 を 20 にスケール
    LUMINANCE_SCALE = 20 / 0x00FF  # 255 を 20 にスケール

    @classmethod
    def from_pattern(cls, color_pattern: str):
        """color_pattern から H, S, L を取得"""
        hue = cls._calculate_hue(color_pattern[:3])
        saturation = cls._calculate_saturation(color_pattern[3:5])
        luminance = cls._calculate_luminance(color_pattern[5:7])
        return hue, saturation, luminance

    @classmethod
    def _calculate_hue(cls, hue_hex: str) -> float:
        """16進数の hue を 0-360 に変換"""
        return round(int(hue_hex, 16) * cls.HUE_SCALE)

    @classmethod
    def _calculate_saturation(cls, sat_hex: str) -> float:
        """16進数の saturation を 0-100 に変換"""
        return round(cls.MAX_SATURATION - int(sat_hex, 16) * cls.SATURATION_SCALE)

    @classmethod
    def _calculate_luminance(cls, lum_hex: str) -> float:
        """16進数の luminance を 0-100 に変換"""
        return round(cls.MAX_LUMINANCE - int(lum_hex, 16) * cls.LUMINANCE_SCALE)
