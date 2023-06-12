import pygame, sys
# https://www.youtube.com/watch?v=tehfGVNWtCM
pygame.init()

speed = [4, 4]
size = 1146, 716
width = 1146
height = 716
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()
logo = pygame.image.load("amongus.png")
rect = logo.get_rect()
fps = 60
pygame.display.set_caption("Among us screen saver")
pygame.display.set_icon(pygame.image.load("amongus.png"))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    if rect.left < -50:
        speed[0] = -speed[0]
    if rect.left > (width - 250): 
        speed[0] = -speed[0]
    if rect.top < 0:
        speed[1] = -speed[1]
    if rect.bottom > height: 
        speed[1] = -speed[1]
    rect.left += speed[0]
    rect.top += speed[1]
    screen.fill((0, 0, 0))
    screen.blit(logo, rect)
    pygame.display.update()
    clock.tick(fps)
    width = screen.get_width()
    height = screen.get_height()