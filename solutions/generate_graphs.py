import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for file generation
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def read_data(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        time_data = sorted(eval(lines[0].strip()), key=lambda x: x[0])
        memory_data = sorted(eval(lines[1].strip()), key=lambda x: x[0])
    return time_data, memory_data

def plot_graph(data_basic, data_efficient, ylabel, title, filename):
    # Ensure the directory exists
    assets_dir = Path('./assets')
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    # Unpack data
    sizes_basic, measurements_basic = zip(*data_basic)
    sizes_efficient, measurements_efficient = zip(*data_efficient)
    
    # Create figure and axis
    plt.figure(figsize=(10, 5))
    plt.plot(sizes_basic, measurements_basic, label='Basic', marker='o')
    plt.plot(sizes_efficient, measurements_efficient, label='Efficient', marker='o')
    
    # Labeling the graph
    plt.xlabel('Problem Size')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    
    # Save the figure
    file_path = assets_dir / filename
    plt.savefig(file_path)
    plt.close()  # Close the plot to free memory
    return file_path

# Paths to the data files
path_basic = Path('./graph_data_basic.txt')
path_efficient = Path('./graph_data_efficient.txt')

# Read the data
time_basic, memory_basic = read_data(path_basic)
time_efficient, memory_efficient = read_data(path_efficient)

# Plotting and saving time usage graph
time_graph_path = plot_graph(time_basic, time_efficient, 'Time (milliseconds)', 'Problem Size vs Time Usage', 'time_graph.png')
print(f"Time graph saved at: {time_graph_path}")

# Plotting and saving memory usage graph
memory_graph_path = plot_graph(memory_basic, memory_efficient, 'Memory Usage (KBs)', 'Problem Size vs Memory Usage', 'memory_graph.png')
print(f"Memory graph saved at: {memory_graph_path}")
