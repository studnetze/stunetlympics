#!/usr/bin/python
# Starts the game (incl. xkb-generation). The game is type a string called "jingle"
# on a random keyboard layout as fast as you can.
#     HF
# 
# If permission for changing the keyboard layout is denied run from shell:
#     touch /usr/share/X11/xkb/symbols/bla
#     chown user:user /usr/share/X11/xkb/symbols/bla
#     chmod 644 /usr/share/X11/xkb/symbols/bla
#
# Tobias Birnbaum, SNT 2015

import subprocess,os,time,sqlite3,shutil

symbolFile='/usr/share/X11/xkb/symbols/bla'
newFile='./bla'

subprocess.Popen("python xkbScramble.py", shell=True).communicate()
shutil.move(newFile, symbolFile)
subprocess.Popen("setxkbmap bla", shell=True).communicate()

try:
    jingle=subprocess.Popen("LANG=C; fortune -s -n 80", shell=True, stdout=subprocess.PIPE).communicate()
    
    jingle=jingle[0].replace("\n", "").replace("  ","")
    
    # Use Short Jingle
    jingle = 'Level5'
    
    print "Welcome to Stun@lympics level 5!\n"
    print "-------------------------------------------------------------\n"
    print "Please type in text, displayed in the following as fast as\n you can.\n "
    print "Now it's your turn to give kbd-mnemonic a try. Be the best...\n"
    print 'Escape hatch into outer space: " setxkbmap de "' 
    print "-------------------------------------------------------------\n"
    raw_input("Press Enter to continue...")
    print "Ready..."
    time.sleep(0.5)
    print "Steady..."
    time.sleep(0.5)
    print "Go!\n"
    print "-------------------------------------------------------------\n"
    
    t0 = time.time()
    while True:
        print jingle + "\n\n"
        var = raw_input("Your guess: \n")
        if var == jingle:
            break
    wallTime = (time.time()-t0)#*100
    print "You did it in {0:8.5f}s. \n".format(wallTime)
    subprocess.Popen("setxkbmap de", shell=True).communicate()
    name = raw_input("\nPlease enter your name (max. len = 12) for the hall of fame: ")
    
    dbconn = sqlite3.connect('HoF.db')
    dbconn.row_factory = sqlite3.Row
    c = dbconn.cursor()
    
    c.execute(('insert into ranking (Name, Time) values '
                '(?,?)'), (name, wallTime))
    dbconn.commit()
except:
    subprocess.Popen("setxkbmap de", shell=True).communicate()

print "\n\n !!!!! Level 5 Ranking !!!!!\n"
c.execute("SELECT Name, Time FROM ranking ORDER BY Time")
i = 0
while True:
    i=i+1
    row = c.fetchone()
    if row == None:
        break
    print "{0:2d} {1:12} {2:8.5f} ".format(i, row[0], row[1])
