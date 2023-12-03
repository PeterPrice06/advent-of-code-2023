from typing import List
import re

class Solution:
    numbers_pattern = re.compile(r'[0-9]')
    spelled_digits_patterns = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|[0-9])')
    reverse_spelled_digits_patterns = re.compile(r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9])')

    def __init__(self):
        pass

    def solve_part1(self, lines: List[str]) -> int:
        count = 0
        for i in range(len(lines)):
            line = lines[i]
            numbers = Solution.numbers_pattern.findall(line)
            count += int(numbers[0] + numbers[-1])
        return count

    def solve_part2(self, lines: List[str]) -> int:
        count = 0
        for i in range(len(lines)):
            line = lines[i]
            first_num = Solution.spelled_digits_patterns.search(line).group(0)
            last_num = Solution.reverse_spelled_digits_patterns.search(line[::-1]).group(0)[::-1]
            print(f'{first_num}, {last_num}')
            count += Solution.convert(first_num) * 10 + Solution.convert(last_num)
        return count

    def convert(s: str) -> str:
        map = {
            'one': 1, 
            'two': 2, 
            'three': 3, 
            'four': 4, 
            'five': 5, 
            'six': 6, 
            'seven': 7, 
            'eight': 8, 
            'nine': 9}
        if map.get(s) != None:
            return map.get(s)
        return int(s)