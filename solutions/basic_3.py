import sys

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
    DP = [[0] * m] * n
    for i in range(m):
        DP[0][i] = i*gap_penalty
    for j in range(n):
        DP[j][0] = j*gap_penalty
    for i in range(1, m):
        for j in range(1, n):
            DP[i][j] = min( mismatch_cost[str_1[i]][str_2[j]] + DP[i-1][j-1],
                           gap_penalty + DP[i-1][j],
                           gap_penalty + DP[i][j-1])
    return DP[m-1][n-1]

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    str_1, str_2 = read_and_generate_strings(input_file)
    
    # print strings for testing (delete before submission)
    if str_1 and str_2:
        print("Generated String 1:", str_1)
        print("Generated String 2:", str_2)

    gap_penalty = 30
    mismatch_cost = {
        'A': {'A': 0, 'C': 110, 'G': 48, 'T': 94},
        'C': {'A': 110, 'C': 0, 'G': 118, 'T': 48},
        'G': {'A': 48, 'C': 118, 'G': 0, 'T': 110},
        'T': {'A': 94, 'C': 48, 'G': 110, 'T': 0}
    }
    cost = sequence_alignment(str_1, str_2, gap_penalty, mismatch_cost)
    print(cost)