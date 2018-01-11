#!/usr/bin/python -tt

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pickle
import os
import sys
import subprocess
import numpy as np
import scipy.io

extension = sys.argv[1]

figure_path = '../Figures/'

current_path = os.getcwd()

if os.path.exists(figure_path) == False:
	os.mkdir(figure_path)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
#files = ['ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-5-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-3-50-50-50-100.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-3-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-2-50-50-50-100.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-2-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-1-50-50-50-100.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-4-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-4-50-50-50-100.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-1-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-5-50-50-50-100.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-4-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-5-50-50-50-100.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-2-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-4-50-50-50-100.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-3-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-0-.5-0-.2-5-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-1-50-50-50-100-Reshuffle.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-1-50-50-50-100.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-2-50-50-50-100.txt', 'ThrHomoHeatmap-thrstep2.py-1000-15-0-.001-.5-0-.2-3-50-50-50-100.txt']

print files
for f in files:
	if '.mat' in f:
		board = scipy.io.loadmat(f)['A']

		fig, ax = plt.subplots()
		cax = ax.imshow(board.T, cmap = plt.cm.gist_yarg_r, origin = 'lower',  extent = [0, 0.5, 0, 50], aspect='auto')
		ax.set_title('Heatmap')
#		cbar = fig.colorbar(cax, ticks = [0, 500, 1000])
#		cbar.ax.set_yticklabels(['0', '0.5', '1'])
		ax.set_xlabel('Threshold difference ' + r'$\Delta\phi$')
		ax.set_ylabel('Linking prob ' + r'$p$')
#		cbar.set_label('Fraction of activated nodes ' + r'$\rho$')

		plt.savefig(figure_path + f[:-4] + '.' + extension)


#scratch_data_path = '/scratch/oh' + current_path[28:] + '/Data/'
#scratch_figure_path = '/scratch/oh' + current_path[28:] + '/Figures/'

##os.makedirs(scratch_data_path)
##os.makedirs(scratch_figure_path)

#ret = subprocess.call(['ssh', 'arabian-knights', 'mkdir -p ' + scratch_data_path])
#ret = subprocess.call(['ssh', 'arabian-knights', 'mkdir -p ' + scratch_figure_path])

#ret = subprocess.call(['ssh', 'arabian-knights', 'mv ' + current_path + '/Data/* ' + scratch_data_path])

#ret = subprocess.call(['ssh', 'arabian-knights', 'mv ' + current_path + '/Figures/* ' + scratch_figure_path])

