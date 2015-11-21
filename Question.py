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


class Choice:
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
    def getCorrectChoice(self):
        return self._correct
    def __str__(self):
        qstr = "Question: " + self.getInstruction()
        qstr = qstr + '\n'
        qstr = qstr + "Figure: None\n"
        for ch in CHOICE_LABELS:
            qstr = qstr + ch + ': ' + str(self._choices[ch]) + "\n"
        return qstr
    def printQuestion(self, choice = None):
        print self
        if choice != None:
            print 'You entered', choice, ',',
            if choice == self.getCorrectChoice():
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
    q1 = Question("Test Question", [Choice('1'), Choice('2'), Choice('3'), Choice('4')], 2)
    q1.printQuestion()
    q1.printQuestion('A')
    q1.printQuestion('C')
    q1.resetQuestion()
    q1.printQuestion()
    q1.printQuestion('C')
    q1.printQuestion(q1.getCorrectChoice())

if __name__ == '__main__':
    main()
