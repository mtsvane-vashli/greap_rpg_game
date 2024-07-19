from pathlib import Path
import os

CHAR_GRASS = 'g'
CHAR_WATER = 'w'
CHAR_DEFAULT = ' '

MAP_IMAGE = {CHAR_GRASS : 'G',  # 'G' は画像の代わり
             CHAR_WATER : 'W',
             CHAR_DEFAULT : ' '}
IMAGE_NUM = len(MAP_IMAGE)

# main
ROW = 5
COL = 10
map = [[" " for _ in range(COL)] for _ in range(ROW)]



file_path = Path(Path(__file__).parent, "map.txt")
with open(file_path) as file :
    
    # print(file.read())  # After reading, the cursor remain at end position.
    # print()
    map = file.readlines()

    for row in range(ROW) :
        for col in range(COL) :
            print(end=MAP_IMAGE[map[row][col]])
        print()


string ="STRING"
print(string[2][0][0][0][0])

print([string[i] for i in range(len(string))])

print([[map[row][col] for col in range(COL)] for row in range(ROW)])

print(Path(__file__))