from wordle_py.models import *
import random


class Wordle:

    turn = 0

    def __init__(self):
        self.answer_String = AnswerString()

    def get_answerString(self):
        return self.answer_String

    def checkString(self, string):
        res = self.answer_String.CheckString(string)
        self.turn -= 1
        return res

    def getTurn(self):
        return self.turn
    @abstractmethod
    def setAnswer(self, string):
        return

    @abstractmethod
    def setAnswer(self):
        return


class WordleOriginal(Wordle):

    AnswerList = [
        "roast",
        "aaron",
    ]

    def __init__(self):
        self.answer_String = AnswerStringEnglish()
        self.turn = 6

    def setAnswer(self, string=None):
        if string:
            self.answer_String = AnswerStringEnglish(string)
        else:
            size = len(self.AnswerList)
            self.answer_String = AnswerStringEnglish(self.AnswerList[random.randrange(0, size-1)])
