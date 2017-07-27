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
				writing_list = zip(*(line1.strip().split('\t') for line1 in info))


for item in writing_list[0]:
	print(item)
	
# print(writing_list[0])
			# writer_list = []
			# write = open(experiment_name + '_parameters.txt', 'w+')
			# writer = csv.writer(write, lineterminator = '\n')
			# for line in info:
			# 	if "Capillary (kV)" in line:
			# 		writer_list.append(line)
			# 	if "Sampling Cone" in line:
			# 		writer_list.append(line)
			# 	if "Source Temperature" in line:
			# 		writer_list.append(line)
			# 	if "Trap Collision Energy" in line:
			# 		writer_list.append(line)
			# 	if "Start Mass" in line:
			# 		writer_list.append(line)
			# 	if "MSMS End Mass" in line:
			# 		writer_list.append(line)
			# 	if "Trap DC Bias" in line:
			# 		writer_list.append(line)
			# 	if "Backing" in line:
			# 		writer_list.append(line)
			# 	if "IMS Wave Height" in line:
			# 		writer_list.append(line)
			# 	if "IMS Wave Velocity" in line:
			# 		writer_list.append(line)
			# 	if "Transfer Wave Height" in line:
			# 		writer_list.append(line)
			# 	if "Transfer Wave Velocity" in line:
			# 		writer_list.append(line)
			# 	if "LM Resolution" in line:
			# 		writer_list.append(line)
			# 	if "HM Resolution" in line:
			# 		writer_list.append(line)

			# print(writer_list)
			# writer.writerow(writer_list)

