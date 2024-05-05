# system independent script to run a Python script using a virtual environment. 
# The script creates a virtual environment if it doesn't exist, installs required packages, and runs the specified Python script using the Python executable in the virtual environment. The script takes the version of the solution, input file, and output file as command-line arguments.

import subprocess
import sys
import os

def create_virtualenv(path):
    """ Create a virtual environment if it doesn't exist. """
    if not os.path.exists(path):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, '-m', 'venv', path])

def install_package(package):
    """ Install a package using pip. """
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"{package} is installed.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}.")

def run_python_script(env_path, script, *args):
    """ Run a Python script using the Python executable in the specified virtual environment. """
    python_exec = os.path.join(env_path, 'bin', 'python') if os.name != 'nt' else os.path.join(env_path, 'Scripts', 'python.exe')
    try:
        subprocess.check_call([python_exec] + [script] + list(args))
    except subprocess.CalledProcessError:
        print(f"Failed to run {script}.")

def main():
    # Define the path to the virtual environment and the script to run
    env_path = "./.venv"
    solution_version = sys.argv[1] if len(sys.argv) > 0 else 'basic'
    script_to_run = f"solutions/{solution_version}_3.py"
    input_file = sys.argv[2] if len(sys.argv) > 1 else 'input.txt'
    output_file = sys.argv[3] if len(sys.argv) > 2 else 'output.txt'

    # Create virtual environment
    create_virtualenv(env_path)

    # Install required packages
    required_packages = ['numpy', 'memory_profiler']
    for package in required_packages:
        install_package(package)

    # Run the Python script
    run_python_script(env_path, script_to_run, input_file, output_file)

if __name__ == "__main__":
    main()
