from inputs import DayOne
from solutions import DayOneSolution

def run(m):
    def execute(s):
        header = "====== %s.%s ======" % (m.__name__, s.__name__)
        print(header)
        result = s().solve()
        print(result)
        print("=" * len(header))
    if (m.PartOne):
        execute(m.PartOne)
    if (m.PartTwo):
        execute(m.PartTwo)

run(DayOneSolution)