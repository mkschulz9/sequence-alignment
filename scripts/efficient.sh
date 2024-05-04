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

# upgrade pip and install required packages
echo "Upgrading pip and installing required packages..."
pip install --upgrade pip
pip install numpy psutil

# run the basic program
python ./solutions/efficient_3.py $INPUT_FILE $OUTPUT_FILE