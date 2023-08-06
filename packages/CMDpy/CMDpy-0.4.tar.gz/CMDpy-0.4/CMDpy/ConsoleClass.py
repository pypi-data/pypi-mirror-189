import textClass
from datetime import datetime
from time import sleep as s
from random import randrange

class Console:
    LOG_COUNT = 0


    def __printer__(self, text : str = '', proportion : textClass.Proportion = textClass.Proportion(), is_return : bool = False) -> str | None:
        if is_return:
            return proportion.mode + text
        else:
            print(proportion.mode + text)


    def print(self, text : str = '', proportion : textClass.Proportion = textClass.Proportion()):
        self.__printer__(text, proportion)



    def __init__(self) -> None:
        self.colorsCLS = textClass.Colors()


    @classmethod
    def auto_random_load(cls, seconds : int = 0, text : list[str] = []):
        cls.load(seconds, randrange(0, 4), text)


    @classmethod
    def load(cls, seconds : int = 0, delay : int = 1, text : list[str] = []):
        for i in range(seconds):
            cls.log(text[i])
            s(delay)


    @classmethod
    def log(cls, text):
        cls.LOG_COUNT += 1
        color = textClass.Colors()
        print(f'{color.GREEN}[{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}]{color.RESET} {text}{color.TABULATE}{cls.LOG_COUNT}')