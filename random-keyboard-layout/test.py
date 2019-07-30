#!/usr/bin/python3
# Starts the game (incl. xkb-generation). The game is type a string called
# "jingle" on a random keyboard layout as fast as you can.
#     HF
#
# Original Author Tobias Birnbaum, SNT 2015

from subprocess import Popen, PIPE
import time

try:
    Popen(['python3', 'create-xkb-symbols.py'])
    Popen(['setxkbmap', 'random_layout'])

    with Popen(['fortune', '-s', '-n', '50'], stdout=PIPE) as proc:
        jingle = proc.stdout.read().decode().replace('\n', '').replace('  ', '')

    print("Welcome to Stunetlympics!")
    print("-------------------------------------------------------------")
    print("Please type in text, displayed in the following as fast as")
    print("you can.")
    print("Now it's your turn to give kbd-mnemonic a try. Be the best...")
    print('Escape hatch into outer space: "setxkbmap de "')
    print("-------------------------------------------------------------")
    input("Press Enter to continue...")
    print("Ready...")
    time.sleep(0.5)
    print("Steady...")
    time.sleep(0.5)
    print("Go!")
    print("-------------------------------------------------------------\n")

    t0 = time.time()
    while True:
        print(jingle + '\n\n')
        var = input('Your guess:\n')
        if var == jingle:
            break
    wallTime = (time.time() - t0)
    print("You did it in {0:8.5f}s.\n".format(wallTime))

    Popen(['setxkbmap', 'de'])
    #name = input("Please enter your name for the hall of fame: ")
    # TODO write simple text file

finally:
    Popen(['setxkbmap', 'de'])
