from abc import abstractmethod


# <answerString>
class AnswerString:
    size = 0

    def __init__(self):
        self.text = []
        return

    def getTextList(self):
        return self.text

    def getsize(self):
        return self.size

    @abstractmethod
    def toString(self):
        return

    def CheckString(self, string):
        res = []
        _text = string.getTextList()
        if string.getsize() != self.size:
            raise Exception('Each string is not the same size.')
        for i in range(self.size):
            res.append(0)
            for j in range(self.size):
                if _text[i] == self.text[j]:
                    if i == j:
                        res[i] = 2
                        break
                    else:
                        res[i] = 1
        return res


class AnswerStringEnglish(AnswerString):

    def __init__(self, text=None):
        if text:
            self.text = [];
            for i in text:
                self.text.append(i)
            self.size = len(self.text)
        else:
            super().__init__()
        return

    def toString(self):
        res = ''
        for i in self.text:
            res += i
        return res


# </answerString>
# <answerStringFactory>


class AnswerStringFactory:

    def __int__(self):
        return

    def getString(self, type, string):
        if type == 'original':
            return AnswerStringEnglish(string)
