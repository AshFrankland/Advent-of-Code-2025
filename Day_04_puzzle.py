def get_Input():
    input = 'Day_04_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = []
        for line in txt:
            raw_Input.append(line.rstrip('\n'))
        paper_Map = {}
        width = len(raw_Input[0])
        height = len(raw_Input)
        for row in range(height):
            for col in range(width):
                paper_Map[(col, row)] = raw_Input[row][col]
        for col in range(width + 2):
            paper_Map[(col - 1, -1)] = '.'
            paper_Map[((col - 1, height))] = '.'
        for row in range(height):
            paper_Map[(-1, row)] = '.'
            paper_Map[(width, row)] = '.'
        return paper_Map, width, height

def find_Reachable(paper_Map, width, height):
    reachable = 0
    for col in range(width):
        for row in range(height):
            if paper_Map[(col, row)] == '@':
                rolls = ''
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        rolls = rolls + paper_Map[(col + x, row + y)]
                if rolls.count('@') <= 4:
                    reachable += 1
    return reachable

def remove_Paper(paper_Map, width, height):
    new_Map = paper_Map
    removed_Total = 0
    while True:
        removed = 0
        for col in range(width):
            for row in range(height):
                if paper_Map[(col, row)] == '@':
                    rolls = ''
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            rolls = rolls + paper_Map[(col + x, row + y)]
                    if rolls.count('@') <= 4:
                        removed += 1
                        new_Map[(col, row)] = '.'
        removed_Total += removed
        if removed == 0:
            break
        paper_Map = new_Map
    return removed_Total

def main():
    paper_Map, width, height = get_Input()
    print(find_Reachable(paper_Map, width, height))
    print(remove_Paper(paper_Map, width, height))

if __name__ == '__main__':
    main()