# Sequence Alignment Project - CSCI-570 Spring 2024
- Welcome to our CSCI-570 Spring 2024 Final Project repository. This project is centered around the practical application of two unique algorithms for solving the Sequence Alignment Problem. Our repo includes a 'basic' solution that utilizes a standard dynamic programming method and an 'efficient' solution that combines dynamic programming with a divide-and-conquer technique to significantly lessen the memory usage. The objective is to evaluate and contrast the efficiency of both methods in terms of time and memory consumption.

## Team Members & Table of Contents:
- Team Members:
    - [Matthew Schulz](https://github.com/mkschulz9)
    - [Ryan Marr](https://github.com/rmarrcode)
    - [Vedant Raval](https://github.com/Vedant2311)
- Table of Contents:
  - [Sequence Alignment Problem](#sequence-alignment-problem)
  - [Repository Structure](#repository-structure)
  - [How to Run the Code](#how-to-run-the-code)

## Sequence Alignment Problem
- The Sequence Alignment problem is a classic problem in bioinformatics that involves finding the optimal alignment between two sequences. The goal is to identify the best alignment that minimizes the total cost of matching, mismatching, and gap penalties. More detailed information about the Sequence Alignment problem can be found [here](https://en.wikipedia.org/wiki/Sequence_alignment).

## Repository Structure
- The repository is structured as follows:
    - `solutions/`: Contains the code for the basic and efficient solutions, as well as a file for generating graphs used in analysis.
        - `basic_3.py`: Contains the code for the basic solution.
        - `efficient_3.py`: Contains the code for the memory efficient solution.
        - `generate_graphs.py`: Contains the code to generate graphs for time and memory analysis of the solutions. Data is colected during execution of the solutions using the input data provided in the `datapoints` folder. You will need to uncomment the code in the solutions to collect the data.

        (**Note**: The solutions are written as standalone files as per the project requirements, so redundant code is present in both files.)
    - `scripts/`: Contains the script to run the solutions. 
        - `run_script.py`: A script to run the solutions independently of the environment.

        (**Note**: Disregard `basic.sh` and `efficient.sh` as they are only needed for project grading purposes.)
    - `datapoints/`: Contains sample inputs used by the solutions to collect time and memory data for generating graphs.
    - `sample-tests/`: Contains sample input and output files for running/testing the solutions.

## How to Run the Code
- Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/mkschulz9/sequence-alignment
```
- In order to run the code independent of the environment, we have provided a `run_script.py` file that can be used to execute the solutions using any OS. Simply run the following command in the terminal:
```bash
python ./scripts/run_script.py [solution_type] [input_file] [output_file]
```
- The `run_script.py` file takes three arguments:
    - `solution_type`: Which solution to run ('basic' or 'efficient').
    - `input_file`: The path to the input file.
    - `output_file`: The path to the output file where the alignment results will be written.

- Example command to run the basic solution, using sample input file `input1.txt` and writing the output to `output_basic.txt`:
```bash
python ./scripts/run_script.py basic ./sample-tests/input1.txt ./output_basic.txt
```

## Working Notes (delete before submission)
- string generation mechanism is the same irrespective of the basic or the
efficient version of the algorithm
- entire program (string generation, solution, write output) should be written in single file (may break those functions in different classes to make code
modular, but there should be only one file for consistency of submissions)
- strongly recommend to refer to lecture slides for the algorithm overview, and
NOT THE PSEUDOCODE PROVIDED IN KLEINBERG AND TARDOS textbook (prior experience, students opting for the latter reported lots of difficulties in implementation)
- DO NOT USE ANY LIBRARIES FOR WRITING YOUR ALGORITHMS (barring the standard ones)
- You should code both the basic version and memory-efficient algorithm (Even though the memory-efficient version will pass all the bounds of the simple version, you must not use the memory-efficient version in both of the sub-problems, otherwise the plots will not show the expected distinctions)
- sample code for memory and time calculaiton provided
