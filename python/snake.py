from tkinter import *
import random

#constants

Game_width = 900
game_hight = 750
speed = 100
space_size = 30
body_parts = 6
snake_color = "#b5ff8a"
food_color = "#FFFFFF"
background_color = "#0000e1"


#Classes

class Snake:
    def __init__(self):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []
        
        for i in range (0, body_parts):
            self.coordinates.append([0,0])
            
        for x, y in self.coordinates:
            square = canvas.create_oval(x, y, x+space_size, y+space_size, fill = snake_color, tag = "snake")
            self.squares.append(square)

class Food:
    
    def __init__(self):
        
        x = random.randint(0, (Game_width/space_size) - 1) * space_size
        y = random.randint(0, (game_hight/space_size) - 1) * space_size
        
        self.coordinates = [x, y]
        
        canvas.create_oval(x, y, x + space_size, y + space_size, fill = food_color, tag = "food")

def next_turn(snake, food):
    global speed
    x, y = snake.coordinates[0]
    
    if direction == "up":
        y -= space_size
    elif direction == "down":
        y+= space_size
    elif direction == "left":
        x-=space_size
    elif direction == "right":
        x+=space_size
    #elif direction == "space":
        #speed -= 10
    
    
    snake.coordinates.insert(0,(x,y))
    square = canvas.create_oval(x, y, x+space_size, y+space_size, fill = snake_color, tag = "snake")
    snake.squares.insert(0, square)
    
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    if check_collition(snake):
        game_over()
    
    
    window.after(speed, next_turn, snake, food)

def check_collition(snake):
    x, y = snake.coordinates[0]
    
    if x < 0 or x >= Game_width:
        return True
    elif y < 0 or y >= game_hight:
        return True
    
    '''
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            #print("GameOver")
            return True
    '''
    return False
    

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font= ('consolas', 70), text="GAME OVER", fill = "red", tag = "gameover")
    
    
    

def change_direction(new_direction):
    global direction
    
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
            
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
            
    #elif new_direction == 'space':
        #direction = new_direction    


#window operations

window = Tk()
window.title("SHAPA Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="score{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg = background_color, height = game_hight, width=Game_width)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_weidth = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_weidth/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
#window.bind('<Space>', lambda event: change_direction('space'))



snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
