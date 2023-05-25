import pygame
import random

##### Clase para la serpiente

class Snake:
    def __init__(self, x, y, block_size, screen_width, screen_height):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.length = 1
        self.body = [(x, y)]
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.direction = (0, 0)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.body.insert(0, (self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop()

    def collide_food(self, x, y):
        if self.x == x and self.y == y:
            self.grow()
            self.move(self.direction[0], self.direction[1])
            return True
        return False
    
    def grow(self):
        self.length += 1

    def draw(self, surface):
        for block in self.body:
            x, y = block[0], block[1]
            rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
            pygame.draw.rect(surface, (0, 255, 0), rect)

    def collide_body(self):
        for block in self.body[1:]:
            if block[0] == self.x and block[1] == self.y:
                return True
        return False
    
    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = (-1, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = (1, 0)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = (0, -1)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = (0, 1)

        self.move(self.direction[0], self.direction[1])

    def collide_wall(self):
        if self.x < 0 or self.x >= self.screen_width or self.y < 0 or self.y >= self.screen_height:
            return True
        return False

##### Clase para la comida

class Food:
    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size

    def draw(self, surface):
        rect = pygame.Rect(self.x * self.block_size, self.y * self.block_size, self.block_size, self.block_size)
        pygame.draw.rect(surface, (255, 0, 0), rect)

    def collide(self, x, y):
        if self.x == x and self.y == y:
            return True
        return False
    
    def spawn(self, width, height):
        self.x = random.randrange(0, width - self.block_size + 1, self.block_size)
        self.y = random.randrange(0, height - self.block_size + 1, self.block_size)

##### Clase para el juego

class Game:
    def __init__(self):
        pygame.init()
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Yeyo's Snake")
        self.block_size = 10
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.snake = Snake(self.width / 2, self.height / 2, self.block_size, self.width, self.height)
        self.food = Food(0, 0, self.block_size)
        self.food.spawn(self.width / self.block_size, self.height / self.block_size)
        self.game_over = False

    # Función para dibujar la serpiente, la comida y el score en bloques
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width / 2, 15))
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def run(self):
        while not self.game_over:
            event = pygame.event.poll()  # use poll() instead of get()
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_over = True

            self.snake.handle_keys()

            if self.snake.collide_food(self.food.x, self.food.y):
                self.snake.grow()
                self.food.spawn(self.width, self.height)
                self.score += 1
            if self.snake.collide_wall() or self.snake.collide_body():
                self.game_over = True

            self.clock.tick(self.fps)

            self.draw()  # update only when necessary

        self.game_over_screen()

    def game_over_screen(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width / 2, self.height / 2))
        self.screen.blit(text, text_rect)
        text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width / 2, self.height / 2 + 30))
        self.screen.blit(text, text_rect)
        pygame.display.update()  # use update() instead of flip()
        pygame.time.wait(2000)

    def quit(self):
        pygame.quit()

def main():
    game = Game()
    game.run()
    game.quit()

if __name__ == "__main__":
    main()