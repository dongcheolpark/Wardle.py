from wordle_py.models import *


class Wordle:

    def __init__(self):
        self.answer_String = AnswerString()

    def get_answerString(self):
        return self.answer_String


class WordleOriginal(Wordle):

    def __init__(self):
        self.answer_String = AnswerStringEnglish()


