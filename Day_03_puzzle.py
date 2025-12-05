def get_Input():
    input = 'Day_03_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = []
        for line in txt:
            raw_Input.append(line.rstrip('\n'))
        batt_Lists = []
        for line in raw_Input:
            num_List = []
            for num in line:
                num_List.append(int(num))
            batt_Lists.append(num_List)
        return batt_Lists

def find_Pair(batteries):
    highest = max(batteries)
    high_Index = batteries.index(highest)
    if high_Index == len(batteries) - 1:
        second = max(batteries[:high_Index])
        pair = int(str(second) + str(highest))
    else:
        second = max(batteries[high_Index + 1:])
        pair = int(str(highest) + str(second))
    return pair

def find_12(batteries):
    joltage = max(batteries[:-11])
    reduced_List = batteries[batteries.index(joltage) + 1:]
    remaining_Digits = 11
    while remaining_Digits > 1:
        next_Digit = max(reduced_List[:(1 - remaining_Digits)])
        joltage = int(str(joltage) + str(next_Digit))
        reduced_List = reduced_List[reduced_List.index(next_Digit) + 1:]
        remaining_Digits -= 1
    next_Digit = max(reduced_List)
    joltage = int(str(joltage) + str(next_Digit))
    return joltage

def main():
    batt_Lists = get_Input()
    joltage1 = 0
    for batteries in batt_Lists:
        joltage1 += find_Pair(batteries)
    print(joltage1)
    joltage2 = 0
    for batteries in batt_Lists:
        joltage2 += find_12(batteries)
    print(joltage2)

if __name__ == '__main__':
    main()