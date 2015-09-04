#!/usr/bin/python
# Generates Hall of Fame for keyboard-scrambling game.
#
# Tobias Birnbaum, SNT 2015

import sqlite3
import os

try:
    os.remove('HoF.db')
except:
    pass

sqlite_file = 'HoF.db'
table_name = 'ranking'
name_column = 'Name'
val_column = 'Time'

dbconn = sqlite3.connect(sqlite_file)
c = dbconn.cursor()
c.execute('CREATE TABLE {tn} ({nf} {ft})'
          .format(tn=table_name, nf=name_column, ft='TEXT'))
c.execute("ALTER TABLE {tn} ADD COLUMN {cn} {ct}"
          .format(tn=table_name, cn=val_column, ct='REAL'))
dbconn.commit()
dbconn.close()
