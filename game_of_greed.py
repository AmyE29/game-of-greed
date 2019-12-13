import random
from collections import Counter

class Game:
    """Sets up the game structure"""

    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.score = 0
        self.num_rounds = 10


    def play(self, num_rounds=10):
        self.num_rounds = num_rounds
        self._print('Welcome to the Game of Greed')
        answer = str.lower(input('Wanna play (y/n)?'))
        if answer == "y":
            self.start_game()
        else:
            self._print('OK. Maybe another time')


    def start_game(self):
        self.score = 0
        rounds = 1
        for i in range(1, self.num_rounds + 1):
            round_score = self.play_game()
            self._print(f'You banked {round_score} points in round {rounds}')

            self.score += round_score
            rounds += 1

            self._print(f'Whoo hoo! You have {self.score} points so far')
        self._print('Come play again soon!')


    def play_game(self):
        num_dice = 6
        score = 0
        while(True):
            self._print(f'Rolling {num_dice} dice')
            roll = self.roll_dice(num_dice)
            farkled_out_score = self.calculate_score(roll)
            self._print(f'You rolled {roll}')

            if farkled_out_score == 0:
                self._print('FARKLE')
                return 0

            values = self.validate_roll(roll)
            num_dice -= len(values)
            score += self.calculate_score(values)

            self._print(f'Do you want to bank your score of {score} or press your luck for more points?')

            if num_dice == 0:
                num_dice = 6

            self._print(f'You have {num_dice} dice remaining')

            roll_again_response = self._input('Roll again? ')

            if not roll_again_response == 'y':
                break


        return score

    def validate_roll(self, roll):

        while True:

            keep_response = self._input('Enter dice to keep: ')

            values = tuple(int(char) for char in keep_response)

            if self.validate(roll, values):
                return values
            else:
                self._print('Hmmmm...those numbers don\'t work')
                self._print(roll)


    def validate(self, roll, values):

        roll_counter = Counter(roll)
        values_counter = Counter(values)
        return len(values_counter - roll_counter) == 0


    def calculate_score(self, dice):

        count = Counter(dice)
        if len(dice) == 6:

            #calculate straight
            roll_counter = Counter(dice)
            if len(roll_counter) == 6:
                return 1500
            
            #three pairs
            vals = roll_counter.values()
            val_set = set(vals)
            if len(val_set):
                return 1500

            # Handle other sum cases. Since 1 is run first
        total = 0

        for key in count:

            if count[key] > 2:
                total += ((count[key]-2)*100)*key
            elif key == 1:
                total += count[key] * 100
            elif key == 5:
                total += count[key] * 50

        if key == 1:
            total *= 10

        return total

    def roll_dice(self, num_dice):
        """ramdomly rolling 6 dice """
        return [random.randint(1, 6) for _ in range(num_dice)]


if __name__ == "__main__":
    game = Game()
    game.play()

