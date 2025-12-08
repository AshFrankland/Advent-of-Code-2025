def get_Input():
    input = 'Day_05_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = []
        for line in txt:
            raw_Input.append(line.rstrip('\n'))
        range_Strs = raw_Input[:raw_Input.index('')]
        id_Strs = raw_Input[raw_Input.index('') + 1:]
        ranges = []
        for entry in range_Strs:
            bound_Strs = entry.split('-')
            bounds = (int(bound_Strs[0]), int(bound_Strs[1]))
            ranges.append(bounds)
        ids = []
        for id in id_Strs:
            ids.append(int(id))
        return ranges, ids

def find_Fresh(ranges, ids):
    fresh_Count = 0
    for id in ids:
        for ran in ranges:
            if id >= ran[0] and id <= ran[1]:
                fresh_Count += 1
                break
    return fresh_Count

def how_Fresh(ranges):
    merged = []
    while ranges:
        new = []
        check_Range = ranges.pop()
        for index in range(len(merged)):
            if max(check_Range[0], merged[index][0]) <= min(check_Range[1], merged[index][1]):
                check_Range = (min(check_Range[0], merged[index][0]), max(check_Range[1], merged[index][1]))
            else:
                new.append(merged[index])
        new.append(check_Range)
        merged = new
    fresh_Ids = 0
    for ran in merged:
        fresh_Ids += ran[1] - ran[0] + 1
    return fresh_Ids

def main():
    ranges, ids = get_Input()
    print(find_Fresh(ranges, ids))
    print(how_Fresh(ranges))

if __name__ == '__main__':
    main()