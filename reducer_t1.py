#!/usr/bin/env python3
import sys

previous = None
current_count = 0
if(len(sys.argv)>1):
	v=sys.argv[1]
f = open(v, "w")
for line in sys.stdin:
	line = line.strip()
	from_node,to = line.split('\t')
	if previous == from_node:
		l.append(to)
	else:
		if previous:
			l.sort()
			#l1 = [int(ele) if ele.isdigit() else ele for ele in l]
			x=(",").join(l)
			#print(x)
			print('%s\t%s' % (previous, x))
			f.write('%s, %d\n' % (previous, 1))
		l=[]
		l.append(to)
		previous=from_node

if previous == from_node:
	l.sort()
	#l1 = [int(ele) if ele.isdigit() else ele for ele in l]
	x=(",").join(l)
	#print(x)
	print('%s\t%s' % (previous, x))
	f.write('%s, %d' % (previous, 1))
f.close()

