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

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    str_1, str_2 = read_and_generate_strings(input_file)
    
    # print strings for testing (delete before submission)
    if str_1 and str_2:
        print("Generated String 1:", str_1)
        print("Generated String 2:", str_2)