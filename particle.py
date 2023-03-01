import pygame
import random

# definir constantes
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PARTICLE_SIZE = 5
PARTICLE_SPEED = 5
PARTICLE_COUNT = 50

# definir la clase Particle
class Particle:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self):
        self.x += random.randint(-self.speed, self.speed)
        self.y += random.randint(-self.speed, self.speed)

        if self.x < 0:
            self.x = SCREEN_WIDTH
        elif self.x > SCREEN_WIDTH:
            self.x = 0

        if self.y < 0:
            self.y = SCREEN_HEIGHT
        elif self.y > SCREEN_HEIGHT:
            self.y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# inicializar Pygame
pygame.init()

# crear la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simulacion de particulas")

# crear la lista de particulas
particles = []
for i in range(PARTICLE_COUNT):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    particle = Particle(x, y, PARTICLE_SIZE, PARTICLE_SPEED)
    particles.append(particle)

# bucle principal
running = True
while running:
    # gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # actualizar las particulas
    for particle in particles:
        particle.update()

    # dibujar las particulas
    screen.fill((0, 0, 0))
    for particle in particles:
        particle.draw(screen)
    pygame.display.flip()

# salir de Pygame
pygame.quit()
