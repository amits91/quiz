# Implementation of classic arcade game Pong

# import simplegui
import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
BALL_ACCEL = 1.1

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [1, 1]
paddle1_pos = 0
paddle2_pos = 0
paddle1_vel = 0
paddle2_vel = 0
acc = 5
score1 = 0
score2 = 0
last_spawn = LEFT
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global last_spawn
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        horiz = random.randrange(120, 240)
        vert  = -random.randrange(60, 180)
    else :
        horiz = -random.randrange(120, 240)
        vert  = -random.randrange(60, 180)
    ball_vel = [horiz/60, vert/60]
    last_spawn = direction
    print ball_vel



# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global last_spawn
    score1 = 0
    score2 = 0
    spawn_ball(not(last_spawn))
def button_handler():
    new_game()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle1_vel, paddle2_pos, paddle2_vel, ball_pos, ball_vel
    global BALL_ACCEL


    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        paddle1_top = paddle1_pos - BALL_RADIUS
        paddle1_bot = paddle1_pos + PAD_HEIGHT + BALL_RADIUS
        if paddle1_top <= ball_pos[1] <= paddle1_bot:
            ball_vel[0] *= BALL_ACCEL
            ball_vel[1] *= BALL_ACCEL
            ball_vel[0] = -ball_vel[0]
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS:
        paddle2_top = paddle2_pos - BALL_RADIUS
        paddle2_bot = paddle2_pos + PAD_HEIGHT + BALL_RADIUS
        if paddle2_top <= ball_pos[1] <= paddle2_bot:
            ball_vel[0] *= BALL_ACCEL
            ball_vel[1] *= BALL_ACCEL
            ball_vel[0] = -ball_vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'Orange', 'White')

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel


    # draw paddles
    # left paddle
    p1 = paddle1_pos + PAD_HEIGHT
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH, p1], PAD_WIDTH, 'White')
    # right paddle
    p2 = paddle2_pos + PAD_HEIGHT
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos], [WIDTH - HALF_PAD_WIDTH, p2], PAD_WIDTH, 'White')
    # determine whether paddle and ball collide
    if paddle1_pos < 0:
        paddle1_pos = 0
    elif paddle1_pos >= HEIGHT - PAD_HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    if paddle2_pos < 0:
        paddle2_pos = 0
    elif paddle2_pos >= HEIGHT - PAD_HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT

    # draw scores
    canvas.draw_text(str(score1), [WIDTH/2 - 100, 50], 50, 'White')
    canvas.draw_text(str(score2), [WIDTH/2 + 100, 50], 50, 'White')

def keydown(key):
    global paddle1_vel, paddle2_vel, acc
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc

    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc

    print ball_pos

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0

    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", button_handler, 100)


# start frame
new_game()
frame.start()
