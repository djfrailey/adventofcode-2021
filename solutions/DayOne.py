from inputs import DayOne

class PartOne:
    def run(self, input: list[int]) -> int:
        num_increases: int = 0
        prev_amount: int = input[0]
        for amount in input:
            if amount > prev_amount:
                num_increases += 1
            prev_amount = amount
        return num_increases

    def solve(self):
        return self.run(DayOne.input)

class PartTwo:
    def run(self, input: list[int]) -> int:
        window_sums : list[int] = []
        for idx, value in enumerate(input):
            window = input[idx:idx+3]
            if (len(window) == 3):
                window_sums.append(sum(window))
        return PartOne().run(window_sums)

    def solve(self):
        return self.run(DayOne.input)