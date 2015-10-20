import sys
import Queue

def generateMap(input_file):
    # Useful helpers
    startIndicator = 'R'
    endIndicator = 'T'
    width = None
    height = None

    # Return values
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

def pathExists(m):
    field = m['field']
    start = m['start']
    end = m['end']

    # Keys of tiles to visit and spread out from
    reachable = Queue.Queue()
    reachable.put(start)

    # Key of tiles we've visited
    visited = {}

    # BFS
    while not reachable.empty():
        current = reachable.get()
        visited[current] = True

        # We've reached the end, success
        if current == end:
            print 'yes'
            return

        # Step through each reachable tile
        for neighbor in field[current]['neighbors']:
            # This tile has neighbors we haven't visited
            if neighbor not in visited and isValidSpace(field[neighbor]['type']):
                # Add neighbor to the list of tiles to visit
                # if they are a new, visitable neighbor
                reachable.put(neighbor)

    # never reached end, fail
    print 'no'

pathFile = sys.argv[1]
pathExists(generateMap(pathFile))
