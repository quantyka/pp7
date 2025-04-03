import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("circle")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, radius, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def move(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed

        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.7071  # Approx 1/sqrt(2)
            dy *= 0.7071

        self.x += int(dx)
        self.y += int(dy)

        # Prevent moving out of bounds
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)

# Create player instance
player = Player(-200, -100, 25, 5)

# Game loop
running = True
while running:
    clock.tick(90)  # Control frame rate

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()

    # Move player
    player.move(keys)

    # Drawing
    screen.fill(WHITE)
    player.draw(screen)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
