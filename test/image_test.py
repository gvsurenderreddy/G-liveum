#!/usr/bin/python
import sys
args=sys.argv
if len(sys.argv)==2:
	fp=sys.argv[1]
	f=open(fp)
	f.seek(510)
	h=f.read(2)
	if h=="U\xaa":
		print "bootable"
	else:
		print "isnt bootable"
	f.close()
