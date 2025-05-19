# using tinker make any formated application according to your idea 
import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
UPDATE_DELAY = 100

direction = 'Right'
snake = [(100, 100), (80, 100), (60, 100)]
food = None

window = tk.Tk()
window.title("Snake Game - Enhanced Version")
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

def draw_snake():
    canvas.delete("snake")
    for segment in snake:
        x, y = segment
        canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="lime", tag="snake")

def place_food():
    global food
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    food = (x, y)
    canvas.create_oval(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="red", tag="food")

def change_direction(event):
    global direction
    opposites = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
    if event.keysym in opposites and direction != opposites[event.keysym]:
        direction = event.keysym

def move_snake():
    global snake, food

    head_x, head_y = snake[0]
    if direction == 'Up': head_y -= CELL_SIZE
    elif direction == 'Down': head_y += CELL_SIZE
    elif direction == 'Left': head_x -= CELL_SIZE
    elif direction == 'Right': head_x += CELL_SIZE

    new_head = (head_x, head_y)

    if new_head in snake or head_x < 0 or head_y < 0 or head_x >= WIDTH or head_y >= HEIGHT:
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER", fill="white", font=('Arial', 32))
        return

    snake.insert(0, new_head)

    if new_head == food:
        place_food()
    else:
        snake.pop()

    draw_snake()
    canvas.after(UPDATE_DELAY, move_snake)

draw_snake()
place_food()
window.bind("<KeyPress>", change_direction)
move_snake()
window.mainloop()