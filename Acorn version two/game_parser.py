from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    f = open(filename, "r")

    line = f.readlines()

    f.close()

    grid = parse(line)
    return grid


def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """

    start = Start()
    end = End()
    air = Air()
    wall = Wall()
    fire = Fire()
    water = Water()
    teleport_one = Teleport(1)
    teleport_two = Teleport(2)
    teleport_three = Teleport(3)
    teleport_four = Teleport(4)
    teleport_five = Teleport(5)
    teleport_six = Teleport(6)
    teleport_seven = Teleport(7)
    teleport_eight = Teleport(8)
    teleport_nine = Teleport(9)
    teleport_zero = Teleport(0)

    i = 0  # used for loop
    x = 0  # used for judging if X(Start position) exists when the loop of while is over
    y = 0  # used for judging if Y(End position) exists when the loop of while is over
    # The variables below represent the number of different teleport
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0

    # Process the line(a list of list string) from here
    ls = []
    for i in lines:
        i = i.strip()
        ls.append(list(i))

    lines = ls

    i = 0

    while i < len(lines):
        j = 0
        while j < len(lines[i]):

            if lines[i][j] != "X" and lines[i][j] != "Y" and lines[i][j] != " " and \
                    lines[i][j] != "*" and lines[i][j] != "F" \
                    and lines[i][j] != "W" and lines[i][j] != "0" \
                    and lines[i][j] != "1" and lines[i][j] != "2" \
                    and lines[i][j] != "3" and lines[i][j] != "4" and \
                    lines[i][j] != "5" and lines[i][j] != "6" \
                    and lines[i][j] != "7" and lines[i][j] != "8" and \
                    lines[i][j] != "9":
                raise ValueError("Bad letter in configuration file: {}.".format(lines[i][j]))
            pass
            if lines[i][j] == "X":
                x = x + 1
            if lines[i][j] == "Y":
                y = y + 1
                # check if the Teleport pads have an exclusively matching pad.
                # if mathched, then the number plus one
            if lines[i][j] == "0":
                zero = zero + 1
            if lines[i][j] == "1":
                one += 1
            if lines[i][j] == "2":
                two += 1
            if lines[i][j] == "3":
                three += 1
            if lines[i][j] == "4":
                four += 1
            if lines[i][j] == "5":
                five += 1
            if lines[i][j] == "6":
                six += 1
            if lines[i][j] == "7":
                seven += 1
            if lines[i][j] == "8":
                eight += 1
            if lines[i][j] == "9":
                nine += 1
            j = j + 1
        i = i + 1
    # If the Teleport pads do not have an exclusively matching pad, then raise ValueError
    if x != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(x))
    if y != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(y))
    if zero != 2 and zero != 0:
        raise ValueError("Teleport pad 0 does not have an exclusively matching pad.")
    if one != 2 and one != 0:
        raise ValueError("Teleport pad 1 does not have an exclusively matching pad.")
    if two != 2 and two != 0:
        raise ValueError("Teleport pad 2 does not have an exclusively matching pad.")
    if three != 2 and three != 0:
        raise ValueError("Teleport pad 3 does not have an exclusively matching pad.")
    if four != 2 and four != 0:
        raise ValueError("Teleport pad 4 does not have an exclusively matching pad.")
    if five != 2 and five != 0:
        raise ValueError("Teleport pad 5 does not have an exclusively matching pad.")
    if six != 2 and six != 0:
        raise ValueError("Teleport pad 6 does not have an exclusively matching pad.")
    if seven != 2 and seven != 0:
        raise ValueError("Teleport pad 7 does not have an exclusively matching pad.")
    if eight != 2 and eight != 0:
        raise ValueError("Teleport pad 8 does not have an exclusively matching pad.")
    if nine != 2 and nine != 0:
        raise ValueError("Teleport pad 9 does not have an exclusively matching pad.")
    ''' 
    After raise all the ValueError, if there is nothing wrong, we change a
    list of lists string into a list of lists instances(Object)
    '''
    i = 0
    while i < len(lines):
        j = 0
        while j < len(lines[i]):

            if lines[i][j] == start.display:
                lines[i][j] = start
            elif lines[i][j] == end.display:
                lines[i][j] = end
            elif lines[i][j] == air.display:
                lines[i][j] = air
            elif lines[i][j] == wall.display:
                lines[i][j] = wall
            elif lines[i][j] == fire.display:
                lines[i][j] = fire
            elif lines[i][j] == water.display:
                lines[i][j] = water
            elif lines[i][j] == teleport_zero.display:
                lines[i][j] = teleport_zero
            elif lines[i][j] == teleport_one.display:
                lines[i][j] = teleport_one
            elif lines[i][j] == teleport_two.display:
                lines[i][j] = teleport_two
            elif lines[i][j] == teleport_three.display:
                lines[i][j] = teleport_three
            elif lines[i][j] == teleport_four.display:
                lines[i][j] = teleport_four
            elif lines[i][j] == teleport_five.display:
                lines[i][j] = teleport_five
            elif lines[i][j] == teleport_six.display:
                lines[i][j] = teleport_six
            elif lines[i][j] == teleport_seven.display:
                lines[i][j] = teleport_seven
            elif lines[i][j] == teleport_eight.display:
                lines[i][j] = teleport_eight
            elif lines[i][j] == teleport_nine.display:
                lines[i][j] = teleport_nine

            j = j + 1
        i = i + 1

    return lines
