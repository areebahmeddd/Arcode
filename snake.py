import pygame
import random

# Initializes the Pygame module, sets up the game screen and starts the game loop
def run_game():
    pygame.init()
    pygame.display.set_caption("Arcode")

    game_screen = pygame.display.set_mode((600, 400))
    fps_clock = pygame.time.Clock()

    game_loop(game_screen, fps_clock)

# Handles the game logic and game updates
def game_loop(game_screen, fps_clock):
    snake_size = 10
    snake_speed = 15

    snake_x = game_screen.get_width() / 2
    snake_y = game_screen.get_height() / 2

    x_direction = 0
    y_direction = 0

    snake_body = []
    snake_length = 1

    food_x, food_y = generate_food(game_screen, snake_size)

    while True:
        x_direction, y_direction = update_snake(x_direction, y_direction, snake_size)

        snake_x += x_direction
        snake_y += y_direction

        if (snake_x < 0 or snake_x >= game_screen.get_width() 
                or snake_y < 0 or snake_y >= game_screen.get_height()):
            display_message(game_screen, "Game Over!", pygame.Color("white"))
            pygame.display.update()
            pygame.time.wait(1000)
            pygame.quit()
            quit()

        if [snake_x, snake_y] == [food_x, food_y]:
            snake_length += 1
            snake_speed += 2
            food_x, food_y = generate_food(game_screen, snake_size)

        snake_body.append([snake_x, snake_y])
        snake_body = snake_body[-snake_length:]

        update_screen(game_screen, food_x, food_y, snake_size, snake_body)
        pygame.display.update()

        fps_clock.tick(snake_speed)

# Generates random coordinates for the food within the game screen
def generate_food(game_screen, snake_size):
    food_x = round(random.randrange(0, game_screen.get_width() - snake_size) / snake_size) * snake_size
    food_y = round(random.randrange(0, game_screen.get_height() - snake_size) / snake_size) * snake_size

    return food_x, food_y

# Handles the user input and snake movement
def update_snake(x_direction, y_direction, snake_size):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x_direction = 0
                y_direction = -snake_size

            elif event.key == pygame.K_DOWN:
                x_direction = 0
                y_direction = snake_size

            elif event.key == pygame.K_LEFT:
                x_direction = -snake_size
                y_direction = 0

            elif event.key == pygame.K_RIGHT:
                x_direction = snake_size
                y_direction = 0

            else:
                print("[Invalid Key]")
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()

    return x_direction, y_direction

# Displays a message on the game screen
def display_message(game_screen, text, text_color):
    render_text = pygame.font.SysFont("Helvetica", 30).render(text, True, text_color)
    text_position = render_text.get_rect(center = game_screen.get_rect().center)
    game_screen.blit(render_text, text_position)

# Renders the game screen with food and snake body
def update_screen(game_screen, food_x, food_y, snake_size, snake_body):
    game_screen.fill(pygame.Color("black"))
    food_position = pygame.Rect(food_x, food_y, snake_size, snake_size)
    pygame.draw.rect(game_screen, pygame.Color("red"), food_position)

    for segment_x, segment_y in snake_body:
        snake_segment = pygame.Rect(segment_x, segment_y, snake_size, snake_size)
        pygame.draw.rect(game_screen, pygame.Color("white"), snake_segment)

run_game()