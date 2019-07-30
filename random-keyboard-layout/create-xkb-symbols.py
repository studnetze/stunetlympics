#!/usr/bin/python3
# creates a randomized xkb symbol config
#
# Original Author Tobias Birnbaum for SNT 2015

import string
import numpy as np
import random

keyboardKeys = ['AE{0:02d}'.format(i) for i in range(1, 11)]
keyboardKeys.extend(['AD{0:02d}'.format(i) for i in range(1, 12)])
keyboardKeys.extend(['AC{0:02d}'.format(i) for i in range(1, 12)])
keyboardKeys.extend(['AB{0:02d}'.format(i) for i in range(1, 8)])

symbols = list(string.ascii_letters)
symbols.extend(['odiaeresis', 'Odiaeresis', 'adiaeresis', 'Adiaeresis',
                'udiaeresis', 'Udiaeresis', 'exclam', 'quotedbl', 'section',
                'dollar', 'percent', 'ampersand', 'slash', 'parenleft',
                'parenright', 'equal'])
symbols.extend([str(i) for i in range(10)])

assert len(symbols) % 2 == 0, "We need to have an even number of symbols!"
assert len(symbols) == 2 * len(keyboardKeys), "We need twice the number of symbols than keys!"

# scramble symbol list
random.shuffle(symbols)

# slice them in half
# first  half will be assigned to <key>
# second half will be assigned to SHIFT+<key>
half_len = len(symbols) // 2
halfes = [symbols[:half_len], symbols[half_len:]]
scrambled = zip(halfes[0], halfes[1])

keyMap = zip(keyboardKeys, scrambled)

with open('random_layout', 'w') as f:
    # HEADER
    f.write('default\n')
    f.write('xkb_symbols "basic" {\n')
    f.write('name[Group1]="Stunetlympics";\n')
    f.write('// this block remains unchanged\n')
    f.write('    key <BKSP> { [ BackSpace ]};\n')
    f.write('    key <DELE> { [ Delete ]};\n')
    f.write('    key <ESC>  { [ Escape ]};\n')
    f.write('    key <FK01> { [ F1 ]};\n')
    f.write('    key <FK02> { [ F2 ]};\n')
    f.write('    key <FK03> { [ F3 ]};\n')
    f.write('    key <FK04> { [ F4 ]};\n')
    f.write('    key <FK05> { [ F5 ]};\n')
    f.write('    key <FK06> { [ F6 ]};\n')
    f.write('    key <FK07> { [ F7 ]};\n')
    f.write('    key <FK08> { [ F8 ]};\n')
    f.write('    key <FK09> { [ F9 ]};\n')
    f.write('    key <FK10> { [ F10 ]};\n')
    f.write('    key <FK11> { [ F11 ]};\n')
    f.write('    key <FK12> { [ F12 ]};\n')
    f.write('    key <RTRN> { [ Return ]};\n')
    f.write('    key <LALT> { [ Alt_L ]};\n')
    f.write('    key <RALT> { [ Alt_R ]};\n')
    f.write('    key <LCTL> { [ Control_L ]};\n')
    f.write('    key <RCTL> { [ Control_R ]};\n')
    f.write('    key <RFSH> { [ Shift_R ]};\n')
    f.write('    key <RFSH> { [ Shift_R ]};\n')
    f.write('    key <RFSH> { [ Shift_R ]};\n')
    f.write('// now the scrambled part\n')

    for mapping in keyMap:
        f.write('    key <{key}> {{ [{sym1}, {sym2}] }};\n'
            .format(
                key=mapping[0],
                sym1=mapping[1][0],
                sym2=mapping[1][1]
            ))

    # FOOTER
    f.write('};\n')
