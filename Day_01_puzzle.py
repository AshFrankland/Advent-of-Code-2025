def get_Input():
    input = 'Day_01_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = []
        for line in txt:
            raw_Input.append(line.rstrip('\n'))
        instructions = []
        for input in raw_Input:
            if input[0] == 'R':
                instructions.append(int(input.lstrip('R')))
            else:
                instructions.append(0 - int(input.lstrip('L')))
        return instructions

def main():
    instructions = get_Input()
    dial = 50
    zero_Count_1 = 0
    zero_Count_2 = 0
    for input in instructions:
        prev_num = dial
        dial += input
        if dial >= 100:
            zero_Count_2 += (dial // 100)
        elif dial <= 0:
            zero_Count_2 += ((dial // -100) + 1)
            if prev_num == 0:
                zero_Count_2 -= 1
        dial %= 100
        if dial == 0:
            zero_Count_1 += 1
    print(zero_Count_1)
    print(zero_Count_2)

if __name__ == '__main__':
    main()