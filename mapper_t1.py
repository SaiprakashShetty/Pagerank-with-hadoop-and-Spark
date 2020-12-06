#!/usr/bin/env python3
import sys
for line in sys.stdin:
	line = line.strip()
	if line.startswith('#'):
		continue
	try:
		from_node,to = line.split('\t')
	except:
		continue
	print ('%s\t%s' % (from_node,to))
