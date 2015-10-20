import sys

pathFile = sys.argv[1]

def generateMap(input_file):
    startIndicator = 'R'
    endIndicator = 'T'
    width = None

    field = {}
    start = None
    end = None

    with open(input_file, "r") as raw:
        string = raw.read()

        # Ignore newline characters
        tiles = list(string.replace('\n', ''))

        height = string.count('\n') # Number of lines
        width = len(tiles) / height # Number of characters per line = total characters / number of lines

        for tile in enumerate(tiles):
            position = tile[0]
            kind = tile[1]
            field[position] = {
                'type': kind,
                'neighbors': []
            }

            # If position % width == 0, it's on the leftmost edge
            if position % width != 0:
                # West
                field[position]['neighbors'].append(position - 1)

            # If position + 1 % width == 0, it's on the rightmost edge
            if (position + 1) % width != 0:
                # East
                field[position]['neighbors'].append(position + 1)

            # If position - width < 0, it's on the topmost edge
            if position - width >= 0:
                # North
                field[position]['neighbors'].append(position - width)

            # If position + width >= len, it's on the bottommost edge
            if position + width < len(tiles):
                print "South"
                # South
                field[position]['neighbors'].append(position + width)

    return {
        'field': field,
        'start': tiles.index(startIndicator),
        'end': tiles.index(endIndicator)
    }

def isValidSpace(space):
    valid = ['.', 'T', 'R']

    return space in valid

print generateMap(pathFile)
