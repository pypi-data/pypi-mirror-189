class Colors:
    START                        = '\033['
    WHITE                        = START+'37m'
    BLACK                        = START+'30m'
    RED                          = START+'31m'
    GREEN                        = START+'32m'
    BLUE                         = START+'34m'
    YELLOW                       = START+'33m'
    PURPLE                       = START+'35m'
    MAGENTA                      = START+'36m'


    WHITE_LIGHT                  = START+'97m'
    BLACK_LIGHT                  = START+'90m'
    RED_LIGHT                    = START+'91m'
    GREEN_LIGHT                  = START+'92m'
    BLUE_LIGHT                   = START+'94m'
    YELLOW_LIGHT                 = START+'93m'
    PURPLE_LIGHT                 = START+'95m'
    MAGENTA_LIGHT                = START+'96m'


    RESET                        = START+'0m'
    BOLD                         = START+'1m'
    UNDERLINE                    = START+'4m'
    ITALIC                       = START+'3m'
    DELETED                      = START+'9m'
         
         
    BACKGROUND_WHITE             = START+'47m'
    BACKGROUND_BLACK             = START+'40m'
    BACKGROUND_RED               = START+'41m'
    BACKGROUND_GREEN             = START+'42m'
    BACKGROUND_BLUE              = START+'44m'
    BACKGROUND_YELLOW            = START+'43m'
    BACKGROUND_PURPLE            = START+'45m'
    BACKGROUND_MAGENTA           = START+'46m'


    TABULATE = '\t\t\t\t\t\t'


class Proportion:
    def __init__(self, mode: str = '') -> None:
        self.text                       = ''
        self.mode : str                 = mode
        self.modes : list[str]          = mode.lower().split(' ')

        for _mode in self.modes:
            #color

            if _mode == 'purple':
                self.text += Colors().PURPLE
                
            if _mode == 'magenta':
                self.text += Colors().MAGENTA
                
            if _mode == 'red':
                self.text += Colors().RED
            
            if _mode == 'yellow':
                self.text += Colors().YELLOW
            
            if _mode == 'blue':
                self.text += Colors().BLUE

            if _mode == 'green':
                self.text += Colors().GREEN

            if _mode == 'white':
                self.text += Colors().WHITE

            if _mode == 'black':
                self.text += Colors().BLACK

            #background

            if _mode == 'background_purple':
                self.text += Colors().BACKGROUND_PURPLE
                
            if _mode == 'background_magenta':
                self.text += Colors().BACKGROUND_MAGENTA
                
            if _mode == 'background_red':
                self.text += Colors().BACKGROUND_RED
            
            if _mode == 'background_yellow':
                self.text += Colors().BACKGROUND_YELLOW
            
            if _mode == 'background_blue':
                self.text += Colors().BACKGROUND_BLUE

            if _mode == 'background_green':
                self.text += Colors().BACKGROUND_GREEN

            if _mode == 'background_white':
                self.text += Colors().BACKGROUND_WHITE

            if _mode == 'background_black':
                self.text += Colors().BACKGROUND_BLACK

            #light color
            if _mode == 'light_purple':
                self.text += Colors().PURPLE_LIGHT
                
            if _mode == 'light_magenta':
                self.text += Colors().MAGENTA_LIGHT
                
            if _mode == 'light_red':
                self.text += Colors().RED_LIGHT
            
            if _mode == 'light_yellow':
                self.text += Colors().YELLOW_LIGHT
            
            if _mode == 'light_blue':
                self.text += Colors().BLUE_LIGHT

            if _mode == 'light_green':
                self.text += Colors().GREEN_LIGHT

            if _mode == 'light_white':
                self.text += Colors().WHITE_LIGHT

            if _mode == 'light_black':
                self.text += Colors().BLACK_LIGHT


            #effects

            if _mode == 'bold':
                self.text += Colors().BOLD
            if _mode == 'italic':
                self.text += Colors().ITALIC
            if _mode == 'underline':
                self.text += Colors().UNDERLINE

            if _mode == 'strike_through':
                self.text += Colors().BLACK + Colors().DELETED
            #comment mode
            if _mode == 'comment':
                self.text += Colors().ITALIC + Colors().BLACK


            if _mode == 'help':
                print(dir(Colors))



class Text:
    def __init__(self, proportion : Proportion = Proportion('white'), text : str = '', mode_write : str = 'left') -> None:
        self.proportion : str           = proportion.text
        self.text                       = text
        self.gy = False
        if self.text.startswith('#'):
            self.gy = True
        self.result = ''
        self.a_text                     = list(text)
        match mode_write:

            case 'left':
                for index in range(len(text)):
                    if index % 20 == 0:
                        if self.a_text[index] == ' ':
                            self.a_text[index] = '\n'
                        else: 
                            self.a_text.insert(index, '\n')


                for i in self.a_text:
                    self.result += i

            case 'full':
                for index in range(len(text)):
                    if index % 60 == 0:
                        self.a_text.insert(index, '\n')

                for i in self.a_text:
                    self.result += i


            case 'center':
                for index in range(len(text)):
                    if index % 10 == 0:
                        self.a_text.insert(index, '\n\t')

                for i in self.a_text:
                    self.result += i


            case 'space_line':
                for index in range(len(text)):
                    if self.a_text[index] == ' ':
                        self.a_text[index] = '\n'

                for i in self.a_text:
                    self.result += i


            case _:
                for i in self.a_text:
                    self.result += i


        if self.gy:
            self.text                       = Colors().ITALIC + Colors().BLACK +  self.proportion + self.result
        else:
            self.text                       = self.proportion + self.result



    def __repr__(self) -> str:
        return self.text
    
    def __del__(self):
        print(Colors().RESET)


        del self