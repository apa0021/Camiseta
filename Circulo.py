import math
class Circulo:
    def __init__(self, radio:float):
        self.radio=radio
    def area(self):
        return math.pi()*self.radio**2
    def circunferencia(self):
        return 2*math.pi()*self.radio
        