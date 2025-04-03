import pygame
from datetime import datetime 
pygame.init()
pygame.display.set_caption("Mickey Clock")
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
back = pygame.image.load("C:/Users/quant/Documents/Lab7/back.png")
minute = pygame.image.load("C:/Users/quant/Documents/Lab7/minute.png")
second = pygame.image.load("C:/Users/quant/Documents/Lab7/second.png")
running = True
while running:
    now = datetime.now()
    nowMin = now.minute
    nowSec = now.second
    minAngle = nowMin * 6
    secAngle = nowSec * 6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    rot_min = pygame.transform.rotate(minute, -minAngle)
    rot_sec = pygame.transform.rotate(second, -secAngle)
    screen.blit(back, (0, 0))
    screen.blit(rot_min, (300 - int(rot_min.get_width()) // 2, 300 - int(rot_min.get_height()) // 2))
    screen.blit(rot_sec, (300 - int(rot_sec.get_width()) // 2, 300 - int(rot_sec.get_height()) // 2))
    pygame.display.flip()
    clock.tick(1)