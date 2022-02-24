from wardle_py.models import *


class Wardle:

    def __init__(self):
        self.answer_String = AnswerString()

    def get_answerString(self):
        return self.answer_String


class WardleOriginal(Wardle):

    def __init__(self):
        self.answer_String = AnswerStringEnglish()


