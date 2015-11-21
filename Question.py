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
        for ch in CHOICE_LABELS:
            qstr = qstr + ch + ': ' + self._choices[ch] + "\n"
        return qstr
    def showQuestion(self, choice = 0):
        print self
        if choice > 0:
            print 'You entered', choice, ',',
            if choice == self.getCorrectChoice():
                print "Correct!! Good Job!"
            else:
                print "WRONG! Please try again."
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
    q1 = Question("Test Question", ['1', '2', '3', '4'], 2)
    q1.showQuestion()
    q1.showQuestion(1)
    q1.showQuestion(2)
    q1.resetQuestion()
    q1.showQuestion()
    q1.showQuestion(2)
    q1.showQuestion(q1.getCorrectChoice())

if __name__ == '__main__':
    main()
