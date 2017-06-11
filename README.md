[![MELPA](http://melpa.org/packages/yahtzee-badge.svg)](http://melpa.org/#/yahtzee)

# Yahtzee

The [Yahtzee](https://en.wikipedia.org/wiki/Yahtzee) game.

![An example game with 3 players](images/yahtzee.png)

The image is from a game with three players.

# Installation

#### Via MELPA (recommended)

If you have a recent version of `package.el` you can install `yahtzee` from
the [MELPA](http://melpa.org) package repository.

#### Manually

Ensure that `yahtzee.el` is in a directory on your load-path, and add `(require 'yahtzee)`
to your `~/.emacs` or `~/.emacs.d/init.el`.

# How to play

- `M-x yahtzee` start a game (in a new buffer)
- `C-c n`       start a new game (in the same buffer)
- `C-c p`       add players
- `C-c P`       reset players
- `SPC`         throw dice
- `{1,2,3,4,5}` hold outcome of `{1,2,3,4,5}`-th dice
- `UP/DOWN`     select score to register
- `ENTER`       register selected score
- `w`           save the game (in json format)

The score of a saved game can be loaded using `M-x yahtzee-load-game-score`.

# Notes

Personally I don't enjoy playing with "Yahtzee bonuses" and "Joker rules"
so they are not implemented (even thought they are simple to include).
Only the "63 bonus" is available (see `yahtzee-compute-bonus`). Furthermore,
some scores differ from the official ones. Changing all this can be
done by simply modifying the corresponding functions in the definition
of `yahtzee-fields-alist`.
