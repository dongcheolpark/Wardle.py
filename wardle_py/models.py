# <wardle>
class Wardle:

    def __init__(self):
        self.answerString = ''

    def get_answerString(self):
        return self.answerString


class WardleOriginal(Wardle):

    def __init__(self):
        self.answerString = AnswerString()


# </wardle>

# <answerString>
class AnswerString:

    def __init__(self):
        return

# </answerString>
