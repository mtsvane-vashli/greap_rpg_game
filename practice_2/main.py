import pygame
from pygame.locals import *
import sys
from constants import *
# from map import


class Player :

    def __init__(self, position) :

        self.rect = Rect(0, 0, 32, 32)
        self.rect.topleft = position
        self.image = pygame.Surface((32, 32))


    # TODO
    def move(self, dx, dy, current_map):
        old_rect = self.rect.copy()
        new_rect = self.rect.move(dx, dy)

        if 0 <= new_rect.left // current_map.msize < current_map.col and 0 <= new_rect.top // current_map.msize < current_map.row:
            if current_map.map[new_rect.bottom // current_map.msize][new_rect.left // current_map.msize] != 1 and \
               current_map.map[new_rect.bottom // current_map.msize][new_rect.right // current_map.msize] != 1:
                self.rect = new_rect
        else:
            self.rect = old_rect


    def draw(self, screen) :
        screen.blit(self.image, self.rect.topleft)



def main() :

    pygame.init()
    pygame.display.set_caption("2D RPG Game")
    clock = pygame.time.Clock()  # for fps setting

    # スクリーンとマップを作成
    screen = pygame.display.set_mode(SCREEN_RECT.size)
    # map = Map()

    player = Player((SCREEN_RECT.width / 2, SCREEN_RECT.height / 2))


    while True :
    
        for event in pygame.event.get() :
        
            if event.type == QUIT:  # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:  # キーを押した(発火タイミング)とき
                if event.key == K_ESCAPE:  # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

        pressed_key = pygame.key.get_pressed()

        if pressed_key[K_a]:
            player.move(-4, 0, map)
            
        elif pressed_key[K_d]:
            player.move(4, 0, map)
           
        elif pressed_key[K_w]:
            player.move(0, -4, map)
          
        elif pressed_key[K_s]:
            player.move(0, 4, map)





        # map.draw()

        player.draw()

        clock.tick(FPS)



if __name__ == "__main__":
    main()