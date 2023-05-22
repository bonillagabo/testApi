class Archivo():
    def __init__(self, filePath):
        self.input = filePath
        self.password = ''
        self.pages = '1'
        self.output = None
        self.convert_white = False
        self.noligatures = False
        self.extra_spaces = False
        self.mode = 'layout'
        self.noformfeed = False
        self.grid = 2
        self.fontsize = 3
        self.skip_empty = False