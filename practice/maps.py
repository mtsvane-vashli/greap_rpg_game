import pygame
from pygame.locals import *
import sys
from pathlib import Path
from enum import Enum, auto
from constants import Constants as Con

DIR_MAP_CHIPS = "images"
DIR_FIELD_TEXTS = "mapdata"
DIR_MAP_TEXTS = "mapdata"

FIELD_DATA_SPLITTER = ','  # Elements(map) of field data must be splitted by this.
# Elements(mapChip) of map data must be one character.


class MapChipEnum(Enum) :

    TRANSPARENT = (auto(), ' ')
    """ Has no image file """

    GRASS = (auto(), 'g')
    WATER = (auto(), 'w')


    def __init__(self, id, symbol: str) :
        self.id = id
        self.symbol = symbol

    def to_str(self) -> str :
        """  Returns `str` for datafile (image) name  """
        return super().__str__().lower()
    
    def to_datafile_name(self) -> str :
        return f"{DIR_MAP_CHIPS}/mapchip_{self.to_str()}.png"


class FieldEnum(Enum) :

    FIELD_MAIN = auto()


    def __init__(self, id) :
        self.id = id
    
    def to_str(self) -> str :
        """  Returns `str` for datafile (txt) name  """
        return super().__str__().removeprefix("FIELD_").lower()
    
    def to_datafile_name(self) -> str :
        return f"{DIR_FIELD_TEXTS}/field_{self.to_str()}.txt"


class MapEnum(Enum) :

    MAP_NONE = (auto(), None, "none")
    """ Has no text file """

    # MAP_TOWN_BEGIN = (auto(), FieldEnum.FIELD_MAIN, "tnbg")


    def __init__(self, id, fieldEnum: FieldEnum, symbol: str) :
        self.id = id
        self.fieldEnum = fieldEnum
        self.symbol = symbol
        
    # def set_mapEnums_dict(self) -> None :
    #     if not len(self.mapEnums_dict) :
    #         self.mapEnums_dict = {fieldEnum : [mapEnum for mapEnum in MapEnum if mapEnum.fieldEnum != None] for fieldEnum in FieldEnum}

    def to_str(self) -> str :
        """  Returns `str` for datafile (txt) name  """
        return super().__str__().removeprefix("MAP_").lower()
    
    def to_datafile_name(self) -> str :
        return f"{DIR_MAP_TEXTS}/{self.get_fieldEnum().to_str()}_map_{self.to_str()}.txt"

    

class MapChips :

    CHIP_SIZE = Con.MAP_CHIP_SIZE

    is_images_loaded = False

    
    def __new__(cls) :
        """  For singleton implementation. Constructs sole instance
            and loads images only once.  """

        if not hasattr(cls, "_instance") :
            cls._instance = super(cls).__new__(cls)
            cls.load_images()

        return cls._instance


    def __init__(self) :
        pass

    # def get_image_dict(self) -> dict[MapChipEnum, pygame.Surface] :
    #     return self.image_dict.copy()
 

    def load_images(self) -> None :
        """  This will be called only once in the constructor. Do not call this in the others.  """

        # Prevents from loading more than once.
        if self.is_images_loaded : return

        self.image_dict = {mapChipEnum : self.load_image(mapChipEnum) for mapChipEnum in MapChipEnum}
        self.is_images_loaded = True


    def load_image(self, mapChipEnum: MapChipEnum) -> pygame.Surface :
        """  \* Private method: do not call this outside.  """

        if mapChipEnum == MapChipEnum.TRANSPARENT :
            surface = pygame.Surface((self.CHIP_SIZE, self.CHIP_SIZE), flags=SRCALPHA)
            surface.fill(0)  # Transparent color
            return surface

        else :
            return pygame.image.load(mapChipEnum.to_datafile_name()).convert()



class Map :

    MAP_ROW = Con.MAP_LIST_ROW
    MAP_COL = Con.MAP_LIST_COL

    # is_images_loaded = False

    def __init__(self, mapEnum: MapEnum) :
        
        self.mapEnum = mapEnum  # TODO: What member needs?

        self.load_text()

    
    def load_text(self) -> None :
        """  This will be called only once in the constructor. Do not call this in the others.  """

        if self.mapEnum == MapEnum.MAP_NONE :
            self.map_list = None

        else :
            # self.map_list = [[MapChipEnum.TRANSPARENT.get_char() for _ in range(self.MAP_COL)] for _ in range(self.MAP_ROW)]
            file_path = Path(self.mapEnum.to_datafile_name())

            with open(file_path) as file :
                temp_list = file.readlines()
                self.map_list = [[temp_list[row][col] for col in range(self.MAP_COL)] for row in range(self.MAP_ROW)]


    def draw(self, ) -> None : ...
    # TODO: image_dict が欲しいがどう入手するか？: 引数に `mapChips` or `.get_image_dict` or メンバに `mapChips`




class Field :

    def __init__(self, fieldEnum: FieldEnum, current_mapEnum: MapEnum) :
        
        self.fieldEnum = fieldEnum
        self.current_mapEnum = current_mapEnum

        self.mapEnums = [mapEnum for mapEnum in MapEnum
                         if mapEnum.fieldEnum == self.fieldEnum or mapEnum.fieldEnum == None]
        self.maps = [Map(mapEnum) for mapEnum in self.mapEnums]


    def load_text(self) -> None :
        """  Call this only once.  """

        file_path = Path(self.fieldEnum.to_datafile_name())

        with open(file_path) as file :
            lines = file.readlines()
            temp_list = [line.rstrip(FIELD_DATA_SPLITTER).split(FIELD_DATA_SPLITTER) for line in lines]

            self.field_list = [[temp_list[row][col] for col in range(len(temp_list[0]))] for row in range(len(temp_list))]
            # TODO: self.field_list の型: list[list[Map]]


    def map_transition(self) -> bool : ...




# TODO: deprecated: Implements method like this in Field and Map
def load_text_map(mapEnum : MapEnum | FieldEnum) -> list[list[str]] :

    map = [[' ' for i in range(MAP_COL)] for i in range(MAP_ROW)]

    file_path = Path(Path(__file__).parent, "data", f"")

    with open(file_path) as file :
        temp_map = file.readlines()
        map = [[temp_map[row][col] for col in range(MAP_COL)] for row in range(MAP_ROW)]
    
    return map
