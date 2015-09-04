#!/usr/bin/python
# replaces layout named bla
#
# to change run keyboard layout simply run "setxkbmap bla"
# See: http://ubuntuforums.org/showthread.php?t=188761 for help
#
# Tobias Birnbaum, SNT 2015

import os
import sys
import glob
import string
import numpy as np
from operator import itemgetter
# Usage: itemgetter(*[Index List])([List])

keyboardKeys = ['AE{0:02d}'.format(i) for i in range(1, 11)]
keyboardKeys.extend(['AD{0:02d}'.format(i) for i in range(1, 12)])
keyboardKeys.extend(['AC{0:02d}'.format(i) for i in range(1, 12)])
keyboardKeys.extend(['AB{0:02d}'.format(i) for i in range(1, 8)])

symbols = list(string.letters)
symbols.extend(['odiaeresis', 'Odiaeresis', 'adiaeresis', 'Adiaeresis',
                'udiaeresis', 'Udiaeresis', 'exclam', 'quotedbl', 'section',
                'dollar', 'percent', 'ampersand', 'slash', 'parenleft',
                'parenright', 'equal'])
symbols.extend(range(10))

# scramble symbol list
symbolsSCR = np.random.permutation(np.array(symbols))
symbolsSCR = symbolsSCR.reshape(len(symbols)/2, 2)
symbolsSCR = symbolsSCR.tolist()           # Format: symbolsSCR[1] = ['N', 'P']

keyMap = dict(zip(keyboardKeys, symbolsSCR))


# create backup
# if os.path.isfile("bla.org"):
#    print "Backup exists already"
# elif not os.path.exists("bla.org"):
#    os.rename("bla", "bla.org")
#    print "New backup created"

# write to file
outfile = open('bla', 'wt')

# HEADER BEGIN
outfile.write('default\n')
outfile.write('xkb_symbols "basic" {\n')
outfile.write('name[Group1]="OwnFoo";\n')
outfile.write('// this block will remain unchanged\n')
outfile.write('    key <BKSP> { [ BackSpace ]};\n')
outfile.write('    key <DELE> { [ Delete ]};\n')
outfile.write('    key <ESC>  { [ Escape ]};\n')
outfile.write('    key <FK01> { [ F1 ]};\n')
outfile.write('    key <FK02> { [ F2 ]};\n')
outfile.write('    key <FK03> { [ F3 ]};\n')
outfile.write('    key <FK04> { [ F4 ]};\n')
outfile.write('    key <FK05> { [ F5 ]};\n')
outfile.write('    key <FK06> { [ F6 ]};\n')
outfile.write('    key <FK07> { [ F7 ]};\n')
outfile.write('    key <FK08> { [ F8 ]};\n')
outfile.write('    key <FK09> { [ F9 ]};\n')
outfile.write('    key <FK10> { [ F10 ]};\n')
outfile.write('    key <FK11> { [ F11 ]};\n')
outfile.write('    key <FK12> { [ F12 ]};\n')
outfile.write('    key <RTRN> { [ Return ]};\n')
outfile.write('    key <LALT> { [Alt_L ]};\n')
outfile.write('    key <RALT> { [Alt_R ]};\n')
outfile.write('    key <LCTL> { [Control_L ]};\n')
outfile.write('    key <RCTL> { [Control_R ]};\n')
outfile.write('    key <RFSH> { [Shift_R ]};\n')
outfile.write('    key <RFSH> { [Shift_R ]};\n')
outfile.write('    key <RFSH> { [Shift_R ]};\n')
outfile.write('// this block will end now\n')
# HEADER END

kbd = keyMap.keys()
kbd.sort()
for key in kbd:
    sym = keyMap[key]
    outfile.write('    key <' + key + '> { [' + str(sym[0]) + ', ' +
                  str(sym[1]) + '] }; \n')
# scrambled output of keys whatsoever
    # for kbd,sym in keyMap.iteritems():
    #    outfile.write('    key <' + kbd + '> { [' + str(sym[0]) + ', ' +
    #                  str(sym[1]) + '] }; \n')

# FINISH BEGIN
outfile.write('};\n')
# FINISH END

outfile.close()
