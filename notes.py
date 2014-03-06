#!/usr/bin/env python

import sys, datetime, shutil, os.path
from ConfigParser import SafeConfigParser

# get file info
configfile = os.path.expandvars("$HOME/.notes.cfg")

parser = SafeConfigParser()
parser.read(configfile)
dirstr = os.path.expandvars(parser.get('files', 'notedir'))
fstr = parser.get('files', 'notefile')
fname = os.path.join(dirstr, fstr)

if len(sys.argv) == 1:
    from subprocess import call
    call(["cat", "-n",fname])

elif sys.argv[1]=="--delete" and len(sys.argv)>=3:
    try:
        line_to_delete = int(sys.argv[2])
    except:
        sys.exit(1)
    f = open(fname,"r")
    lines = f.readlines()
    f.close()
    if line_to_delete <=0 or line_to_delete > len(lines):
        print "[ERROR] Invalid Note Number:", line_to_delete
        sys.exit(1)
    f = open(fname,"w")
    line_number = 1;
    for line in lines:
        if line_number!=line_to_delete:
            f.write(line)
        line_number=line_number+1    
    f.close()
    print "[INFO] Note Deleted"	

else:
    f = open(fname, 'a')
    timestr = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    f.write("- %s [%s]\n" % (' '.join(sys.argv[1:]), timestr))
    f.close()
