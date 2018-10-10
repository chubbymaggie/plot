import os, sys
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLineCollection, HandlerTuple
import matplotlib.ticker as ticker
import numpy as np

def import_data(filepath):
	"""
	Import data file @filepath to plot. 
	"""
	data = []
	with open(filepath, "r") as f:
		for line in f:
			data.append(int(line.strip()))
	return data

def plot_multilines(data_arrays, tick_interval, xlabelrotation, linestyle_array, legend_array, legend_loc, xlabel_str, ylabel_str, savefilepath):
	"""
	Plot multiple lines (all encompassed in @data_arrays) in the same figure.
	x ticks have interval @tick_interval, and the tick labels are rotated at the angle @xlabelrotation.
	Each line has legend included in @legend_array which is located at @legend_loc, and line style @linestyle_array.
	x and y labels are named by @xlabel_str and @ylabel_str.
	The resulting plot is saved in @savefilepath.
	"""
	fig, ax = plt.subplots()
	# create x-axes for all plots in @data_arrays and plot all of them
	for pos, line in enumerate(data_arrays):
		timeline = np.arange(1, len(line) + 1)
		draw_line, = ax.plot(timeline, line, linestyle=linestyle_array[pos], label=legend_array[pos])
	# set x-axis ticks to be every @tick_interval 
	ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_interval))
	# set x-axis smallest value to be 0
	ax.set_xlim(left=0)
	# set y-axis smallest value to be 0
	ax.set_ylim(bottom=0)
	# tick appearance
	ax.tick_params(axis='x', labelrotation=xlabelrotation)
	# create legend for both lines
	ax.legend(loc=legend_loc, shadow=False)
	# set labels
	ax.set_xlabel(xlabel_str)
	ax.set_ylabel(ylabel_str)

	plt.savefig(savefilepath, format='pdf', bbox_inches='tight')

def print_instruction():
	print(
		"Usage: python plot.py\n")

if __name__ == "__main__":
	
	if (len(sys.argv) < 1):
		print_instruction()
		sys.exit(1)

	# plot the performance between streaming and analyzing
	stream_data = import_data("../data/stream-wget-attack-baseline-0.txt")
	analyze_data = import_data("../data/perf-wget-attack-baseline-0-hop-3-l-2000.txt")
	data_arrays = [stream_data, analyze_data]
	plot_multilines(data_arrays, 15, 45, ['-', '-'], ['stream', 'analyze'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/stream_analyze.pdf")

	# plot the performance with different hop counts
	hop1_data = import_data("../data/perf-wget-attack-baseline-0-hop-1-l-2000.txt")
	hop2_data = import_data("../data/perf-wget-attack-baseline-0-hop-2-l-2000.txt")
	hop3_data = import_data("../data/perf-wget-attack-baseline-0-hop-3-l-2000.txt")
	hop4_data = import_data("../data/perf-wget-attack-baseline-0-hop-4-l-2000.txt")
	hop5_data = import_data("../data/perf-wget-attack-baseline-0-hop-5-l-2000.txt")
	data_arrays = [stream_data, hop1_data, hop2_data, hop3_data, hop4_data, hop5_data]
	plot_multilines(data_arrays, 15, 45, ['--', '-', '-', '-', '-', '-'], ['stream', 'Hop = 1', 'Hop = 2', 'Hop = 3', 'Hop = 4', 'Hop = 5'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/hop.pdf")

	# plot the performance with various sketch sizes
	sketch1_data = import_data("../data/perf-wget-attack-baseline-0-hop-3-l-500.txt")
	sketch2_data = import_data("../data/perf-wget-attack-baseline-0-hop-3-l-1000.txt")
	sketch3_data = import_data("../data/perf-wget-attack-baseline-0-hop-3-l-2000.txt")
	sketch4_data = import_data("../data/perf-wget-attack-baseline-0-hop-3-l-3000.txt")
	data_arrays = [stream_data, sketch1_data, sketch2_data, sketch3_data, sketch4_data]
	plot_multilines(data_arrays, 15, 45, ['--', '-', '-', '-', '-'], ['stream', '|S| = 500', '|S| = 1,000', '|S| = 2,000', '|S| = 3,000'], 'lower right', 'Time (seconds)', 'Graph Size (# of Edges)', "../plot/sketch.pdf")

