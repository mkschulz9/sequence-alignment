# vars for input/output files
INPUT_FILE=$1
OUTPUT_FILE=$2

# path to virtual env
VENV_PATH="./.venv"

# create virtual env if it doesn't exist
if [ ! -d "$VENV_PATH" ]; then
    echo "Creating virtual environment..."
    python -m venv $VENV_PATH
fi

# activate the virtual env
source $VENV_PATH/Scripts/activate

# Function to check and install a package if not already installed
function check_and_install {
    PACKAGE=$1
    if ! pip list | grep -F $PACKAGE > /dev/null; then
        echo "Installing $PACKAGE..."
        pip install $PACKAGE
    else
        echo "$PACKAGE is already installed."
    fi
}

# Check and install necessary packages
check_and_install "numpy"
check_and_install "psutil"
check_and_install "memory_profiler"

# run the basic program
python ./solutions/basic_3.py $INPUT_FILE $OUTPUT_FILE

deactivate