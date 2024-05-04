import sys
import time
import psutil
import numpy as np


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

def sequence_alignment(str_1, str_2, gap_penalty, mismatch_cost):
    m = len(str_1)
    n = len(str_2)
    DP = np.zeros((m+1,n+1))
    for i in range(m+1):
        DP[i,0] = i*gap_penalty
    for j in range(n+1):
        DP[0,j] = j*gap_penalty
    for i in range(1, m+1):
        for j in range(1, n+1):
            DP[i,j] = min(mismatch_cost[str_1[i-1]][str_2[j-1]] + DP[i-1,j-1],
                           gap_penalty + DP[i-1,j],
                           gap_penalty + DP[i,j-1])
    return DP, DP[m,n]

def top_down_pass(DP, str_1, str_2):
    aligned_str_1 = ""
    aligned_str_2 = ""
    m = len(str_1)
    n = len(str_2)
    i, j = m, n

    # Go through the constructed DP table to get the accurate string alignments
    while i!=0 and j!=0:
        mismatch = mismatch_cost[str_1[i-1]][str_2[j-1]] + DP[i-1,j-1]
        skip_str_1 = gap_penalty + DP[i-1,j]
        skip_str_2 = gap_penalty + DP[i,j-1]
        min_index = np.argmin(np.array([mismatch, skip_str_1, skip_str_2]))

        if min_index == 0:
            aligned_str_1 += str_1[i-1]
            aligned_str_2 += str_2[j-1]
            i = i-1
            j = j-1
        elif min_index == 1:
            aligned_str_1 += str_1[i-1]
            aligned_str_2 += "_"
            i = i-1
        else:
            aligned_str_1 += "_"
            aligned_str_2 += str_2[j-1]
            j = j-1

    # We need to align the strings with "_" once only one string has been fully consumed
    while i > 0:
        aligned_str_1 += str_1[i-1]
        aligned_str_2 += "_"
        i = i-1
    while j > 0:
        aligned_str_1 += "_"
        aligned_str_2 += str_2[j-1]
        j = j-1

    # Reverse the strings and return them
    return aligned_str_1[::-1], aligned_str_2[::-1]

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
    (DP, cost), time_taken = time_wrapper(sequence_alignment, str_1, str_2, gap_penalty, mismatch_cost)

    aligned_str_1, aligned_str_2 = top_down_pass(DP, str_1, str_2)
    memory_after = process_memory()
    memory_used = memory_after - memory_before
    
    with open(output_file_path, 'w') as file:
        file.write(f"{int(cost)}\n")
        file.write(f"{aligned_str_1}\n")
        file.write(f"{aligned_str_2}\n")
        file.write(f"{time_taken}\n")
        file.write(f"{memory_used}")