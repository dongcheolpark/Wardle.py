from wordle_py.models import *


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
    def setAnswer(self):
        return


class WordleOriginal(Wordle):

    def __init__(self):
        self.answer_String = AnswerStringEnglish()
        self.turn = 6

    def setAnswer(self,string):
        self.answer_String = AnswerStringEnglish(string)


