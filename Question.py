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
        qstr = qstr + "A:" + str(self._choices[0]) + "\n"
        qstr = qstr + "B:" + str(self._choices[1]) + "\n"
        qstr = qstr + "C:" + str(self._choices[2]) + "\n"
        qstr = qstr + "D:" + str(self._choices[3])
        return qstr
    def showQuestion(self, choice = 0):
        print self
        if choice > 0:
            print 'You entered', CHOICE[choice]
            if choice == self.getCorrectChoice():
                print "Correct!! Good Job!"
            else:
                print "WRONG! Please try again."
    def resetQuestion(self):
        correct = self._choices[self._correct]
        random.shuffle(self._choices)
        self._correct = self._choices.index(correct)


def main():
    '''
    main function for testing
    :return: None
    '''
    q1 = Question()
    q1.showQuestion()
    q1.showQuestion(1)
    q1.showQuestion(2)
    q1.resetQuestion()
    q1.showQuestion()
    q1.showQuestion(2)
    q1.showQuestion(q1.getCorrectChoice())

if __name__ == '__main__':
    main()
