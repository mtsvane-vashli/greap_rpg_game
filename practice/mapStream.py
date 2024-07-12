

CHAR_GRASS = 'g'
CHAR_WATER = 'w'

MAP_IMAGE = {CHAR_GRASS: 'G',  # 'G' は画像の代わり
             CHAR_WATER: 'W'}
IMAGE_NUM = len(MAP_IMAGE)

# main
ROW = 5
COL = 10
map = [[" " for i in range(COL)] for i in range(ROW)]


with open("C:/Users/subsu/Documents/GLEAP/hackathon_2024_team_f/greap_rpg_game/practice/map.txt") as file :
    
    # print(file.read())  # After reading, the cursor remain at end position.
    print()
    lis_map = file.read().split('\n')

    for row in range(ROW) :
        for col in range(COL) :
            print(end=MAP_IMAGE[map[row][col]])
        print()
