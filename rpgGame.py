# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

# 画面サイズの設定
SCR_RECT = Rect(0, 0, 640, 480)

# キャラクターの1フレームのサイズ (幅, 高さ)
CHARACTER_SIZE = (32, 32)

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# マップのクラス
class Map:
    # マップデータ
    map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1],
           [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
           [1,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1],
           [1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1],
           [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1],
           [1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1],
           [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
           [1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1],
           [1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    row,col = len(map), len(map[0]) # マップの行数,列数を取得
    imgs = [None] * 256             # マップチップ
    msize = 32                      # 1マスの大きさ[px]
    # マップの描画
    def draw(self, screen):
        for i in range(self.row):
            for j in range(self.col):
                screen.blit(self.imgs[self.map[i][j]], (j*self.msize,i*self.msize))

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
        if direction:
            self.direction = direction
            self.frame += 1
            self.frame %= self.animcycle
            self.image = self.get_image()

    def get_image(self):
        x = (self.frame // (self.animcycle // 3)) * CHARACTER_SIZE[0]
        y = self.direction * CHARACTER_SIZE[1]
        return self.sheet.subsurface(Rect(x, y, CHARACTER_SIZE[0], CHARACTER_SIZE[1]))

    def move(self, dx, dy, current_map):
        # 移動前の位置
        old_rect = self.rect.copy()

        # 移動先の座標を計算
        new_rect = self.rect.move(dx, dy)

        # 移動先の座標がマップの範囲内かチェック
        if 0 <= new_rect.left // current_map.msize < current_map.col and 0 <= new_rect.top // current_map.msize < current_map.row:
            # 移動先のマップの値が1（壁）でないことを確認
            if current_map.map[new_rect.bottom // current_map.msize][new_rect.left // current_map.msize] != 1 and current_map.map[new_rect.bottom // current_map.msize][new_rect.right // current_map.msize] != 1:
                self.rect = new_rect
        else:
            self.rect = old_rect

# NPCのクラス
class NPC:
    def __init__(self, image, position, dialog):
        self.sheet = pygame.image.load(image).convert_alpha()
        self.rect = Rect(0, 0, CHARACTER_SIZE[0], CHARACTER_SIZE[1])
        self.rect.topleft = position
        self.image = self.sheet.subsurface(Rect(0, 0, CHARACTER_SIZE[0], CHARACTER_SIZE[1]))
        self.dialog = dialog

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)


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

    # ゲームのタイトル設定
    pygame.display.set_caption("2D RPG Game")

    # フォントの設定
    font = pygame.font.Font(None, 36)

    # スクリーンとマップを作成
    screen = pygame.display.set_mode(SCR_RECT.size)
    Map.imgs[0] = load_img("grass.png")         # 草地
    Map.imgs[1] = load_img("water.png")         # 水
    map = Map()

    # キャラクターを作成
    character = Character("character.png", (SCR_RECT.width / 2, SCR_RECT.height / 2))

    # NPCを作成
    npc = NPC("npc.png", (200, 200), "Hello, adventurer! Welcome to our village.")


    # ゲームの状態
    STATE_OVERWORLD = "overworld"
    STATE_COMBAT = "combat"
    STATE_MENU = "menu"
    STATE_DIALOG = "dialog"

    # 現在のゲーム状態
    current_state = STATE_OVERWORLD


    # ゲームループ
    while True:
        if current_state == STATE_OVERWORLD:
            map.draw(screen)
            screen.blit(character.image, character.rect.topleft)   # 画像の描画
        elif current_state == STATE_COMBAT:
            screen.fill(WHITE)
            text = font.render("Combat State", True, BLACK)
            screen.blit(text, (SCR_RECT.width // 2 - text.get_width() // 2, SCR_RECT.height // 2 - text.get_height() // 2))
        elif current_state == STATE_MENU:
            screen.fill(WHITE)
            text = font.render("Menu State", True, BLACK)
            screen.blit(text, (SCR_RECT.width // 2 - text.get_width() // 2, SCR_RECT.height // 2 - text.get_height() // 2))
        elif current_state == STATE_DIALOG:
            screen.fill(WHITE)
            text = font.render(npc.dialog, True, BLACK)
            screen.blit(text, (SCR_RECT.width // 2 - text.get_width() // 2, SCR_RECT.height // 2 - text.get_height() // 2))

        pygame.display.update()
        pygame.time.wait(30)        # 更新時間間隔

        # キャラクターの向きの初期設定
        direction = None

        #　今押されてるキーを取得
        pressed_key = pygame.key.get_pressed()

        # イベント処理
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_o:
                    current_state = STATE_OVERWORLD
                if event.key == K_c:
                    current_state = STATE_COMBAT
                if event.key == K_m:
                    current_state = STATE_MENU
                if event.key == K_RETURN and current_state == STATE_DIALOG:
                    current_state = STATE_OVERWORLD  # Enterキーで会話終了
            # 終了用のイベント処理
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       # キーを押したとき
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

        # WASDキーでキャラクター移動
        if pressed_key[K_a]:
            character.move(-2, 0, map)
            direction = 1
        if pressed_key[K_d]:
            character.move(2, 0, map)
            direction = 2
        if pressed_key[K_w]:
            character.move(0, -2, map)
            direction = 3
        if pressed_key[K_s]:
            character.move(0, 2, map)
            direction = 0.00001 # direction = 0だとスプライトの分割がうまくいかないので応急処置

        character.update(direction)

        # NPCとの接触をチェック
        if current_state == STATE_OVERWORLD and npc.check_collision(character.rect):
            current_state = STATE_DIALOG


if __name__ == "__main__":
    main()
