from textClass import Colors as c
class MiniContent:
    def __init__(self, text : list[str] = []) -> None:
        self.result = ''
        if text:
            for i in text:
                self.result += f'\n\t- {i}'


    def __repr__(self) -> str:
        return self.result
    


class TablePart:
    def __init__(self, row_name, many_content) -> None:
        self.name = '#'+row_name + '\n'
        self.many = many_content
        for i in range(len(self.name)):
            self.name += '#'
        for j in self.many:
            self.name += '\n#' + j


        self.name += '\n'

    def __repr__(self) -> str:
        return self.name