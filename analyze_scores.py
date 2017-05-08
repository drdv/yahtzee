#!/usr/bin/python
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
        self.best_score      = 0
        self.total_score     = 0
        self.number_of_games = 0

    def set(self, winners, loosers):
        if self.name in winners:
            self.win.extend(list(loosers))
            self.draw.extend([key for key in winners.keys() if key != self.name])

            if self.best_score < winners[self.name]:
                self.best_score = winners[self.name]

            self.total_score += winners[self.name]
            self.number_of_games += 1

        if self.name in loosers:
            self.loose.extend(list(winners))
            self.draw.extend([key for key in loosers.keys() if key != self.name])

            if self.best_score < loosers[self.name]:
                self.best_score = loosers[self.name]

            self.total_score += loosers[self.name]
            self.number_of_games += 1


    def show_result_against(self, opponent):
        W = len([x for x in self.win   if x == opponent.name])
        L = len([x for x in self.loose if x == opponent.name])

        if L+W > 0:
            print('{0:17s}: {1:2d} - {2:2d}'.format(self.name + ' vs. ' + opponent.name, W, L))

    def show_score(self):
        if self.number_of_games > 0:
            print("{0:17s}: {1:2.2f}  ({2:3d})".format(self.name,
                                                       self.total_score/self.number_of_games,
                                                       self.best_score))

# ===========================================================================

players = [player('Elena'),
           player('Mitko'),
           player('Marina'),
           player('Tomas')]

for file in glob.glob(filename_wildcard):
    with open(file) as data_file:
        data = json.load(data_file)

    scores = data['total-score']
    max_score = max(scores.values())

    winners = dict([(key, val) for (key, val) in scores.items() if val == max_score])
    loosers = dict([(key, val) for (key, val) in scores.items() if val != max_score])

    for player in players:
        player.set(winners, loosers)

# ===========================================================================

# display scores
print("===============================")
for (player_i, player_j) in list(itertools.combinations(players,2)):
    player_i.show_result_against(player_j)
print("===============================")
print("                   average  max")
for player in players:
    player.show_score()
print("===============================")

###EOF
