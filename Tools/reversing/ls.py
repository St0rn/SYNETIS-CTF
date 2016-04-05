#!/usr/bin/env python
# coding: utf8
#
# Author: St0rn - Security Consultant @ Synetis
# Contact: fabien.dromas@synetis.com
#
# Le££e CTF Team
# Le££e toi et marche!

import commands
from os import system
from sys import argv,exit

keys=['flag','CTF','FLAG','ctf']

# For evol
#def getType(bin):
# get=commands.getoutput("file "+bin+" | grep dynamically")
# if get:
#  return 1
# else:
#  return 0

def performStrings(bin):
 print "First analyse with keywords:"
 for i in keys:
  out=commands.getoutput("strings "+bin+" | grep "+i)
  if out:
   print "Here is your flag bitch!\n%s" %out
   break
 print "For more research the strings dump\n is saved with name %s.dump" %bin
 f=open(bin+".dump","w")
 f.write(commands.getoutput("strings "+bin))
 f.close()

def ltrace(bin):
 print "ltrace result:"
 system("/bin/chmod +x "+bin)
 print commands.getoutput("ltrace ./"+bin+ " aaaaaa")

if __name__ == '__main__':
 if len(argv)<2:
  print "Usage: python %s fucking_binary" %argv[0]
  exit(0)
 else:
  bin=argv[1]
  performStrings(bin)
  print ""
  ltrace(bin)
