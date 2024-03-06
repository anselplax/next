import random
import curses

# initialize the screen
screen = curses.initscr()
curses.curs_set(1)
screen_height, screen_width = screen.getmaxyx()

# create the snake
snake = [(screen_height//2, screen_width//2)]
direction = curses.KEY_RIGHT

# create the food
food = (random.randint(1, screen_height-2), random.randint(1, screen_width-1))

# draw the food
screen.addch(food[0], food[1], curses.ACS_PI)

# game loop
while True:
    # get the user input
    key = screen.getch()

    # change direction based on input
    if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        direction = key

    # move the snake
    head = snake[0]
    if direction == curses.KEY_UP:
        new_head = (head[0]-1, head[0])
    elif direction == curses.KEY_DOWN:
        new_head = (head[0]+1, head[1])
    elif direction == curses.KEY_LEFT:
        new_head = (head[0], head[1]-1)
    elif direction == curses.KEY_RIGHT:
        new_head = (head[0], head[1]+1)

    # check if the snake hits the wall or itself
    if new_head[0] in [0, screen_height] or new_head[1] in [0, screen_width] or new_head in snake:
        curses.endwin()
        quit()

    # add the new head to the snake
    snake.insert(0, new_head)

    # check if the snake eats the food
    if snake[0] == food:
        food = (random.randint(1, screen_height-1), random.randint(1, screen_width-1))
        screen.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        screen.addch(tail[0], tail[1], ' ')

    # draw the snake
    for i, (y, x) in enumerate(snake):
        if i == 0:
            screen.addch(y, x, curses.ACS_CKBOARD)
        else:
            screen.addch(y, x, curses.ACS_BLOCK)

    # refresh the screen
    screen.refresh()
