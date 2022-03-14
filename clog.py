#!/usr/bin/env python3

from time import sleep
import argparse, sys

# if there are quoted strings, we can use 
# from shlex import split
# out = split(quoted_string)

parser = argparse.ArgumentParser(description='Remove fields from MX-SPC3 generated syslog \
    to be similar to MS-MPC.')
parser.add_argument("-c", "--console", action="store_true", 
    help="use STDIN as input, overrides filename")
parser.add_argument("-t", "--tail", action="store_true", 
    help="tail the default input") 
parser.add_argument("filename", default="test.log", nargs="?",
    help="input syslog file. Default: test.log")
args = parser.parse_args()

# Select imput
if args.console: 
  f = sys.stdin
else:
  f = open(args.filename)

s = ' '
line = f.readline() # critical that we do not use readlines on multi GB logfiles!

while(1): # Loop forever and break later if we don't need to
  while(line):
    elements = line.split(s)
    if (len(elements) > 9): # Ensure line is actually a log (not a random line)
      if (elements[10] == 'created'):
        print(s.join(elements[:16]), elements[27]) # Grab first 17 elements, followed by 28th
      if (elements[10] == 'closed'):
        print(s.join(elements[:16]), elements[34])
    line = f.readline()
  if not(args.tail): # Do not continue to attempt to read if not tailing
    break 
  sleep(1) # Sleep 1 second to wait for new logs
  f.seek(0,1) # This is to reset the EOF, seeking 0 offset from current pos
  line = f.readline() # Attempt to read again
