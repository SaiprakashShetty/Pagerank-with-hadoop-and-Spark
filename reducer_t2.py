#!/usr/bin/env python3
import sys
node_current = None
current_count = 0
node = None
for line in sys.stdin:
	line = line.strip()
	node, page_Rank = line.split('\t')
	try:
		page_Rank = float(page_Rank)
	except ValueError:
		continue
	if node_current==node:
		cumulative += page_Rank
	else:
		if node_current:
			new_pr=0.15+0.85*cumulative
			round(new_pr,5)
			print('%s, %f' % (node_current, new_pr))
		cumulative = page_Rank
		node_current= node
if node_current==node:
	new_pr=0.15+0.85*cumulative
	round(new_pr,5)
	print('%s, %f' % (node_current, new_pr))
