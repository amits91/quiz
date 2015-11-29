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
SCORE_X = 680
SCORE_Y = 25
QUES_X = 10
TRIES_X = QUES_X + (10 * FONT_SIZE)
TIMER_X = (SCORE_X - QUES_X)/2
quiz_started = False
quiz_finished = False
current_question = None
timeSec = 0
timer = None
quiz = None

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

class Data:
    def __init__(self, text):
        self._text = text
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
        font_color = FONT_COLOR
        if isSelected == True:
            font_color = 'Blue'
        canvas.draw_text(self._text, pos, FONT_SIZE, font_color)

def conv_choice_list(ch):
    choices = {}
    for i in range(len(ch)):
        choices[CHOICE_LABELS[i]] = Data(str(ch[i]))
    return choices

class QuestionData(Data):
    def __init__(self, text, choice_list, correct_idx):
        Data.__init__(self, text)
        self._choices = conv_choice_list(choice_list)
        self._correct = CHOICE_LABELS[correct_idx]
    def getChoices(self):
        return self._choices
    def getCorrectChoice(self):
        return self._correct
    def randomizeData(self):
        correct = self._choices[self._correct]
        chlist = self._choices.values()
        random.shuffle(chlist)
        self._choices = conv_choice_list(chlist)
        self._correct = CHOICE_LABELS[chlist.index(correct)]
    def isCorrectChoice(self, choice):
        if choice == self._correct:
            return True
        else:
            return False
    def __str__(self):
        qstr = "Question: " + str(self._text)
        qstr = qstr + '\n'
        for ch in CHOICE_LABELS:
            qstr = qstr + ch + ': ' + str(self._choices[ch]) + "\n"
        return qstr

def timer_handler():
    global timeSec
    timeSec +=1

def startTimer():
    global timeSec, timer
    timeSec = 0
    if timer != None:
        timer.start()

def stopTimer():
    global timeSec, timer
    if timer != None:
        timer.stop()
    return timeSec

class Question:
    '''
    Textual Question
    '''
    def __init__(self, question):
        self._question = question
        self._user_choice = None
        self._elapsedTime = 0
        self._numTries = 0

    def getNumTries(self):
        return self._numTries

    def getElapsedTime(self):
        return self._elapsedTime
    def startTimer(self):
        self._elapsedTime = 0
        startTimer()
    def stopTimer(self):
        self._elapsedTime = stopTimer()
    def getCorrectData(self):
        return self._question.getCorrectChoice()
    def __str__(self):
        return str(self._question)
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
            font_size = FONT_SIZE
            font_color = FONT_COLOR
            if ch == choice:
                selected = True
                font_color = 'Blue'
            else:
                selected = False
                font_color = FONT_COLOR
            canvas.draw_text(ch + ": ", pos, font_size, font_color)
            pos[0] = 10 + font_size * 2
            self._question.getChoices()[ch].draw(canvas, pos, selected)
            # pos[1] = pos[1] + FONT_SIZE * 2
            pos[1] = pos[1] + self._question.getChoices()[ch].getHeight()
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
        self._numTries += 1
        self._user_choice = choice
    def isCorrect(self):
        if self._question.isCorrectChoice(self._user_choice):
            return 1
        else:
            return 0
    def resetQuestion(self):
        self._question.randomizeData()
        self.stopTimer()
        self._user_choice = None
        self._elapsedTime = 0
        self._numTries = 0

