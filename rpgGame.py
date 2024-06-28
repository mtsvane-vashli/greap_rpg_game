import pygame
import sys

# ゲームの初期化
pygame.init()

# 画面のサイズ設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# ゲームのタイトル設定
pygame.display.set_caption("2D RPG Game")

# フォントの設定
font = pygame.font.Font(None, 36)

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ゲームの状態
STATE_OVERWORLD = "overworld"
STATE_COMBAT = "combat"
STATE_MENU = "menu"

# 現在のゲーム状態
current_state = STATE_OVERWORLD

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                current_state = STATE_MENU
            elif event.key == pygame.K_c:
                current_state = STATE_COMBAT
            elif event.key == pygame.K_o:
                current_state = STATE_OVERWORLD

    screen.fill(WHITE)

    if current_state == STATE_OVERWORLD:
        text = font.render("Overworld State", True, BLACK)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    elif current_state == STATE_COMBAT:
        text = font.render("Combat State", True, BLACK)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    elif current_state == STATE_MENU:
        text = font.render("Menu State", True, BLACK)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

    pygame.display.flip()

# ゲームの終了
pygame.quit()
sys.exit()
