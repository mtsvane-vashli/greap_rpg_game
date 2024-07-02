# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

# 画面サイズの設定
SCR_RECT = Rect(0, 0, 1280, 740)

# キャラクターの1フレームのサイズ (幅, 高さ)
CHARACTER_SIZE = (31, 32)

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# マップのクラス
class Map:
    # マップデータ
    map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
    def __init__(self):
        self.row, self.col = len(self.map), len(self.map[0])  # マップの行数,列数を取得
        self.imgs = [None] * 256  # マップチップ
        self.msize = 32  # 1マスの大きさ[px]

        # マップの画像をロード
        self.imgs[0] = load_img("assets/grass.png")  # 草地
        self.imgs[1] = load_img("assets/water.png")  # 水
    
    def draw(self, screen):
        for i in range(self.row):
            for j in range(self.col):
                screen.blit(self.imgs[self.map[i][j]], (j * self.msize, i * self.msize))

# キャラクターのクラス
class Character:
    def __init__(self, image, position):
        self.sheet = pygame.image.load(image).convert_alpha()
        self.rect = Rect(0, 0, CHARACTER_SIZE[0], CHARACTER_SIZE[1])
        self.rect.topleft = position
        self.frame = 0
        self.direction = 0
        self.animcycle = 24
        self.image = self.get_image()

    def update(self, direction):
        if direction is not None:
            self.direction = direction
            self.frame += 1
            self.frame %= self.animcycle
            self.image = self.get_image()

    def get_image(self):
        x = (self.frame // (self.animcycle // 3)) * CHARACTER_SIZE[0]
        y = self.direction * CHARACTER_SIZE[1]
        return self.sheet.subsurface(Rect(x, y, CHARACTER_SIZE[0], CHARACTER_SIZE[1]))

    def move(self, dx, dy, current_map):
        old_rect = self.rect.copy()
        new_rect = self.rect.move(dx, dy)

        if 0 <= new_rect.left // current_map.msize < current_map.col and 0 <= new_rect.top // current_map.msize < current_map.row:
            if current_map.map[new_rect.bottom // current_map.msize][new_rect.left // current_map.msize] != 1 and \
               current_map.map[new_rect.bottom // current_map.msize][new_rect.right // current_map.msize] != 1:
                self.rect = new_rect
        else:
            self.rect = old_rect

# NPCのクラス
class NPC:
    def __init__(self, image, position, dialogue):
        self.sheet = pygame.image.load(image).convert_alpha()
        self.rect = Rect(0, 0, CHARACTER_SIZE[0], CHARACTER_SIZE[1])
        self.rect.topleft = position
        self.frame = 0
        self.direction = 0
        self.animcycle = 24
        self.image = self.get_image()
        self.dialogue = dialogue

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def get_image(self):
        x = (self.frame // (self.animcycle // 3)) * CHARACTER_SIZE[0]
        y = self.direction * CHARACTER_SIZE[1]
        return self.sheet.subsurface(Rect(x, y, CHARACTER_SIZE[0], CHARACTER_SIZE[1]))

    def talk(self):
        # ダイアログボックスを返す
        return self.dialogue


# 画像の読み込み関数
def load_img(filename, colorkey=None):
    img = pygame.image.load(filename)
    img = img.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = img.get_at((0,0))
        img.set_colorkey(colorkey, RLEACCEL)
    return img

def main():
    pygame.init()
    pygame.display.set_caption("2D RPG Game")

    # フォントの設定
    font = pygame.font.Font(None, 36)

    # スクリーンとマップを作成
    screen = pygame.display.set_mode(SCR_RECT.size)
    map = Map()

    # キャラクターを作成
    character = Character("assets/character.png", (SCR_RECT.width / 2, SCR_RECT.height / 2))

    # NPCを作成
    npc = NPC("assets/npc.png", (200, 300), ["Hello there!", "Nice to meet you!", "Goodbye!"])


    # ゲームの状態
    STATE_OVERWORLD = "overworld"
    STATE_COMBAT = "combat"
    STATE_MENU = "menu"
    STATE_DIALOGUE = "dialogue"
    current_state = STATE_OVERWORLD

    # ゲームループ
    while True:
        if current_state == STATE_OVERWORLD:
            map.draw(screen)
            screen.blit(character.image, character.rect.topleft)  # 画像の描画
            npc.draw(screen)
        elif current_state == STATE_COMBAT:
            screen.fill(WHITE)
            text = font.render("Combat State", True, BLACK)
            screen.blit(text, (SCR_RECT.width // 2 - text.get_width() // 2, SCR_RECT.height // 2 - text.get_height() // 2))
        elif current_state == STATE_MENU:
            screen.fill(WHITE)
            text = font.render("Menu State", True, BLACK)
            screen.blit(text, (SCR_RECT.width // 2 - text.get_width() // 2, SCR_RECT.height // 2 - text.get_height() // 2))
        elif current_state == STATE_DIALOGUE:
            screen.fill(WHITE)
            for i, line in enumerate(npc.talk()):
                text = font.render(line, True, BLACK)
                screen.blit(text, (SCR_RECT.width // 2 - text.get_width() // 2, SCR_RECT.height // 2 - text.get_height() // 2 + i * 40))
        
        pygame.display.update()
        pygame.time.wait(30)  # 更新時間間隔

        # キャラクターの向きの初期設定
        direction = None

        # 今押されてるキーを取得
        pressed_key = pygame.key.get_pressed()

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                if event.key == K_o:
                    current_state = STATE_OVERWORLD
                elif event.key == K_c:
                    current_state = STATE_COMBAT
                elif event.key == K_m:
                    current_state = STATE_MENU
                elif event.key == K_ESCAPE:  # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
                elif event.key == K_e and current_state == STATE_OVERWORLD:
                    if character.rect.colliderect(npc.rect):
                        current_state = STATE_DIALOGUE
                elif event.key == K_e and current_state == STATE_DIALOGUE:
                    current_state = STATE_OVERWORLD

        # WASDキーでキャラクター移動
        if pressed_key[K_a]:
            character.move(-2, 0, map)
            direction = 1
        elif pressed_key[K_d]:
            character.move(2, 0, map)
            direction = 2
        elif pressed_key[K_w]:
            character.move(0, -2, map)
            direction = 3
        elif pressed_key[K_s]:
            character.move(0, 2, map)
            direction = 0  # 方向の設定

        character.update(direction)

if __name__ == "__main__":
    main()
