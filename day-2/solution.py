from typing import List
import re

class Solution:
    game_num_pattern = re.compile(r'^Game ([0-9]+): ')
    red_pattern = re.compile(r'([0-9]+) red')
    green_pattern = re.compile(r'([0-9]+) green')
    blue_pattern = re.compile(r'([0-9]+) blue')

    def __init__(self, bag_contents = [12, 13, 14]):
        self.bag_contents = bag_contents
        pass

    def solve(self, lines: List[str]) -> int:
        count = 0
        for i in range(len(lines)):
            line = lines[i]
            game_number_pattern_match = Solution.game_num_pattern.match(line)
            game_num = int(game_number_pattern_match.group(1))
            games = line[game_number_pattern_match.end(0):].split(";")
            print(f'{game_number_pattern_match.group(1)}: {games}')

            are_all_games_valid = True
            for game in games:
                print(f'{Solution.evaluate_game(game)}')
                if not self.is_game_valid(Solution.evaluate_game(game)):
                    are_all_games_valid = False

            print(f'{are_all_games_valid}')

            if are_all_games_valid:
                count += game_num
        return count
    
    def is_game_valid(self, game: List[int]) -> bool:
        for i in range(len(self.bag_contents)):
            if game[i] > self.bag_contents[i]:
                return False
        return True

    def evaluate_game(game: str) -> List[int]:
        return [
            Solution.search_or_zero(Solution.red_pattern, game),
            Solution.search_or_zero(Solution.green_pattern, game),
            Solution.search_or_zero(Solution.blue_pattern, game)
        ]
    
    def search_or_zero(pattern: re.Pattern, game: str) -> int:
        match = pattern.search(game)
        if match == None:
            return 0
        return int(match.group(1))

