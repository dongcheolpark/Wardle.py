from abc import abstractmethod


# <answerString>
class AnswerString:

    def __init__(self):
        self.text = []
        return

    @abstractmethod
    def toString(self):
        return


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
