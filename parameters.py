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

writer_list = ['\nExtra bits \n\n']

nanoflow_list = ['Nanoflow \n \n']
instrument_list = ['\nInstrument \n \n']
triwave_DC_list = ['\nTriwave DC \n \n']
triwave_list = ['\nTriwave \n \n']
trapping_list = ['\nTrapping \n \n']
ims_config_list =['\nIMS Config \n \n']

for item in writing_list[0]:

	################
	# Nanoflow tab #
	################

	if "Capillary (kV)" in item:
		nanoflow_list.append(item + '\n')
	if "Sampling Cone" in item:
		nanoflow_list.append(item + '\n')
	if "Extraction Cone" in item:
		nanoflow_list.append(item + '\n')
	if "Source Temperature" in item:
		nanoflow_list.append(item + '\n')
	if "Cone Gas" in item:
		nanoflow_list.append(item + '\n')
	
	##################
	# Instrument tab #
	##################

	if "Trap Collision Energy" in item:
		instrument_list.append(item + '\n')
	if "Transfer Collision Energy" in item:
		instrument_list.append(item + '\n')
	if "Source Gas" in item:
		instrument_list.append(item + '\n')
	if "Trap Gas" in item:
		instrument_list.append(item + '\n')
	if "IMS Gas" in item:
		instrument_list.append(item + '\n')

	##################
	# Triwave DC tab #
	##################

	if "Trap DC Entrance" in item:
		triwave_DC_list.append(item + '\n')
	if "Trap DC Bias" in item:
		triwave_DC_list.append(item + '\n')
	if "Trap DC Exit" in item:
		triwave_DC_list.append(item + '\n')
	if "IMS DC Entrance" in item:
		triwave_DC_list.append(item + '\n')
	if "IMS DC Exit" in item:
		triwave_DC_list.append(item + '\n')
	if "Transfer DC Entrace" in item:
		triwave_DC_list.append(item + '\n')
	if "Transfer DC Exit" in item:
		triwave_DC_list.append(item + '\n')

	###############
	# Triwave tab #
	###############


	if "IMS Wave Height" in item:
		triwave_list.append(item + '\n')
	if "IMS Wave Velocity" in item:
		triwave_list.append(item + '\n')
	if "Transfer Wave Height" in item:
		triwave_list.append(item + '\n')
	if "Transfer Wave Velocity" in item:
		triwave_list.append(item + '\n')
	
	################
	# Trapping tab #
	################

	if "Trap Manual" in item:
		trapping_list.append(item + '\n')


	##################
	# IMS config tab #
	##################

	# variable wave height, wave height ramp
	if "Variable Wave height" in item:
		ims_config_list.append(item + '\n')
	if "Wave Height Ramp" in item:
		ims_config_list.append(item + '\n')
	if "Wave Height Start" in item:
		ims_config_list.append(item + '\n')
	if "Wave Height End" in item:
		ims_config_list.append(item + '\n')
	if "Wave Height Using" in item:
		ims_config_list.append(item + '\n')
	if "Wave Height Ramp" in item:
		ims_config_list.append(item + '\n')
	if "Vairable Wave Velocity" in item:
		ims_config_list.append(item + '\n')
	if "Wave Velocity Ramp" in item:
		ims_config_list.append(item + '\n')
	if "Wave Velocity Start" in item:
		ims_config_list.append(item + '\n')
	if "Wave Velocity End" in item:
		ims_config_list.append(item + '\n')
	if "Wave Velocity Using" in item:
		ims_config_list.append(item + '\n')



	##########
	# Extras #
	##########

	if "Start Mass" in item:
		writer_list.append(item + '\n')
	if "End Mass" in item:
		writer_list.append(item + '\n')
	if "MSMS End Mass" in item:
		writer_list.append(item + '\n')
	if "Backing" in item:
		writer_list.append(item + '\n')
	if "LM Resolution" in item:
		writer_list.append(item + '\n')
	if "HM Resolution" in item:
		writer_list.append(item + '\n')


write = open(experiment_name + '_parameters.txt', 'w+')
for item in nanoflow_list:
	write.write(item)

for item in instrument_list:
	write.write(item)

for item in triwave_DC_list:
	write.write(item)

for item in triwave_list:
	write.write(item)

for item in trapping_list:
	write.write(item)

for item in ims_config_list:
	write.write(item)

for item in writer_list:
	write.write(item)