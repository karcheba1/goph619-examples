class MyClass:

    def __init__(self, x=0.):
        self.x = x
        self.name = 'an object of MyClass'

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        x = float(value)
        self._x = x

    def print_x(self):
        print(f'x: {self.x}')
