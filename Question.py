'''
Base Question class for Quiz
'''
import random

CHOICE_LABELS = ['A', 'B', 'C', 'D']

def conv_choice_list(ch):
    choices = {}
    for i in range(len(ch)):
        choices[CHOICE_LABELS[i]] = ch[i]
    return choices

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
q1_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

welcome_sound = simplegui.load_sound("https://www.dropbox.com/s/aboqginatbi5tpe/Welcome.mp3?dl=0")
wrong_sound   = simplegui.load_sound("https://www.dropbox.com/s/4wy0o9lsdgeh729/Wrong.mp3?dl=0")
correct_sound = simplegui.load_sound("https://www.dropbox.com/s/stu10xsbzd9svcd/Right.mp3?dl=0")

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


def main():
    '''
    main function for testing
    :return: None
    '''
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
