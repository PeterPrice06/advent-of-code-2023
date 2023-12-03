from typing import List
import re

class Solution:
    numbers_pattern = re.compile(r'[0-9]')

    def __init__(self):
        pass

    def solve(self, lines: List[str]) -> int:
        count = 0
        for i in range(len(lines)):
            line = lines[i]
            numbers = Solution.numbers_pattern.findall(line)
            count += int(numbers[0] + numbers[-1])
        return count
