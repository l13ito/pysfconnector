# -*- coding: utf-8 -*-
# Version v.03
# Author: Angel Herrera Falcon
# Email :litos1985@gmail.com
#
import option
import sys
import os

opt = 0
sf = None
file = None
if len(sys.argv) == 3:
    file = str(sys.argv[2])
os.system('cls' if os.name == 'nt' else 'clear')
print "Welcome to pysfconnector v.0.3\n"


while opt >= 0 or opt < 6:
    print "************************"
    print "          Menu          "
    print "(1). Login to Salesforce"
    print "(2). SOQL Query"
    print "(3)  Retrieve metadata (Planned)"
    print "(4). Read the csv (Not finished) "
    print "(5). Read the csv detailed"
    print "(6). Format to UTF-8"
    print "(7). Exit"
    print "************************\n"
    opt = raw_input("Enter your option: ")
    if opt.isdigit():
        opt =int(opt)
        if opt == 1:
            sf = option.switch(opt, sf, file)
        elif 4 <= opt <=6 and file == None:
            os.system('cls' if os.name == 'nt' else 'clear')
            print "There is not any file as argument. (Example: pfconnector.py filename.csv). It is mandatory for option(" + str(opt)+")."  
        else:
            option.switch(opt, sf, file)
    else: 
        raw_input("Please insert a number. Press Enter to continue...") 