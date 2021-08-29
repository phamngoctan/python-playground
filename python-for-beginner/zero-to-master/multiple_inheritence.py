class User:
    def login(self):
        print('Logged in')
class Wizard(User):
    def __init__(self, name, power) -> None:
        self._name = name
        self._power = power
    def check_power(self):
        print(f'{self._power} remaining')

class Archer(User):
    def __init__(self, name, arrows) -> None:
        self._name = name
        self._arrows = arrows
    def check_arrows(self):
        print(f'{self._arrows} remaining')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows) -> None:
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

hb1 = HybridBorg('Borgie', 50, 100)
hb1.check_arrows()
hb1.check_power()
hb1.login()
