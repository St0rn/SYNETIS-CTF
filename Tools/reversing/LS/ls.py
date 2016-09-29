#
#======================================================================
# 
#    88888888
#   88      888                                         88    88
#  888       88                                         88
#  788           Z88      88  88.888888     8888888   888888  88    8888888.
#   888888.       88     88   888    Z88   88     88    88    88   88     88
#       8888888    88    88   88      88  88       88   88    88   888
#            888   88   88    88      88  88888888888   88    88     888888
#  88         88    88  8.    88      88  88            88    88          888
#  888       ,88     8I88     88      88   88      88   88    88  .88     .88
#   ?8888888888.     888      88      88    88888888    8888  88   =88888888
#       888.          88
#                    88    www.synetis.com
#                 8888  Consulting firm in management and information security
# 
# Fabien DROMAS - Security Consultant @ Synetis | 0xbadcoded
#
#--
#SYNETIS | 0xbadcoded
#CONTACT: www.synetis.com | ww.0xbadcoded.com
#======================================================================
#
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

def getType(bin):
 get=commands.getoutput("file "+bin+" | grep dynamically")
 if get:
  return 1
 else:
  return 0

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
 
def hook(bin):
 if getType(bin):
   if len(argv)>2:
    print "\n[+] The binary is dynamically linked!"
    arch=commands.getoutput("file test/stage1.bin | grep 'ELF 64'")
    if arch:
     print "[+] Launch 64 bit hook\n"
     system("LD_PRELOAD=lib64/hook.so ./"+bin+" aaaaaa")
    else:
     print "[+] Launch 32 bit hook\n"
     system("LD_PRELOAD=lib32/hook32.so ./"+bin+" aaaaaa")
   else:
    print "\n[+] The binary is dinamically linked!"
    arch=commands.getoutput("file test/stage1.bin | grep 'ELF 64'")
    if arch:
     print "[+] Launch 64 bit hook\n"
     system("LD_PRELOAD=lib64/hook.so ./"+bin)
    else:
     print "[+] Launch 32 bit hook\n"
     system("LD_PRELOAD=lib32/hook32.so ./"+bin)
 else:
   print "\nfail..."

if __name__ == '__main__':
 if len(argv)<2:
  print "Usage: python %s fucking_binary optional_args" %argv[0]
  exit(0)
 else:
  bin=argv[1]
  performStrings(bin)
  print ""
  ltrace(bin)
  print ""
  c=raw_input("Can you perfom function hooking? y/n: ")
  if c=="n":
   exit(0)
  else:
   hook(bin)
