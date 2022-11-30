# clog

`clog.py` is a simple script to tail (with the -f option) a syslog generated file that is sent by CGNAT on MX-SPC3.  
This script strips away some unnecessary fields to match the log by MS-MPC.  Currently, the 
cleaned up log is send to console but can be easily modified to send via system or python3 log 
facilities.

Command:
```
usage: clog.py [-h] [-c] [-f] [logfile]

positional arguments:
  logfile        input syslog file. Default: test.log

optional arguments:
  -h, --help     show this help message and exit
  -c, --console  use STDIN as input, overrides filename
  -f, --tail     tail the default input
```
## Using the -c option
The script can also be configured to receive the input from stdin, typically this could be to receive
the decompressed file bytestream from lzo or zip. clog can be used to remove the extra fields using pipes 
without the use of intermediate files. An example of this could be:

`lzop -dc test.log.lzo | ./clog.py -c | xz > test.log.xz`

In actual production, you may want to use the -T0 or -Tn to enable xz to use multiple cores for the 
fastest compression and processing as it is likely that xz will be the bottlenecking process.

## Using the file option
A demo can be viewed [here](https://asciinema.org/a/LfGPJHUbVZbOXgt7b3CSZ76Ib).  This recording will
be removed by 28/2/2022.

To simulate new logs going into `test.log`, you can open another terminal window and do:
`cat 1.log >> test.log` to create the 1st line of the sample log
`cat 2.log >> test.log` to create the 2nd line of the sample log

If you have access to more logs, you can simply concat mulitple lines into test.log. `clog.py` will 
run till it runs out of lines and then sleep for 1 second before checking again.

## Using the --tail option

Please note the previous -t that has been changed to -f to be consistent with other common CLI (eg. tail -f)
You can use `clog -f filename` or `clog -cf` if you want clog to tail a file or stdin respectively.
