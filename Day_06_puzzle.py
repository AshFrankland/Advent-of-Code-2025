from math import prod

def get_Input():
    input = 'Day_06_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = []
        for line in txt:
            raw_Input.append(line.rstrip('\n'))
        math_Strs = []
        for line in raw_Input:
            math_Strs.append(line.split())
        digits = len(raw_Input) - 1
        ceph_Nums = []
        nums = []
        for index in range(len(raw_Input[0])):
            num = ''
            for digit in range(digits):
                num = num + raw_Input[digit][index]
            if num.isspace():
                ceph_Nums.append(nums)
                nums = []
            else:
                nums.append(int(num.strip()))
        ceph_Nums.append(nums)
        ceph_Nums.append(raw_Input[-1].split())
        return math_Strs, ceph_Nums

def do_Math(math_Strs):
    how_Many = len(math_Strs) - 1
    total = 0
    for question in range(len(math_Strs[0])):
        opp = math_Strs[-1][question]
        nums = []
        for num in range(how_Many):
            nums.append(int(math_Strs[num][question]))
        if opp == '*':
            total += prod(nums)
        else:
            total += sum(nums)
    return total

def ceph_Math(ceph_Nums):
    total = 0
    for question in range(len(ceph_Nums[-1])):
        if ceph_Nums[-1][question] == '*':
            total += prod(ceph_Nums[question])
        else:
            total += sum(ceph_Nums[question])
    return total

def main():
    math_Strs, ceph_Nums = get_Input()
    print(do_Math(math_Strs))
    print(ceph_Math(ceph_Nums))

if __name__ == '__main__':
    main()