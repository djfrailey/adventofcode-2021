from inputs import DayTwo

class Submarine:
    def __init__(self):
        self.position = [0, 0]

    def forward(self, amount : int):
        self.position[0] += amount
    
    def down(self, amount: int):
        self.position[1] += amount

    def up (self, amount: int):
        self.position[1] -= amount

class PartOne:
    def __init__(self):
        self.submarine = Submarine()

    def run(self, input : list[str]):
        for command in input:
            method, argument = command.split(' ')
            submarine_command = getattr(self.submarine, method)
            submarine_command(int(argument))

    def solve(self) -> int:
        self.run(DayTwo.input)
        return self.submarine.position[0] * self.submarine.position[1]