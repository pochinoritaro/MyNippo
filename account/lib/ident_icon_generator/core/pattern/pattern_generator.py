import numpy as np


class PatternGenerator:
    PATTERN_WIDTH = 5
    PATTERN_HEIGHT = 3

    def __init__(self, hex_pattern: str):
        """16進数の文字列からパターンを生成"""
        self.pattern = self._create_pattern(hex_pattern)

    def _create_pattern(self, hex_pattern: str) -> np.ndarray:
        """16進数の文字列を基に2次元のパターンを作成"""
        binary_pattern = np.array(
            [(1 if int(x, 16) % 2 == 0 else 0) for x in hex_pattern]
        ).reshape(self.PATTERN_HEIGHT, self.PATTERN_WIDTH)

        # 左右対称にミラーリング
        mirrored_pattern = self._mirror_pattern(binary_pattern)

        # 90度回転して最終パターンを作成
        return np.rot90(mirrored_pattern, 3)

    def _mirror_pattern(self, pattern: np.ndarray) -> np.ndarray:
        """左右対称のミラーリングを行う"""
        return pattern[[2, 1, 0, 1, 2]]

    def apply_color(self, rgb_pattern: list) -> np.ndarray:
        """パターンにRGBカラーを適用した配列を返す"""
        WHITE_RGB = [255, 255, 255]
        color_pattern = np.zeros((*self.pattern.shape, 3), dtype=int)
        color_pattern[self.pattern == 0] = WHITE_RGB
        color_pattern[self.pattern == 1] = rgb_pattern
        return color_pattern
