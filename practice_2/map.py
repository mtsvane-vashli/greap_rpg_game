import pygame
from pygame.locals import *
import sys
from pathlib import Path
from enum import Enum, auto
from constants import *

DIR_IMAGES = "images"
DIR_MAP_TEXTS = "maptext"

# FIELD_DATA_SPLITTER = ','  # Elements(map) of field data must be splitted by this.
# # Elements(mapChip) of map(not sheet) data must be one character.


class FieldEnum(Enum) :

    MAIN = auto()
    HOUSES = auto()

    def __init__(self, id) :
        self.id = id
    
    def to_str(self) -> str:
        """  Returns `str` for datafile (txt) name  """
        return super().__str__().lower()

    def to_datafile_name(self) -> str :
        return f"{DIR_MAP_TEXTS}/field_{self.to_str()}.txt"


class MapEnum(Enum) :

    NONE = (auto(), None, "-")
    """ Has no text file """

    TOWN_BEGIN_1 = (auto(), FieldEnum.MAIN, 'b')
    TOWN_BEGIN_2 = (auto(), FieldEnum.MAIN, 'd')

    TOWN_BEGIN_POST_1 = (auto(), FieldEnum.MAIN, 'p')
    TOWN_BEGIN_POST_2 = (auto(), FieldEnum.MAIN, 'q')


    def __init__(self, id, fieldEnum: FieldEnum, symbol: str) :
        self.id = id
        self.fieldEnum = fieldEnum
        self.symbol = symbol
        
    # TODO: これは Field とかで記述しようか
    # def set_mapEnums_dict(self) -> None :
    #     if not len(self.mapEnums_dict) :
    #         self.mapEnums_dict = {fieldEnum : [mapEnum for mapEnum in MapEnum if mapEnum.fieldEnum != None] for fieldEnum in FieldEnum}

    def to_str(self) -> str :
        """  Returns `str` for datafile (image, text) name  """
        return super().__str__().lower()
    
    def to_datafile_name(self) -> dict[str, str] :
        return {"":"",
                "flagobject": f"{DIR_MAP_TEXTS}/{self.get_fieldEnum().to_str()}_flagobject_{self.to_str()}.txt",
                "mapsheet": f"{DIR_IMAGES}/{self.get_fieldEnum().to_str()}_mapsheet_{self.to_str()}.png",
                "collision": f"{DIR_MAP_TEXTS}/{self.get_fieldEnum().to_str()}_collision_{self.to_str()}.txt"}



class CollisionTypeEnum(Enum) :

    ENTERABLE = (auto(), '0')
    TALKABLE  = (auto(), '2')
    NOT_ENTERABLE = (auto(), '1')

    def __init__(self, id, symbol: str) :
        self.id = id
        self.symbol = symbol
    

class WarpPointEnum(Enum) :

    TO_HOUSE_PLAYER   = (auto(), 'h', `mapEnum`, (SCREEN_RECT.width / 2 - (PLAYER_WIDTH / 2), SCREEN_HEIGHT / 2 - (PLAYER_HEIGHT / 2)), DIRECTION_UP)
    FROM_HOUSE_PLAYER = (auto(), 'H', `mmmmmmm`, (MAP_CHIP_SIZE * 20, MAP_CHIP_SIZE * 10), DIRECTION_DOWN)

    def __init__(self, id, symbol: str, mapEnum: MapEnum, position: tuple[int, int], direction: int) :
        self.id = id
        self.symbol = symbol
        self.mapEnum = mapEnum
        self.position = position
        self.direction = direction


class FlagObjectTypeEnum(Enum) :

    ITEM_SIGN = auto()

    def to_str(self) -> str:
        return super().__str__().lower()

    def to_datafile_name(self) -> str :
        return f"{DIR_IMAGES}/flagged_{self.to_str()}"


class FlagObjectEnum(Enum) :

    ITEM_SIGN_1 = (auto(), 's', "倒れた看板１", FlagObjectTypeEnum.ITEM_SIGN)

    def __init__(self, id, symbol: str, name: str, flagObjectTypeEnum: FlagObjectTypeEnum) :
        self.id = id
        self.symbol = symbol
        self.name = name
        self.flagObjectTypeEnum = flagObjectTypeEnum
        
    
class 


