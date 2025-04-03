import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

running = True
drawing = False
color = BLACK
brush_size = 5
shape_mode = "brush"  
start_pos = None

def draw_shape(start, end, mode, color):
    if mode == "rectangle":
        rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
        pygame.draw.rect(screen, color, rect, 2)
    elif mode == "circle":
        radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, start, radius, 2)

screen.fill(WHITE)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos
                if shape_mode in ["rectangle", "circle"]:
                    draw_shape(start_pos, end_pos, shape_mode, color)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill(WHITE)  
            elif event.key == pygame.K_1:
                color = COLORS[0]
            elif event.key == pygame.K_2:
                color = COLORS[1]
            elif event.key == pygame.K_3:
                color = COLORS[2]
            elif event.key == pygame.K_4:
                color = COLORS[3]
            elif event.key == pygame.K_5:
                color = COLORS[4]
            elif event.key == pygame.K_UP:
                brush_size += 2
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 2)
            elif event.key == pygame.K_b:
                shape_mode = "brush"
            elif event.key == pygame.K_r:
                shape_mode = "rectangle"
            elif event.key == pygame.K_o:
                shape_mode = "circle"
            elif event.key == pygame.K_e:
                shape_mode = "eraser"

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if shape_mode == "brush":
            pygame.draw.circle(screen, color, mouse_pos, brush_size)
        elif shape_mode == "eraser":
            pygame.draw.circle(screen, WHITE, mouse_pos, brush_size)
    
    pygame.display.flip()
pygame.quit()
