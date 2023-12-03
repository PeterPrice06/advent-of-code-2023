import unittest
from typing import List
import solution

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = solution.Solution()

    def test_simple(self) -> None:
        lines = file_read_helper('simple_input.txt')
        result = self.solution.solve(lines)
        self.assertEqual(result, 142)

    def test_long(self) -> None:
        lines = file_read_helper('long_input.txt')
        result = self.solution.solve(lines)
        self.assertEqual(result, 56108)

def file_read_helper(filename: str) -> List[str]:
    lines = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines

if __name__ == '__main__':
    unittest.main()
