import os

from wordle_py.models import *
import random
import csv


class Wordle:

    turn = 0
    AnswerList = []

    def __init__(self, string):
        self.answer_String = AnswerString()
        self.AnswerListSource = string

        f = open(self.AnswerListSource, 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.AnswerList.append(line[0])
        f.close()

    def get_answerString(self):
        return self.answer_String

    def checkString(self, string, isDictionary=False):
        if isDictionary:
            check = False
            for item in self.AnswerList:
                if string.toString() == item:
                    check = True
            if not check:
                return False
        res = self.answer_String.CheckString(string)
        self.turn -= 1
        return res

    def getTurn(self):
        return self.turn

    def setAnswer(self, type, string=None, ):
        if string:
            self.answer_String = AnswerStringFactory().getString(type, string)
        else:
            size = len(self.AnswerList)
            self.answer_String = AnswerStringFactory().getString(type, self.AnswerList[random.randrange(0, size-1)])


class WordleOriginal(Wordle):

    def __init__(self):
        super().__init__(os.path.dirname(__file__)+'/AnswerLists/AnswerListOriginal.csv');
        self.answer_String = AnswerStringEnglish()
        self.turn = 6

    def setAnswer(self, string=None):
        super(WordleOriginal, self).setAnswer('original', string)
