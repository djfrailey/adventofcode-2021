from solutions import DayOne, DayTwo

def run(m):
    def execute(s):
        header = "====== %s.%s ======" % (m.__name__, s.__name__)
        print(header)
        result = s().solve()
        print(result)
        print("=" * len(header))
        
    members = dir(m)
    if ("PartOne" in members):
        execute(m.PartOne)
    if ("PartTwo" in members):
        execute(m.PartTwo)

run(DayOne)
run(DayTwo)