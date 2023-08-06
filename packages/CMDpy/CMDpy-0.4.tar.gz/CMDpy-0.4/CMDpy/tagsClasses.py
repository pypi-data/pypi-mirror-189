from textClass import Colors
class HTML:
    @staticmethod
    def p(text) -> str:
        return '\t' + text + Colors().RESET
    
    @staticmethod
    def h1(text) -> str:
        return Colors().BOLD + Colors().TABULATE + text + Colors().RESET
    

    @staticmethod
    def u(text) -> str:
        return Colors().UNDERLINE + text
    

    @staticmethod
    def b(text) -> str:
        return Colors().BOLD + text
    