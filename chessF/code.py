import pygame

window = pygame.display.set_mode((700,600))
pygame.display.set_caption("CHESS")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False