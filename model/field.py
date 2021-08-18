import re
class Field:

    def __init__(self,raw_code):
        self.raw_code = raw_code
        self.parser()

    def parser(self):
        pass
    

    def __str__(self):
        return self.raw_code
