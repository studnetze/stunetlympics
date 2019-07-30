# StuNetlympics

A game where you have to enter a given sentence as fast as possible, but with a scrambled keyboard layout.

## Setup

Lets say `test.py` is located in `$DIR`.

Create a symlink to the symbol config, which will be generated: `sudo ln -s "$DIR/random_layout" /usr/share/X11/xkb/symbols/random_layout`.

That's it. This way you won't need special permissions to run `test.py`.

## Play

Run `safety-net.sh` in a separate window. In case the game crashes and cannot reset your keyboard layout, you just have to press ENTER in that script to reset it.

Run `test.py`.

It will generate a new random layout, activate it with `setxkbmap random_layout` and show a fortune for you to copy.

It will be hard to kill the game, as the C key of CTRL-C will be remapped. By using `safety-net.sh` you can reset your kayboard layout.
