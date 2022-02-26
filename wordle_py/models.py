from abc import abstractmethod


# <answerString>
class AnswerString:

    def __init__(self):
        self.text = []
        return

    def getTextList(self):
        return self.text

    @abstractmethod
    def toString(self):
        return

    def CheckString(self, string):
        res = []
        _text = string.getTextList()
        for i in range(len(_text)):
            res.append(0)
            for j in range(len(_text)):
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
        else:
            super().__init__()
        return

    def toString(self):
        res = ''
        for i in self.text:
            res += i
        return res

# </answerString>
