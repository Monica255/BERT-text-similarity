# export FLASK_APP=${HOME}/test-heroku2/main.py 
# Get the directory of the current script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Construct the file path of the Python file
PYTHON_FILE="$SCRIPT_DIR/main.py"

# Export FLASK_APP with the Python file path
export FLASK_APP="$PYTHON_FILE"
export FLASK_ENV=development
python3 -m flask run --host=0.0.0.0 --port 8000 --debugger