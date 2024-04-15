# Sequence Alignment Solutions - CSCI-570 Spring 2024 Final Project

- Welcome to our CSCI-570 Spring 2024 Final Project repository. This project focuses on the practical implementation of two distinct algorithms to solve the Sequence Alignment problem. These solutions encompass a dynamic programming approach and a memory-efficient strategy combining dynamic programming with divide-and-conquer.

## Sequence Alignment Problem
- The Sequence Alignment problem is a classic problem in bioinformatics that involves finding the optimal alignment between two sequences. The goal is to identify the best alignment that minimizes the total cost of matching, mismatching, and gap penalties. More detailed information about the Sequence Alignment problem can be found [here](https://en.wikipedia.org/wiki/Sequence_alignment).

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
