import os
from typing import List, Tuple
from matplotlib.ticker import MultipleLocator
from PIL import Image
import matplotlib.pyplot as plt

def plot_spikes(data: List[Tuple[float, float]], spikes: List[Tuple[float, float]], file_name: str, out_folder='tmp'):
	if not os.path.exists(out_folder):
		os.makedirs(out_folder)
	
	if not data:
		return
	
	if spikes:
		X_spike, y_spike = zip(*spikes)
	else:
		X_spike, y_spike = [], []


	X, y = zip(*data)

	# settings for the plot
	plt.figure(figsize=(180, 10))
	ax = plt.gca()
	ax.xaxis.set_major_locator(MultipleLocator(10))
	ax.xaxis.set_minor_locator(MultipleLocator(1))
	plt.xlabel('X')
	plt.ylabel('y')
	plt.title('Line Plot: ' + file_name)
	plt.grid(True)


	# plot data 
	plt.plot(X, y, marker='o', linestyle='-', color='b')

	# plot spikes using a bold vertical line
	# at the same time, display the index of the sike around the line
	for i in range(len(spikes)):
		plt.axvline(x=X_spike[i], color='r', linewidth=4)
		plt.text(X_spike[i]+5, y_spike[i], str(i+1), fontsize=12, color='r')



	# save the plot
	plt.savefig(os.path.join(out_folder, file_name+'.jpg'))
	plt.savefig(os.path.join(out_folder, file_name+'.pdf'))


# vertically merge all images in 'out' folder into a single image
def merge_images(input_foler='tmp', out_folder='out'):
	if not os.path.exists(out_folder):
		os.makedirs(out_folder)
	images = [Image.open(os.path.join(input_foler, img)) for img in os.listdir(input_foler) if img.endswith('.jpg') and not img.startswith('merged')]
	widths, heights = zip(*(i.size for i in images))

	total_width = max(widths)
	total_height = sum(heights)

	new_im = Image.new('RGB', (total_width, total_height))

	y_offset = 0
	for im in images:
		new_im.paste(im, (0, y_offset))
		y_offset += im.size[1]

	new_im.save(os.path.join(out_folder, 'merged.jpg'))
	new_im.save(os.path.join(out_folder, 'merged.pdf'))

	
if __name__ == '__main__':
	pass
	# data_l = [(float(i), float(sin(i*2*pi/360))) for i in range(700)]
	# spike_l = [(float(i), float(sin(i*2*pi/360))) for i in range(100, 600, 100)]
	# plot_spikes(data_l, spike_l, 'sin(i*2*pi/360)')
	# merge_images()