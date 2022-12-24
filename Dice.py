import random


class Die:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)


class DnDDice:
    def __init__(self):
        self.d4 = Die(4)
        self.d6 = Die(6)
        self.d8 = Die(8)
        self.d10 = Die(10)
        self.d12 = Die(12)
        self.d20 = Die(20)

    def roll_d4(self, num_dice=1):
        results = []
        for i in range(num_dice):
            results.append(self.d4.roll())
        return results if num_dice > 1 else results[0]

    def roll_d6(self, num_dice=1):
        results = []
        for i in range(num_dice):
            results.append(self.d6.roll())
        return results if num_dice > 1 else results[0]

    def roll_d8(self, num_dice=1):
        results = []
        for i in range(num_dice):
            results.append(self.d8.roll())
        return results if num_dice > 1 else results[0]

    def roll_d10(self, num_dice=1):
        results = []
        for i in range(num_dice):
            results.append(self.d10.roll())
        return results if num_dice > 1 else results[0]

    def roll_d12(self, num_dice=1):
        results = []
        for i in range(num_dice):
            results.append(self.d12.roll())
        return results if num_dice > 1 else results[0]

    def roll_d20(self, num_dice=1):
        results = []
        for i in range(num_dice):
            results.append(self.d20.roll())
        return results if num_dice > 1 else results[0]

    def roll_top(self, dice_type, num_dice, num_top):
        results = self.__getattribute__(f"roll_{dice_type}")(num_dice)
        return sum(sorted(results, reverse=True)[:num_top]) if num_dice > 1 else results

