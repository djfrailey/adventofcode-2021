class DayOneSolution:
    def run(self, input: list[int]) -> int:
        num_increases: int = 0
        prev_amount: int = input[0]
        for amount in input:
            if amount > prev_amount:
                num_increases += 1
            prev_amount = amount
        return num_increases
