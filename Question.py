'''
Base Question class for Quiz
Codeskulptor Link: http://www.codeskulptor.org/#user40_nva4UorE3O_2.py
'''
'''
Base Question class for Quiz
'''
import random
DESKTOP = True
CHOICE_LABELS = ['A', 'B', 'C', 'D']
WIDTH = 800
HEIGHT = 600
FONT_COLOR = 'Black'
FONT_SIZE = 15
quiz_started = False

# DESKTOP = False
if DESKTOP == False:
    import simplegui
    PATH = "https://dl.dropbox.com/s/"
    WELCOME_PREFIX = "aboqginatbi5tpe/"
    WRONG_PREFIX = "4wy0o9lsdgeh729/"
    CORRECT_SOUND = "stu10xsbzd9svcd/"
else:
    import simpleguitk as simplegui
    PATH = 'C:\\AMIT_FILES\\Dropbox\\BETU\\Quiz_game\\sound_files\\'
    WELCOME_PREFIX = ""
    WRONG_PREFIX = ""
    CORRECT_SOUND = ""

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

q1_info = ImageInfo([64, 64], [128, 128], 17, 24, True)

betu_image = simplegui.load_image("https://dl.dropbox.com/s/e0ven0zimd60q16/betu.jpg")
betu_info = ImageInfo([111, 122], [222, 244])
# welcome_sound = simplegui.load_sound(PATH + WELCOME_PREFIX + "Welcome.mp3")
# wrong_sound   = simplegui.load_sound(PATH + WRONG_PREFIX + "Wrong.mp3")
# correct_sound = simplegui.load_sound(PATH + CORRECT_SOUND + "Right.mp3")

def conv_choice_list(ch):
    choices = {}
    for i in range(len(ch)):
        choices[CHOICE_LABELS[i]] = ch[i]
    return choices

class Data:
    def __init__(self, text, img = None):
        self._text = text
        self._img = img
        self._width = FONT_SIZE * len(text)
        self._height = FONT_SIZE * 2
    def getText(self):
        return self._text
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def __str__(self):
        return str(self._text)
    def draw(self, canvas, pos, isSelected = False):
        canvas.draw_text(self._text, pos, FONT_SIZE, FONT_COLOR)


class Question:
    '''
    Textual Question
    '''
    def __init__(self, question, choice_list, correct_idx):
        self._question = question
        self._choices = conv_choice_list(choice_list)
        self._correct = CHOICE_LABELS[correct_idx]
        self._user_choice = None

    def getInstruction(self):
        return self._question
    def getCorrectData(self):
        return self._correct
    def __str__(self):
        qstr = "Question: " + self.getInstruction()
        qstr = qstr + '\n'
        # qstr = qstr + "Figure: None\n"
        for ch in CHOICE_LABELS:
            qstr = qstr + ch + ': ' + str(self._choices[ch]) + "\n"
        return qstr
    def printQuestion(self, choice = None):
        print self
        if choice != None:
            print 'You entered', choice, ',',
            if choice == self.getCorrectData():
                print "Correct!! Good Job!"
                #correct_sound.play()
            else:
                print "WRONG! Please try again."
    def draw(self, canvas):
        # canvas.draw_text("", [10, 100], FONT_SIZE, FONT_COLOR)
        self._question.draw(canvas, [10, 100])
        choice = self._user_choice
        selected = False
        pos = [10, 200]
        for ch in CHOICE_LABELS:
            pos[0] = 10
            canvas.draw_text(ch + ": ", pos, FONT_SIZE, FONT_COLOR)
            pos[0] = 10 + FONT_SIZE * 2
            if ch == choice:
                selected = True
            self._choices[ch].draw(canvas, pos, selected)
            # pos[1] = pos[1] + FONT_SIZE * 2
            pos[1] = pos[1] + self._choices[ch].getHeight()
        if choice != None:
            msg = ""
            pos[0] = 100
            font_size = FONT_SIZE
            font_color = FONT_COLOR
            if choice == self.getCorrectData():
                msg = "Correct!! Good Job!"
                font_size = FONT_SIZE * 2
                font_color = 'Green'
            else:
                msg = "WRONG! Please try again."
                font_size = FONT_SIZE
                font_color = 'Red'
            pos[1] = pos[1] + FONT_SIZE * 2
            canvas.draw_text(msg, pos, font_size, font_color)
    def setUserChoice(self, choice):
        self._user_choice = choice

    def resetQuestion(self):
        correct = self._choices[self._correct]
        chlist = self._choices.values()
        random.shuffle(chlist)
        self._choices = conv_choice_list(chlist)
        self._correct = CHOICE_LABELS[chlist.index(correct)]
        self._user_choice = None

def restart():
    global quiz_started
    quiz_started = False

def nextQuestion():
    global quiz_started
    quiz_started = True
def resetQuestion():
    global current_question
    current_question.resetQuestion()

def prev():
    pass
def selectA():
    global current_question
    current_question.setUserChoice('A')
def selectB():
    global current_question
    current_question.setUserChoice('B')
def selectC():
    global current_question
    current_question.setUserChoice('C')
def selectD():
    global current_question
    current_question.setUserChoice('D')

current_question = Question(Data("What is 5 times 2?"), [Data('9'), Data('10'), Data('11'), Data('12')], 1)
def drawQuestion(canvas):
    global current_question
    canvas.draw_text("Question", [10, 30], FONT_SIZE, FONT_COLOR)
    canvas.draw_text("Score", [680, 30], FONT_SIZE, FONT_COLOR)
    canvas.draw_text(str(1), [20, 55], FONT_SIZE, FONT_COLOR)
    canvas.draw_text(str(1), [680, 55], FONT_SIZE, FONT_COLOR)
    current_question.draw(canvas)

def drawWelcomeScreen(canvas):
    canvas.draw_text("Welcome Shambhavi", [150, 100], 40, FONT_COLOR)
    canvas.draw_image(betu_image, betu_info.get_center(), betu_info.get_size(), [WIDTH / 2, HEIGHT / 2], betu_info.get_size())


def draw(canvas):
    global quiz_started
    # draw UI
    if quiz_started == False:
        drawWelcomeScreen(canvas)
    else:
        drawQuestion(canvas)

def setup_frame():
    # initialize stuff
    frame = simplegui.create_frame("QUIZ", WIDTH, HEIGHT)
    frame.set_canvas_background("Pink")
    # register handlers
    #frame.set_keyup_handler(keyup)
    #frame.set_keydown_handler(keydown)
    #frame.set_mouseclick_handler(click)
    frame.set_draw_handler(draw)
    frame.add_label("Game Controls")
    frame.add_button("Restart", restart, 100)
    frame.add_button("Next Question", nextQuestion, 100)
    # frame.add_button("Previous Question", prev, 100)
    frame.add_button("Reset Question", resetQuestion, 100)
    frame.add_label("Select Your Answer")
    frame.add_button("A", selectA, 100)
    frame.add_button("B", selectB, 100)
    frame.add_button("C", selectC, 100)
    frame.add_button("D", selectD, 100)
    #timer = simplegui.create_timer(1000.0, rock_spawner)
    # get things rolling
    #timer.start()
    frame.start()


def main():
    '''
    main function for testing
    :return: None
    '''
    # welcome_sound.play()
    setup_frame()
    global current_question
    current_question.printQuestion()
    current_question.printQuestion('A')
    current_question.printQuestion('C')
    current_question.resetQuestion()
    current_question.printQuestion()
    current_question.printQuestion('C')
    current_question.printQuestion(q1.getCorrectData())


if __name__ == '__main__':
    main()