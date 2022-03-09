#!/usr/bin/env python3

from time import sleep
import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--console", action="store_true", 
    help="use STDIN as input, overrides filename")
parser.add_argument("-t", "--tail", action="store_true", 
    help="tail the default input") 
parser.add_argument("filename", default="test.log", nargs="?",
    help="input syslog file. Default: test.log")
args = parser.parse_args()

if args.console: 
  f = sys.stdin
else:
  f = open(args.filename)

s = ' '
line = f.readline()

while(1): # Loop forever
  while(line):
    elements = line.split(s)
    if (len(elements) > 9): # Ensure line is actually a log (not a random line)
      if (elements[10] == 'created'):
        print(s.join(elements[:16]), elements[27]) # Grab first 17 elements, followed by 28th
      if (elements[10] == 'closed'):
        print(s.join(elements[:16]), elements[34])
    line = f.readline()
  if not(args.tail):
    break # Do not continue to read if not tailing
  sleep(1) # Sleep 1 second
  f.seek(0,1) # This is to reset the EOF, seeking 0 offset from current pos
  line = f.readline() # Attempt to read again
