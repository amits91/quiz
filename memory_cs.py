# implementation of card game - Memory

# import simplegui
import simpleguitk as simplegui
import random

nums = []
SPACE = 13
exposed = []
state = 0
prev_idx1 = -1
prev_idx2 = -1
turns = 0
# helper function to initialize globals
def new_game():
    global nums, exposed, state, prev_idx1, prev_idx2, turns
    nums = range(0, 8)*2
    random.shuffle(nums)
    exposed = [False] * 16
    state = 0
    prev_idx1 = -1
    prev_idx2 = -1
    turns = 0
    label.set_text('Turns = ' + str(turns))


# define event handlers
def mouseclick(pos):
    global state, prev_idx1, prev_idx2, exposed, nums, turns, label
    # return if y axis is beyond range
    if not(0 <= pos[1] < 100):
        return
    if not(0 <= pos[0] < 800):
        return
    idx = pos[0] // 50
    if exposed[idx] == False:
        exposed[idx] = True
        #print prev_idx1, nums[prev_idx1], "=>", prev_idx2, nums[prev_idx2]
        if state == 0:
            state = 1
        elif state == 1:
            state = 2
            turns += 1
        else:
            state = 1
            #turns += 1
            if (nums[prev_idx1] == nums[prev_idx2]):
                #print "Match"
                exposed[prev_idx1] = True
                exposed[prev_idx2] = True
            else:
                exposed[prev_idx1] = False
                exposed[prev_idx2] = False
        prev_idx2 = prev_idx1
        prev_idx1 = idx
        label.set_text('Turns = ' + str(turns))


# cards are logically 50x100 pixels in size
def draw(canvas):
    global nums, SPACE, exposed
    for i in range(len(nums)):
        if exposed[i]:
            canvas.draw_text(str(nums[i]), [50 * i + SPACE, 70], 50, 'White')
        else:
            canvas.draw_line([50 * i + 25, 0], [50 * i + 25, 100], 50, 'Green')
        #canvas.draw_text(str(i), [50*i, 20], 20, 'White')
    #canvas.draw_text(str(state), [0, 40], 20, 'White')
    for i in range(1, len(nums)):
        canvas.draw_line([50*i, 0], [50*i, 100], 2, 'Red')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric