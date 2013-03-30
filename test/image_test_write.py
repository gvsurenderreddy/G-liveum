#!/usr/bin/python
import sys
args=sys.argv
if len(sys.argv)==2:
	fp=sys.argv[1]
	f=open(fp)
	with open('/media/rushabh/Joli OS - 1.2 (LTS)', 'wb') as stream:
		stream.write(f.read(2))
	f.close()
