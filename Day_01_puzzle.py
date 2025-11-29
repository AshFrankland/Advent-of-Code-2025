from pprint import pprint

def get_Input():
    input = 'test_input.txt'
    #input = 'Day_01_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = []
        for line in txt:
            raw_Input.append(line.rstrip('\n'))
        return raw_Input

def main():
    get_Input()

if __name__ == '__main__':
    main()