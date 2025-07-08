import random

# Scorecard
PlayerRed = []
PlayerYellow = []
PlayerBlue = []
PlayerGreen = []

# Dice Rolls
RedDie = random.randrange(1, 6)
YellowDie = random.randrange(1, 6)
BlueDie = random.randrange(1, 6)
GreenDie = random.randrange(1, 6)
White1 = random.randrange(1, 6)
White2 = random.randrange(1, 6)

# Potential Scores
RedScores = [RedDie + White1, RedDie + White2]
YellowScores = [YellowDie + White1, YellowDie + White2]
BlueScores = [BlueDie + White1, BlueDie + White2]
GreenScores = [GreenDie + White1, GreenDie + White2]
WildCards = [White1 + White2]






print(RedDie, YellowDie, BlueDie, GreenDie, White1, White2, RedScores, YellowScores, BlueScores, GreenScores, WildCards)