class Quiz:

    def reset(self):
        self._finished = False
        self._curr_idx = -1
        self._curr_question = None
        self._score = 0
        for i in range(self.getNumQuestions()):
            self._questions[i].resetQuestion()

    def __init__(self, questions):
        self._questions = [Question(qd) for qd in questions]
        self.reset()

    def getAllQuestions(self):
        return self._questions

    def getNumQuestions(self):
        return len(self._questions)

    def currQuestionNum(self):
        return self._curr_idx + 1

    def getQuestion(self, qno):
        return self._questions[qno - 1]

    def score(self):
        return self._score

    def latestScore(self):
        tempScore = 0
        if self._finished == False and self._curr_question != None:
            tempScore = self._curr_question.isCorrect()
        return self._score + tempScore

    def getQuesTime(self):
        if self._finished == False:
            return timeSec
        elif self._curr_question != None:
            return self._curr_question.getElapsedTime()
        else:
            return 0


    def currentQuestion(self):
        return self._curr_question

    def nextQuestion(self):
        num = self.getNumQuestions()
        if self._finished == False and self._curr_question != None:
            self._score += self._curr_question.isCorrect()
            self._curr_question.stopTimer()
        self._curr_idx += 1
        if self._curr_idx == num:
            self._finished = True
            self._curr_idx -= 1
        self._curr_question = self._questions[self._curr_idx]
        if self._finished == False:
            self._curr_question.startTimer()

    def prevQuestion(self):
        if self._finished:
            self._curr_idx = (self._curr_idx - 1) % self.getNumQuestions()
            self._curr_question = self._questions[self._curr_idx]

    def draw(self, canvas):
        if self._curr_question == None:
            canvas.draw_text("Welcome Shambhavi", [150, 100], 40, FONT_COLOR)
            canvas.draw_image(betu_image, betu_info.get_center(), betu_info.get_size(), [WIDTH / 2, HEIGHT / 2], betu_info.get_size())
        else:
            canvas.draw_text("Question", [QUES_X, SCORE_Y], FONT_SIZE, FONT_COLOR)
            canvas.draw_text("Tries", [TRIES_X, SCORE_Y], FONT_SIZE, FONT_COLOR)
            canvas.draw_text("Elapsed Time", [TIMER_X, SCORE_Y], FONT_SIZE, FONT_COLOR)
            canvas.draw_text("Score", [SCORE_X, SCORE_Y], FONT_SIZE, FONT_COLOR)
            canvas.draw_text(str(self.currQuestionNum()), [QUES_X + 10, SCORE_Y + FONT_SIZE + 5], FONT_SIZE, FONT_COLOR)
            canvas.draw_text(str(self._curr_question.getNumTries()), [TRIES_X + 10, SCORE_Y + FONT_SIZE + 5], FONT_SIZE, FONT_COLOR)
            canvas.draw_text(str(self.getQuesTime()) + " sec", [TIMER_X + 10, SCORE_Y + FONT_SIZE + 5], FONT_SIZE, FONT_COLOR)
            canvas.draw_text(str(self.latestScore()) + '/' + str(self.getNumQuestions()), [SCORE_X + 10, SCORE_Y + FONT_SIZE + 5], FONT_SIZE, FONT_COLOR)
            self._curr_question.draw(canvas)
            if self._finished == True:
                canvas.draw_text("Finished. Press 'Restart' to start new game. 'Review' to review.", [50, HEIGHT - 50], 20, 'Red')

    def setUserChoice(self, choice):
        if self._finished == False and self._curr_question != None:
            self._curr_question.setUserChoice(choice)

class QuestionDataTimesSum(QuestionData):
    def randomizeData(self):
        self._times = random.randint(2, 11)
        self._num = random.choice([10, 25, 20, 50, random.randint(2, 10)])
        self._text = "What is {0} times {1}?".format(str(self._times), str(self._num))
        t = self._times
        n = self._num
        self._choices = conv_choice_list([str(t * n), str(t + n), str(abs((t + 1) * n)), str((t - 1) * n)])
        self._correct = CHOICE_LABELS[0]
        QuestionData.randomizeData(self)
    def __init__(self):
        self.randomizeData()


class QuestionDataGreatSmall(QuestionData):
    def randomizeData(self):
        self._listsz = random.randint(8, 13)
        self._nums = random.sample(range(1, 100), self._listsz)
        self._text = "What is the difference between the greatest and smallest number?\n {0}".format(str(self._nums))
        sorted_list = sorted(self._nums)
        a = abs(sorted_list[0] - sorted_list[-1])
        b = abs(sorted_list[1] - sorted_list[-1])
        c = abs(sorted_list[0] - sorted_list[-2])
        d = 'None of these'
        self._choices = conv_choice_list([a, b, c, d])
        self._correct = CHOICE_LABELS[0]
        QuestionData.randomizeData(self)
    def __init__(self):
        self.randomizeData()

class QuestionDataDivideGirls(QuestionData):
    def randomizeData(self):
        self._num = random.randint(2, 5)
        self._girls = random.randint(3, 6)
        self._girls2 = random.randint(1, self._girls - 1)
        if self._girls2 == 1:
            girlstr = 'girl'
        else:
            girlstr = 'girls'
        self._text = "Divide {0} chocolates equally between {1} girls. How many will {2} {3} get?" \
            .format(str(self._num * self._girls),
                    str(self._girls),
                    str(self._girls2),
                    girlstr
                    )
        a = self._num * self._girls2
        b = self._num * self._girls2 - 1
        c = self._num * self._girls2 + 1
        d = self._num * self._girls
        self._choices = conv_choice_list([a, b, c, d])
        self._correct = CHOICE_LABELS[0]
        QuestionData.randomizeData(self)
    def __init__(self):
        self.randomizeData()

