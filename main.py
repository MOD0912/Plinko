import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plinko Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Peg settings
PEG_RADIUS = 10
PEG_SPACING = 60

# Ball settings
BALL_RADIUS = 10
BALL_COLOR = RED
BALL_VELOCITY = 2

# Create pegs in a pyramid shape
def create_pegs():
    pegs = []
    for y in range(7):
        for x in range(y + 3):
            peg_x = WIDTH // 3 + (x - y / 2) * PEG_SPACING + 70
            peg_y = HEIGHT // 4 + y * PEG_SPACING + 5
            pegs.append((peg_x, peg_y))
    return pegs

# Draw pegs
def draw_pegs(pegs):
    for peg in pegs:
        pygame.draw.circle(screen, BLUE, peg, PEG_RADIUS)

# Ball class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = BALL_VELOCITY

    def move(self):
        self.vy += 0.1
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pygame.draw.circle(screen, BALL_COLOR, (int(self.x), int(self.y)), BALL_RADIUS)

    def check_collision(self, pegs):
        for peg in pegs:
            dx = self.x - peg[0]
            dy = self.y - peg[1]
            distance = math.hypot(dx, dy)
            if distance <= PEG_RADIUS + BALL_RADIUS:
                angle = math.atan2(dy, dx)
                self.vx = math.cos(angle)  * 1.5
                self.vy = math.sin(angle)  * 1.5
                overlap = PEG_RADIUS + BALL_RADIUS - distance
                self.x += math.cos(angle) * overlap
                self.y += math.sin(angle) * overlap
                
         
        if self.x < 100 or self.x > WIDTH-100:
            self.vx *= -1

# Main game loop
def main():
    clock = pygame.time.Clock()
    pegs = create_pegs()
    balls = []

    running = True
    while running:
        screen.fill(WHITE)
        draw_pegs(pegs)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                balls.append(Ball(WIDTH // 2, 0))

        for ball in balls:
            ball.move()
            ball.check_collision(pegs)
            ball.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()