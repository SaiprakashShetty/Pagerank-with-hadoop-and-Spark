#!/usr/bin/env python3
import sys

if(len(sys.argv)>1):
	v=sys.argv[1]
f = open(v, "r")
pagerank=dict()
for line in f:
	node,pr=line.split(", ")
	try:
		node=int(node)
	except:
		pass
	pagerank[node]=float(pr)

for line in sys.stdin:
	line = line.strip()
	from_node,adj = line.split("\t")
	nodes1=adj.strip("'").split(',')
	nodes = [int(ele) if ele.isdigit() else ele for ele in nodes1]
	length=len(nodes)
	try:
		from_node=int(from_node)
	except:
		pass
	print('%s\t%f' % (from_node,0.0))
	for word in nodes: 
		try:
			if word in pagerank:
				contri=pagerank[from_node]/length
				print ('%s\t%f' % (word,contri))
		except:
			continue
