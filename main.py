class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        if not self.is_valid_roll(pins):
            raise ValueError("Ungültige Anzahl von Pins für einen Wurf")

        self.rolls.append(pins)

    def is_valid_roll(self, pins):
        return 0 <= pins <= 10

    def calculate_score(self):
        score = 0
        frame_index = 0

        for frame in range(10):
            if self.is_strike(frame_index):
                score += 10 + self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                score += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self.sum_of_pins_in_frame(frame_index)
                frame_index += 2

        return score

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def is_spare(self, frame_index):
        return self.sum_of_pins_in_frame(frame_index) == 10

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def sum_of_pins_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]


game = BowlingGame()
rolls_sequence = [3, 5, 5, 5, 10, 8, 1, 4, 3, 2, 10, 6, 3, 7, 2, 9, 1, 10, 5, 5, 8]
for pins in rolls_sequence:
    game.roll(pins)

score = game.calculate_score()
print(f"Der Endstand beträgt: {score}")
