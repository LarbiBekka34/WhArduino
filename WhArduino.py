#!/usr/bin/env python2

import re
from serial.tools.list_ports import comports

# This section load the `boards.txt` file in a dictionary of the following format
# { 'model0': ['Name of arduino board',
#             vid,
#             pid],
# 'model1': ['Name of arduino board',
#             vid,
#             pid]
# ... }
# where vid and pid are two lists of the same length, and vid[i]:pid[i] are the
# vendor id and product id couple for the board

boards_file = open('./boards.txt', 'r')
boards_lines = boards_file.readlines()

model = {}

for line in boards_lines:
	match = re.search(r'(^[a-z]*)\.name=(.*)', line)
	if match:
		model[match.group(1)] = [match.group(2), [], []] # the two empty lists are the vid and pid lists

for line in boards_lines:
	for k in model.keys():
		match_vid = re.search(r'^' + k + r'\.vid\.[0-9]*=0x([A-F0-9]{4})', line)
		match_pid = re.search(r'^' + k + r'\.pid\.[0-9]*=0x([A-F0-9]{4})', line)
		if match_vid:
			model[k][1].append(match_vid.group(1))
		elif match_pid:
			model[k][2].append(match_pid.group(1))

prods = {'0001':'Arduino Uno'      , '0043':'Arduino Uno R3',
		 '0010':'Arduino Mega 2560', '0042':'Arduino Mega 2560 R3',
		 '003F':'Arduino Mega ADK' , '0044':'Arduino Mega ADK R3'}

#Arduino vendor ID: 0x2341
#Old Arduinos use the FTDI VID/PID (VID=0x0403)
VIDs  = ['2341', '0403']

sdevs = comports()
intdev = []
for dev in sdevs:
	if dev[2]!= 'n/a':
		intdev.append(dev)

ptn = 'USB VID:PID=([A-F0-9]{4}):([A-F0-9]{4}) '
arduinos = []
for dev in intdev:
	match = re.search(ptn,dev[2])
	if match and match.group(1) == VIDs[0]:
		if match.group(2) in prods:
			data = (prods[match.group(2)], dev[0])
		else:
			data = ('Arduino', dev[0])
	elif match and match.group(1) == VIDs[1]:
			data = ('FTDI', dev[0])
	else:
		data = ('Unknown', dev[0])
	arduinos.append(data)

if not arduinos:
	print 'No arduino connected !!!'
else:
	print 'Connected Arduino device(s):'
	for ard in arduinos:
		print ard[0], ' at ', ard[1]