class QuestionDataDivideGroups(QuestionData):
    def randomizeData(self):
        self._num = random.randint(2, 5)
        self._groups = random.randint(3, 6)
        self._text = "How many groups of {0} pencils can be formed from {1} pencils?" \
            .format(
            str(self._groups),
            str(self._num * self._groups))
        a = self._num
        b = self._num + 1
        c = self._num - 1
        d = self._groups
        self._choices = conv_choice_list([a, b, c, d])
        self._correct = CHOICE_LABELS[0]
        QuestionData.randomizeData(self)
    def __init__(self):
        self.randomizeData()

class QuestionDataBorrowSub(QuestionData):
    def randomizeData(self):
        d1 = random.randint(0, 10) * 10
        d2 = random.randint(0, 10) * 10
        self._bnum = max(d1, d2)
        self._snum = min(d1, d2)
        d1 = random.randint(0, 10)
        d2 = random.randint(0, 10)
        self._bnum += min(d1, d2)
        self._snum += max(d1, d2)
        if self._bnum < self._snum:
            self._bnum, self._snum = self._snum, self._bnum
        self._text = "What is {0} - {1}?" \
            .format(str(self._bnum), str(self._snum))
        a = self._bnum - self._snum
        b = abs(a - 1)
        c = a + 1
        d = self._bnum + self._snum
        self._choices = conv_choice_list([a, b, c, d])
        self._correct = CHOICE_LABELS[0]
        QuestionData.randomizeData(self)
    def __init__(self):
        self.randomizeData()
questions = [
    QuestionDataDivideGroups(),
    QuestionDataDivideGirls(),
    QuestionDataDivideGroups(),
    QuestionDataDivideGirls(),
    QuestionDataDivideGroups(),
    QuestionDataDivideGirls(),
    QuestionDataDivideGroups(),
    QuestionDataBorrowSub(),
    QuestionDataDivideGirls(),
    QuestionDataTimesSum(),
    QuestionDataGreatSmall()]

def init_game():
    quiz.reset()

def restart():
    init_game()

def nextQuestion():
    quiz.nextQuestion()

def resetQuestion():
    quiz.currentQuestion().resetQuestion()

def prev():
    quiz.prevQuestion()

def selectA():
    quiz.setUserChoice('A')
def selectB():
    quiz.setUserChoice('B')
def selectC():
    quiz.setUserChoice('C')
def selectD():
    quiz.setUserChoice('D')

def draw(canvas):
    quiz.draw(canvas)

def setup_frame():
    # initialize stuff
    global timer, quiz, questions
    quiz = Quiz(questions)
    frame = simplegui.create_frame("QUIZ", WIDTH, HEIGHT)
    timer = simplegui.create_timer(1000, timer_handler)
    frame.set_canvas_background("Pink")
    # register handlers
    #frame.set_keyup_handler(keyup)
    #frame.set_keydown_handler(keydown)
    #frame.set_mouseclick_handler(click)
    frame.set_draw_handler(draw)
    frame.add_label("Game Controls")
    frame.add_button("Restart", restart, 100)
    frame.add_button("Next Question", nextQuestion, 100)
    frame.add_button("Review Question", prev, 100)
    # frame.add_button("Reset Question", resetQuestion, 100)
    frame.add_label("Select Your Answer")
    frame.add_button("A", selectA, 100)
    frame.add_button("B", selectB, 100)
    frame.add_button("C", selectC, 100)
    frame.add_button("D", selectD, 100)
    # get things rolling
    init_game()
    frame.start()


def main():
    '''
    main function for testing
    :return: None
    '''
    # welcome_sound.play()
    setup_frame()
    # global current_question
    # current_question.printQuestion()
    # current_question.printQuestion('A')
    # current_question.printQuestion('C')
    # current_question.resetQuestion()
    # current_question.printQuestion()
    # current_question.printQuestion('C')
    # current_question.printQuestion(q1.getCorrectData())


if __name__ == '__main__':
    main()