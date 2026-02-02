import random
import time

# Board size
WIDTH = 20
HEIGHT = 10

# Snake starting position
snake = [(5, 5)]
direction = "RIGHT"

# Food position
food = (random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))

def draw():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                print("O", end="")
            elif (x, y) == food:
                print("X", end="")
            elif x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()

while True:
    print("\n" * 50)
    draw()

    move = input("Move (W/A/S/D): ").upper()

    if move == "W":
        direction = "UP"
    elif move == "S":
        direction = "DOWN"
    elif move == "A":
        direction = "LEFT"
    elif move == "D":
        direction = "RIGHT"

    head_x, head_y = snake[0]

    if direction == "UP":
        new_head = (head_x, head_y - 1)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 1)
    elif direction == "LEFT":
        new_head = (head_x - 1, head_y)
    else:
        new_head = (head_x + 1, head_y)

    # Collision with wall or self
    if (new_head in snake or
        new_head[0] == 0 or new_head[0] == WIDTH - 1 or
        new_head[1] == 0 or new_head[1] == HEIGHT - 1):
        print("💀 Game Over!")
        break

    snake.insert(0, new_head)

    # Eating food
    if new_head == food:
        food = (random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))
    else:
        snake.pop()

    time.sleep(0.1)
