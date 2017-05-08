#
# analyze the scores in the saved games
#

import json
import glob
import itertools

filename_wildcard = "./scores/game-*.json"

# ===========================================================================

class player():
    def __init__(self, name):
        self.name  = name
        self.win   = [];
        self.loose = [];
        self.draw  = [];
        self.best_score = 0

    def set(self, winners, loosers, score):
        if self.name in winners:
            self.win.extend(loosers)
            self.draw.extend([w for w in winners if w != self.name])

            if self.best_score < score:
                self.best_score = score

        if self.name in loosers:
            self.loose.extend(winners)
            self.draw.extend([w for w in loosers if w != self.name])

    def result_against(self, opponent):
        W = len([x for x in self.win   if x == opponent.name])
        L = len([x for x in self.loose if x == opponent.name])

        print('{0:s} vs. {1:s}: {2:d} - {3:d}'.format(self.name, opponent.name, W, L))

# ===========================================================================

players = [player('Elena'),
           player('Mitko'),
           player('Marina')]

for file in glob.glob(filename_wildcard):
    with open(file) as data_file:
        data = json.load(data_file)

    key = list(data['total-score'].keys())
    val = list(data['total-score'].values())
    max_score = max(val)

    winners = [key[i] for i,j in enumerate(val) if j == max_score]
    loosers = [key[i] for i,j in enumerate(val) if j != max_score]

    for player in players:
        player.set(winners, loosers, max_score)

# ===========================================================================

# display scores
print("============================")
for (player_i, player_j) in list(itertools.combinations(players,2)):
    player_i.result_against(player_j)
print("============================")
for player in players:
    print("{0:s}: {1:d}".format(player.name, player.best_score))
print("============================")

###EOF
