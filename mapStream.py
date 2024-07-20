import pygame
from pathlib import Path
from enum import Enum, auto

CURRENT_DIR = Path(__file__).parent



DIC_NPC = {' ': pygame.image.load()}

class CollisionEnum(Enum) :

    ENTERABLE = (auto(), ' ')

    def __init__(self, id, symbol: str) :
        self.id = id
        self.symbol = symbol



def load_text_file(relative_path_name: str) -> list[list[str]] :
    """  テキストファイルから、1文字の`str`の2次元`listを生成`  """

    with open(Path(CURRENT_DIR, relative_path_name)) as file :
        temp_list = file.readlines()
        return [[temp_list[row][col] for col in range(len(temp_list[0]))] for row in range(len(temp_list))].copy()
    