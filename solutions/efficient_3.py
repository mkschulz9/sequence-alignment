import sys
import time
import psutil
import copy

memory_history = []

def argmin(a):
    return min(range(len(a)), key=lambda x : a[x])

def zeros(m, n):
    DP = []
    for i in range(m + 1):
        row = []
        for j in range(n + 1):
            row.append(0.)
        DP.append(row)
    return DP

def generate_string(base_string, indices):
    current_string = base_string
    
    for index in indices:
        if index < len(current_string):
            current_string = current_string[:index + 1] + current_string + current_string[index + 1:]
        else:
            current_string += current_string
    return current_string

def read_and_generate_strings(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        
        strings = []
        indices = []
        current_base_string = lines[0]

        for line in lines[1:]:
            try:
                index = int(line)
                indices.append(index)
            except ValueError:
                generated_string = generate_string(current_base_string, indices)
                strings.append(generated_string)
                
                indices = []
                current_base_string = line
        
        generated_string = generate_string(current_base_string, indices)
        strings.append(generated_string)

        return strings

def top_down_pass(DP, str_1, str_2):
    aligned_str_1 = ""
    aligned_str_2 = ""
    m = len(str_1)
    n = len(str_2)
    i, j = m, n
    while i != 0 and j != 0:
        mismatch = mismatch_cost[str_1[i-1]][str_2[j-1]] + DP[i-1][j-1]
        skip_str_1 = gap_penalty + DP[i-1][j]
        skip_str_2 = gap_penalty + DP[i][j-1]
        min_index = argmin([mismatch, skip_str_1, skip_str_2])

        if min_index == 0:
            aligned_str_1 += str_1[i-1]
            aligned_str_2 += str_2[j-1]
            i -= 1
            j -= 1
        elif min_index == 1:
            aligned_str_1 += str_1[i-1]
            aligned_str_2 += "_"
            i -= 1
        else:
            aligned_str_1 += "_"
            aligned_str_2 += str_2[j-1]
            j -= 1
            
        # update_memory()

    while i > 0:
        aligned_str_1 += str_1[i-1]
        aligned_str_2 += "_"
        i -= 1
        # update_memory()
    while j > 0:
        aligned_str_1 += "_"
        aligned_str_2 += str_2[j-1]
        j -= 1
        # update_memory()

    return aligned_str_1[::-1], aligned_str_2[::-1]

def sequence_alignment_basic(str_1, str_2, gap_penalty, mismatch_cost):
    m = len(str_1)
    n = len(str_2)
    DP = zeros(m+1, n+1)
    # update_memory()
    
    for i in range(m+1):
        DP[i][0] = i * gap_penalty
        update_memory()
    for j in range(n+1):
        DP[0][j] = j * gap_penalty
        update_memory()
    for i in range(1, m+1):
        for j in range(1, n+1):
            DP[i][j] = min(
                mismatch_cost[str_1[i-1]][str_2[j-1]] + DP[i-1][j-1],
                gap_penalty + DP[i-1][j],
                gap_penalty + DP[i][j-1]
            )
        update_memory()
    return DP, DP[m][n]

def build_table(X, Y, gap_penalty, mismatch_cost):
    m = len(X)
    n = len(Y)
    DP_old = [0]*(n+1) 
    DP_cur = [0]*(n+1)

    for i in range(1, n+1):
        DP_old[i] = i * gap_penalty
    # update_memory()
    
    for i in range(1, m+1):
        DP_cur[0] = i * gap_penalty
        # update_memory()
        for j in range(1, n+1):
            DP_cur[j] = min(
                mismatch_cost[X[i-1]][Y[j-1]] + DP_old[j-1],
                gap_penalty + DP_old[j],
                gap_penalty + DP_cur[j-1]
            )
        update_memory()
        DP_old = copy.deepcopy(DP_cur)
        update_memory()
    
    return DP_cur

def divide_and_conquer(X, Y, gap_penalty, mismatch_cost):
    m = len(X)
    n = len(Y)
    if m < 2 or n < 2:
        DP, cost = sequence_alignment_basic(X, Y, gap_penalty, mismatch_cost)
        X_edit, Y_edit = top_down_pass(DP, X, Y)
        update_memory()
        return cost, X_edit, Y_edit

    cost_xl = build_table(X[:m//2], Y, gap_penalty, mismatch_cost)
    cost_xr = build_table(X[m//2:][::-1], Y[::-1], gap_penalty, mismatch_cost)

    update_memory()
    
    places_to_cut = [cost_xl[j] + cost_xr[n - j] for j in range(n + 1)]
    min_cost = min(places_to_cut)
    c = places_to_cut.index(min_cost)

    update_memory()
    
    cost_l, x_l, y_l = divide_and_conquer(X[:m//2], Y[:c], gap_penalty, mismatch_cost)
    cost_r, x_r, y_r = divide_and_conquer(X[m//2:], Y[c:], gap_penalty, mismatch_cost)

    update_memory()
    
    return (cost_l+cost_r, x_l+x_r, y_l+y_r)

def get_alignment_cost(aligned_str_1, aligned_str_2, gap_penalty, mismatch_cost):
    # This function will compute the alignment cost between the given aligned strings
    m = len(aligned_str_1)
    if len(aligned_str_2) != m:
        return -1
    cost = 0.
    for i in range(m):
        if aligned_str_1[i] == "_" or aligned_str_2[i] == "_":
            cost += gap_penalty
        else:
            cost += mismatch_cost[aligned_str_1[i]][aligned_str_2[i]]
    return cost

def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss / 1024)  # memory in KB
    return memory_consumed

def time_wrapper(function, *args, **kwargs):
    start_time = time.time()
    result = function(*args, **kwargs)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000  # time in milliseconds
    return result, time_taken

def reset_memory():
    global memory_history
    memory_history = []
    
def update_memory():
    global memory_history
    memory_history.append(process_memory())

if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    
    str_1, str_2 = read_and_generate_strings(input_file_path)

    gap_penalty = 30
    mismatch_cost = {
        'A': {'A': 0, 'C': 110, 'G': 48, 'T': 94},
        'C': {'A': 110, 'C': 0, 'G': 118, 'T': 48},
        'G': {'A': 48, 'C': 118, 'G': 0, 'T': 110},
        'T': {'A': 94, 'C': 48, 'G': 110, 'T': 0}
    }
    
    memory_before = process_memory()
    memory_history.append(memory_before)
    (cost, aligned_str_1, aligned_str_2), time_taken = time_wrapper(divide_and_conquer, str_1, str_2, gap_penalty, mismatch_cost)
    
    peak_memory_usage = max(memory_history) - memory_before
    reset_memory() 

    with open(output_file_path, 'w') as file:
         file.write(f"{int(cost)}\n")
         file.write(f"{aligned_str_1}\n")
         file.write(f"{aligned_str_2}\n")
         file.write(f"{time_taken}\n")
         file.write(f"{peak_memory_usage}")
         
    # collect data for generating graphs & write data to file
    import os 
    
    directory = 'datapoints'
    time_results = []
    memory_results = []
    problem_sizes = []
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        str_1, str_2 = read_and_generate_strings(file_path)
        problem_size = len(str_1) + len(str_2)
        problem_sizes.append(problem_size) 
        
        memory_before = process_memory()
        memory_history.append(memory_before)
        (cost, aligned_str_1, aligned_str_2), time_taken = time_wrapper(divide_and_conquer, str_1, str_2, gap_penalty, mismatch_cost)
        
        peak_memory_usage = max(memory_history) - memory_before
        reset_memory() 
        
        time_results.append(time_taken)
        memory_results.append(peak_memory_usage)
    
    with open('graph_data_efficient.txt', 'w') as file:
        # create two sets of tuples; one for (problem_size, time_taken) and one for (problem_size, memory_used)
        time_results_output = ', '.join(f"({problem_sizes[i]}, {time_results[i]})" for i in range(len(problem_sizes))) + '\n'
        memory_results_output = ', '.join(f"({problem_sizes[i]}, {memory_results[i]})" for i in range(len(problem_sizes))) + '\n'
        
        file.write(time_results_output)
        file.write(memory_results_output)