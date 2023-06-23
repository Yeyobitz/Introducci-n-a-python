import pygame
import random

pygame.init()

########### objeto de la serpiente ##############
class Snake:
    def __init__(self, block_size, screen_width, screen_height, width, height):
        # Initialize the snake with its starting position, length, and body
        self.block_size = block_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.direction = (0, 0)
        self.x = screen_width // (2 * block_size) * block_size
        self.y = screen_height // (2 * block_size) * block_size        
        self.length = 1
        self.body = [(self.x, self.y)]
        self.width = width
        self.height = height

    def move(self, dx, dy):
        # Move the snake in the given direction
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, self.screen_width - 1))
        self.y = max(0, min(self.y, self.screen_height - 1))
        self.body.insert(0, (self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop()

    def collide_food(self, x, y):
        # Check if the snake has collided with the food
        if self.x == x and self.y == y:
            self.grow()
            self.move(self.direction[0], self.direction[1])
            return True
        return False

    def grow(self):
        # Increase the length of the snake
        self.length += 1

    def draw(self, surface):
        # Draw the snake on the given surface
        for block in self.body:
            x, y = block[0], block[1]
            rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size - 1, self.block_size - 1)
            pygame.draw.rect(surface, (0, 255, 0), rect)

    def collide_body(self):
        # Check if the snake has collided with its own body
        for block in self.body[1:]:
            if block[0] == self.x and block[1] == self.y:
                return True
        return False

    def handle_keys(self):
        # Handle user input to change the direction of the snake
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.direction != (1, 0):
                self.direction = (-1, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.direction != (-1, 0):
                self.direction = (1, 0)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.direction != (0, 1):
                self.direction = (0, -1)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.direction != (0, -1):
                self.direction = (0, 1)

        self.move(self.direction[0], self.direction[1])

    def collide_wall(self):
        # Check if the snake has collided with a wall
        return self.x == 0 or self.x == self.screen_width - 1 or self.y == 1 or self.y == self.screen_height - 1
    
########### objeto de la comida ##############
class Food:
    def __init__(self, block_size):
        # Initialize the food with its starting position
        self.block_size = block_size
        self.x = 0
        self.y = 0

    def draw(self, surface):
        # Draw the food on the given surface
        rect = pygame.Rect(self.x * self.block_size, self.y * self.block_size, self.block_size, self.block_size)
        pygame.draw.rect(surface, (255, 0, 0), rect)

    def collide(self, x, y):
        # Check if the food has been eaten by the snake
        return self.x == x and self.y == y

    def spawn(self, width, height, snake_body):
        # Spawn the food at a random location within the given width and height
        self.x = random.randrange(1, width -1)
        self.y = random.randrange(2, height)
        # Don't spawn the food inside the snake
        while (self.x, self.y) in snake_body:
            self.x = random.randrange(1, width - 1)
            self.y = random.randrange(2, height)
        

########### objeto del juego ##############
class Game:
    def __init__(self):
        # Initialize the game with its starting values
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Yeyo'Snake")
        self.block_size = 15
        self.clock = pygame.time.Clock()
        self.fps = 10
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.snake = Snake(self.block_size, self.width // self.block_size, self.height // self.block_size, self.width, self.height)
        self.food = Food(self.block_size)
        self.food.spawn(self.width // self.block_size, self.height // self.block_size, self.snake.body)
        self.game_over = False
        self.speed_increase_interval = 5  # Increase speed every 5 points
        self.speed_increase_amount = 1  # Increase speed by 1 FPS
        self.difficulty = None
        self.title_screen()

    def title_screen(self):
        # Show the title screen with the game name and options to start the game, select difficulty, or quit
        while True:
            self.screen.fill((0, 0, 0))
            text = self.font.render("Yeyo'Snake", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 60))
            self.screen.blit(text, text_rect)
            start_button = pygame.Rect(self.width // 2 - 100, self.height // 2 - 20, 200, 40)
            pygame.draw.rect(self.screen, (255, 255, 255), start_button)
            text = self.font.render("Start Game", True, (0, 0, 0))
            text_rect = text.get_rect(center=start_button.center)
            self.screen.blit(text, text_rect)
            difficulty_button = pygame.Rect(self.width // 2 - 100, self.height // 2 + 40, 200, 40)
            pygame.draw.rect(self.screen, (255, 255, 255), difficulty_button)
            text = self.font.render("Select Difficulty", True, (0, 0, 0))
            text_rect = text.get_rect(center=difficulty_button.center)
            self.screen.blit(text, text_rect)
            quit_button = pygame.Rect(self.width // 2 - 100, self.height // 2 + 100, 200, 40)
            pygame.draw.rect(self.screen, (255, 255, 255), quit_button)
            text = self.font.render("Quit", True, (0, 0, 0))
            text_rect = text.get_rect(center=quit_button.center)
            self.screen.blit(text, text_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        self.difficulty = "easy"
                        return
                    elif difficulty_button.collidepoint(event.pos):
                        self.select_difficulty()
                    elif quit_button.collidepoint(event.pos):
                        pygame.quit()

    def select_difficulty(self):
        # Show the difficulty selection screen with options for easy, medium, and hard
        while True:
            self.screen.fill((0, 0, 0))
            text = self.font.render("Select Difficulty", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 60))
            self.screen.blit(text, text_rect)
            easy_button = pygame.Rect(self.width // 2 - 100, self.height // 2 - 20, 200, 40)
            pygame.draw.rect(self.screen, (255, 255, 255), easy_button)
            text = self.font.render("Easy", True, (0, 0, 0))
            text_rect = text.get_rect(center=easy_button.center)
            self.screen.blit(text, text_rect)
            medium_button = pygame.Rect(self.width // 2 - 100, self.height // 2 + 40, 200, 40)
            pygame.draw.rect(self.screen, (255, 255, 255), medium_button)
            text = self.font.render("Medium", True, (0, 0, 0))
            text_rect = text.get_rect(center=medium_button.center)
            self.screen.blit(text, text_rect)
            hard_button = pygame.Rect(self.width // 2 - 100, self.height // 2 + 100, 200, 40)
            pygame.draw.rect(self.screen, (255, 255, 255), hard_button)
            text = self.font.render("Hard", True, (0, 0, 0))
            text_rect = text.get_rect(center=hard_button.center)
            self.screen.blit(text, text_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.collidepoint(event.pos):
                        self.difficulty = "easy"
                        return
                    elif medium_button.collidepoint(event.pos):
                        self.difficulty = "medium"
                        return
                    elif hard_button.collidepoint(event.pos):
                        self.difficulty = "hard"
                        return
    def draw_grid(self):
        # Draw the grid lines on the screen
        for x in range(0, self.width, self.block_size):
            pygame.draw.line(self.screen, (128, 128, 128), (x, 0), (x, self.height))
        for y in range(0, self.height, self.block_size):
            pygame.draw.line(self.screen, (128, 128, 128), (0, y), (self.width, y))

    def draw(self):
        # Draw the game on the screen
        if self.difficulty == "easy":
            self.draw_grid()  # Draw the grid lines on top of the black background
        elif self.difficulty == "hard":
            self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(10, 10))
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def run(self):
        # Run the game loop until the game is over
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_over = True

            self.snake.handle_keys()

            if self.snake.collide_food(self.food.x, self.food.y):
                self.snake.grow()
                self.score += 1
                self.food.spawn(self.width // self.block_size, self.height // self.block_size, self.snake.body)

                # Increase speed every `speed_increase_interval` points for medium difficulty
                if self.difficulty == "medium" and self.score % self.speed_increase_interval == 0 and self.fps < 30:
                    self.fps += self.speed_increase_amount

                # Increase speed every `speed_increase_interval` points for hard difficulty
                elif self.difficulty == "hard" and self.score % self.speed_increase_interval == 0 and self.fps < 50:
                    self.fps += self.speed_increase_amount

            if self.snake.collide_wall() or self.snake.collide_body():
                self.game_over = True

            self.clock.tick(self.fps)
            self.draw()

        self.game_over_screen()

    def game_over_screen(self):
        # Show the game over screen with the final score and an option to retry
        self.screen.fill((0, 0, 0))
        text = self.font.render(f"Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 - 30))
        self.screen.blit(text, text_rect)
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 + 30))
        self.screen.blit(text, text_rect)
        text = self.font.render(f"Press SPACE to try again or ESC to quit", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2 + 90))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.__init__()
                        self.run()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()



def main():
    # Start the game 
    game = Game()
    game.run()
    game.quit()

if __name__ == "__main__":
    main()