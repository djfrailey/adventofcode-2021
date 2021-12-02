from solutions.DayOne import PartOne, PartTwo

input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def test_part_one():
    assert PartOne().run(input) == 7

def test_part_two():
    assert PartTwo().run(input) == 5