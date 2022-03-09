# clog

clog is a simple script to tail (with the -t option) a syslog generated file that is sent by CGNAT on MX-SPC3.  
This script strips away some unnecessary fields to match the log by MS-MPC.  Currently, the 
cleaned up log is send to console but can be easily modified to send via system or python3 log 
facilities.

Command:
```
usage: clog.py [-h] [-c] [-t] [filename]

positional arguments:
  filename       input syslog file. Default: test.log

optional arguments:
  -h, --help     show this help message and exit
  -c, --console  use STDIN as input, overrides filename
  -t, --tail     tail the default input
```
## Using the -c option
The script can also be configured to receive the input from stdin, typically this could be to receive
the decompressed file bytestream from zip. clog can be used to remove the extra fields using pipes 
without the use of intermediate files. An example of this could be:

`unzip -cq test.log | clog -c | xz > test.xz`

## Using the file option
A demo can be viewed [here](https://asciinema.org/a/LfGPJHUbVZbOXgt7b3CSZ76Ib).  This recording will
be removed by 28/2/2022.

To simulate new logs going into `test.log`, you can open another terminal window and do:
`cat 1.log >> test.log` to create the 1st line of the sample log
`cat 2.log >> test.log` to create the 2nd line of the sample log

If you have access to more logs, you can simply concat mulitple lines into test.log. Main.py will 
run till it runs out of lines and then sleep for 1 second before checking again.
