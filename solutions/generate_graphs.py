import matplotlib # install manually if not installed already
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

def read_data(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        time_data = sorted(eval(lines[0].strip()), key=lambda x: x[0])
        memory_data = sorted(eval(lines[1].strip()), key=lambda x: x[0])
    return time_data, memory_data

def plot_single_graph(data, ylabel , title, filename):
    assets_dir = Path('./assets')
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    sizes, measurements = zip(*data)
    
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, measurements, label='Efficient', marker='o')
    
    plt.xlabel('Problem Size')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
   
    file_path = assets_dir / filename
    plt.savefig(file_path)
    plt.close() 
    return file_path

def plot_graph(data_basic, data_efficient, ylabel, title, filename):
    assets_dir = Path('./assets')
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    sizes_basic, measurements_basic = zip(*data_basic)
    sizes_efficient, measurements_efficient = zip(*data_efficient)
    
    plt.figure(figsize=(10, 5))
    plt.plot(sizes_basic, measurements_basic, label='Basic', marker='o')
    plt.plot(sizes_efficient, measurements_efficient, label='Efficient', marker='o')
    
    plt.xlabel('Problem Size')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
   
    file_path = assets_dir / filename
    plt.savefig(file_path)
    plt.close() 
    return file_path

path_basic = Path('./graph_data_basic.txt')
path_efficient = Path('./graph_data_efficient.txt')

time_basic, memory_basic = read_data(path_basic)
time_efficient, memory_efficient = read_data(path_efficient)

time_graph_path = plot_graph(time_basic, time_efficient, 'Time (milliseconds)', 'Problem Size vs Time Usage', 'time_graph.png')
print(f"Time graph saved at: {time_graph_path}")

memory_graph_path = plot_graph(memory_basic, memory_efficient, 'Memory Usage (KBs)', 'Problem Size vs Memory Usage', 'memory_graph.png')
print(f"Memory graph saved at: {memory_graph_path}")

memory_graph_path = plot_single_graph(memory_efficient, 'Memory Usage (KBs)', 'Problem Size vs Memory Usage', 'memory_graph_efficient_only.png')
print(f"Memory graph saved at: {memory_graph_path}")