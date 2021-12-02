from inputs import DayTwo

class Pilot:
    def __init__(self, submarine):
        self.submarine = submarine

    def make_it_so(self, input : list[str]):
        for command in input:
            method, argument = command.split(' ')
            submarine_command = getattr(self.submarine, method)
            submarine_command(int(argument))

class Submarine:
    def __init__(self):
        self.position = [0, 0]

    def forward(self, amount : int):
        self.position[0] += amount
    
    def down(self, amount: int):
        self.position[1] += amount

    def up (self, amount: int):
        self.position[1] -= amount

class AimableSubmarine:
    def __init__(self):
        self.position = {"h": 0, "d": 0, "a": 0}

    def forward(self, amount : int):
        self.position["h"] += amount
        self.position["d"] += amount * self.position["a"]

    def up(self, amount : int):
        self.position["a"] -= amount

    def down(self, amount: int):
        self.position["a"] += amount
class PartOne:
    def __init__(self):
        self.submarine = Submarine()

    def run(self, input : list[str]):
        Pilot(self.submarine).make_it_so(input)

    def solve(self) -> int:
        self.run(DayTwo.input)
        return self.submarine.position[0] * self.submarine.position[1]

class PartTwo:
    def __init__(self):
        self.submarine = AimableSubmarine()

    def run(self, input : list[str]):
        Pilot(self.submarine).make_it_so(input)

    def solve(self) -> int:
        self.run(DayTwo.input)
        return self.submarine.position["h"] * self.submarine.position["d"]