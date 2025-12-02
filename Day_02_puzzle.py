def get_Input():
    input = 'Day_02_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = txt[0].split(',')
        clean_Input = []
        for entry in  raw_Input:
            range_Str = entry.split('-')
            clean_Input.append([int(range_Str[0]), int(range_Str[1])])
        return clean_Input

def find_Double(bounds):
    invalid_ID_Sum1 = 0
    for num in range(bounds[0], bounds[1] + 1):
        if len(str(num)) % 2 == 0:
            if str(num) == str(num)[0:len(str(num)) // 2] + str(num)[0:len(str(num)) // 2]:
                invalid_ID_Sum1 += num
    return invalid_ID_Sum1

def find_Repeat(bounds):
    invalid_ID_Sum2 = 0
    for num in range(bounds[0], bounds[1] + 1):
        if (str(num) + str(num)).find(str(num), 1) != len(str(num)):
            invalid_ID_Sum2 += num
    return invalid_ID_Sum2

def main():
    ranges = get_Input()
    invalid_Sum1 = 0
    invalid_Sum2 = 0
    for bounds in ranges:
        invalid_Sum1 += find_Double(bounds)
        invalid_Sum2 += find_Repeat(bounds)
    print(invalid_Sum1)
    print(invalid_Sum2)

if __name__ == '__main__':
    main()