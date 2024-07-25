import csv
from typing import List, Tuple

from src.algo import algo_l
from src.helper import remove_dir_contents
from src.plotting import merge_images, plot_spikes
fieldnames = ['timestamp(s)', 'score', "frame_idx"]

def load_result(result_csv_path):
	result = []
	with open(result_csv_path, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			result.append(row)
	return result

def run(data: List[Tuple[float, float]], spike_finder_algo):
	if spike_finder_algo.__name__.startswith("algo_threshold_v1"):
		value_threshold=float(0.55)
		spike_l = spike_finder_algo(data, value_threshold=value_threshold)
		plot_spikes(data_l, spike_l, spike_finder_algo.__name__ + f"_thld={value_threshold}")
	
	if spike_finder_algo.__name__.startswith("algo_threshold_v2"):
		for i in range(1, 10):
			slope_threshold=float(i*0.1)
			spike_l = spike_finder_algo(data, slope_threshold=slope_threshold)
			plot_spikes(data_l, spike_l, spike_finder_algo.__name__ + f"_thld={slope_threshold:.2f}")

if __name__ == "__main__":
	remove_dir_contents("tmp")
	remove_dir_contents("out")
	csv_path = "res/result.csv"
	result = load_result(csv_path)
	data_l = [(float(r[fieldnames[0]]), float(r[fieldnames[1]])) for r in result]

	for algo in algo_l:
		run(data_l, algo)


	merge_images()
	

