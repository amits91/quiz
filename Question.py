'''
Base Question class for Quiz
Codeskulptor Link: http://www.codeskulptor.org/#user40_nva4UorE3O_2.py
'''
'''
Base Question class for Quiz
'''
import random
DESKTOP = True
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

CHOICE_LABELS = ['A', 'B', 'C', 'D']
WIDTH = 800
HEIGHT = 600
FONT_COLOR = 'Black'

def conv_choice_list(ch):
    choices = {}
    for i in range(len(ch)):
        choices[CHOICE_LABELS[i]] = ch[i]
    return choices

class Data:
    def __init__(self, text, img = None):
        self._text = text
        self._img = img
    def getText(self):
        return self._text
    def __str__(self):
        return str(self._text)
    def draw(self, pos, isSelected = False):
        pass


class Question:
    '''
    Textual Question
    '''
    def __init__(self, question, choice_list, correct_idx):
        self._question = question
        self._choices = conv_choice_list(choice_list)
        self._correct = CHOICE_LABELS[correct_idx]
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
    def drawQuestion(self, choice = None):
        # self.draw(choice)
        pass
    def resetQuestion(self):
        correct = self._choices[self._correct]
        chlist = self._choices.values()
        random.shuffle(chlist)
        self._choices = conv_choice_list(chlist)
        self._correct = CHOICE_LABELS[chlist.index(correct)]

def restart():
    pass
def nextQuestion():
    pass
def prev():
    pass
def selectA():
    pass
def selectB():
    pass
def selectC():
    pass
def selectD():
    pass

def drawQuestion(canvas):
    canvas.draw_text("Question", [50, 50], 22, FONT_COLOR)
    canvas.draw_text("Score", [680, 50], 22, FONT_COLOR)
    canvas.draw_text(str(1), [50, 80], 22, FONT_COLOR)
    canvas.draw_text(str(1), [680, 80], 22, FONT_COLOR)

def drawWelcomeScreen(canvas):
    canvas.draw_text("Welcome Shambhavi", [150, 100], 40, FONT_COLOR)
    canvas.draw_image(betu_image, betu_info.get_center(), betu_info.get_size(), [WIDTH / 2, HEIGHT / 2], betu_info.get_size())


def draw(canvas):
    # draw UI
    drawWelcomeScreen(canvas)

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
    frame.add_button("Previous Question", prev, 100)
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
    q1 = Question("Test Question", [Data('1'), Data('2'), Data('3'), Data('4')], 2)
    q1.printQuestion()
    q1.printQuestion('A')
    q1.printQuestion('C')
    q1.resetQuestion()
    q1.printQuestion()
    q1.printQuestion('C')
    q1.printQuestion(q1.getCorrectData())


if __name__ == '__main__':
    main()