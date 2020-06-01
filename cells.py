class Start:
    def __init__(self):
        self.display = 'X'


class End:
    def __init__(self):
        self.display = 'Y'


class Air:
    def __init__(self):
        self.display = ' '


class Wall:
    def __init__(self):
        self.display = '*'


class Fire:
    def __init__(self):
        self.display = 'F'


class Water:
    def __init__(self):
        self.display = 'W'


class Teleport:
    def __init__(self, x):  # use the parameter x to get different teleport 0-9
        self.display = str(x)

