#!/usr/bin/env python3

from time import sleep

f = open('test.log')
s = ' '
line = f.readline()

while(1): # Loop forever
  while(line):
    elements = line.split(' ')
    if (len(elements)>1): # Ensure line is actually a log (not an empty line)
      if (elements[10] == 'created'):
        print(s.join(elements[:16]), elements[27]) # Grab first 17 elements, followed by 28th
      if (elements[10] == 'closed'):
        print(s.join(elements[:16]), elements[34])
    line = f.readline()
  sleep(1) # Sleep 1 second
  f.seek(0,1) # This is to reset the EOF, seeking 0 offset from current pos
  line = f.readline() # Attempt to read again