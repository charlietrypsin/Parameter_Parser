# basic structure

# open .raw files, read extern.inf files
# for line, "if [X] presnt then: print line"
# have relevant parameters copied into a table to be inserted into files

import ConfigParser
from os import listdir, walk
from os.path import isfile, join
import csv
import sys
import argparse

parser = argparse.ArgumentParser(description='Produce .txt file output from _extern.inf')
parser.add_argument ('dataFn', help='Folder Name', action='store')
args = parser.parse_args()
dataFn = args.dataFn

f = []
for dirpath, dirnames, filenames in walk(dataFn):
	if "_extern.inf" in filenames:
		foldername = dirpath.split('/')[-1]
		#print(foldername)
		experiment_name = foldername.replace('.raw', '')
		print(foldername)
		with open(dirpath + "/" + "_extern.inf") as info:
			for line in info:
				writing_list = zip(*(line1.strip().split('\t\t\t\t\t') for line1 in info))

for item in writing_list[0]:
	print(item)

writer_list = []


for item in writing_list[0]:
	if "Capillary (kV)" in item:
		writer_list.append(item + '\n')
	if "Sampling Cone" in item:
		writer_list.append(item + '\n')
	if "Source Temperature" in item:
		writer_list.append(item + '\n')
	if "Trap Collision Energy" in item:
		writer_list.append(item + '\n')
	if "Start Mass" in item:
		writer_list.append(item + '\n')
	if "End Mass" in item:
		writer_list.append(item + '\n')
	if "MSMS End Mass" in item:
		writer_list.append(item + '\n')
	if "Trap DC Bias" in item:
		writer_list.append(item + '\n')
	if "Backing" in item:
		writer_list.append(item + '\n')
	if "IMS Wave Height" in item:
		writer_list.append(item + '\n')
	if "IMS Wave Velocity" in item:
		writer_list.append(item + '\n')
	if "Transfer Wave Height" in item:
		writer_list.append(item + '\n')
	if "Transfer Wave Velocity" in item:
		writer_list.append(item + '\n')
	if "LM Resolution" in item:
		writer_list.append(item + '\n')
	if "HM Resolution" in item:
		writer_list.append(item + '\n')

# for item in writer_list:
# 	print(item)

write = open(experiment_name + '_parameters.txt', 'w+')
for item in writer_list:
	write.write(item)
