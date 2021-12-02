from solutions import DayTwo

input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]

def test_part_one():
    sut = DayTwo.PartOne()
    sut.run(input)
    assert sut.submarine.position == [15, 10]

def test_part_two():
    sut = DayTwo.PartTwo()
    sut.run(input)
    assert sut.submarine.position["h"] == 15
    assert sut.submarine.position["d"] == 60