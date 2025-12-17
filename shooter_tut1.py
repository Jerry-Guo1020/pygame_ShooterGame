import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        # 加载播放器的照片
        img = pygame.image.load('img/player/Idle/0.png')
        self.img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.img.get_rect()
        # 定位这个矩形的位置
        self.rect.center = (x, y)


#  这里有一个角色，我能够通过鼠标啦进行移动，弄个坐标
player = Soldier(200, 200, 3)
player2 = Soldier(400, 200, 3)





run = True
while run:
    
    # 使用blit函数
    screen.blit(player.img, player.rect)    
    screen.blit(player2.img, player2.rect)    
    
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
            
    # 让东西出现在画面上，通过循环就可以一直保留
    pygame.display.update()
    
pygame.quit()