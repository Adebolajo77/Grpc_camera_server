

#!/bin/bash

# Create the virtual environment
python3 -m venv grpc_server

# Activate the virtual environment
source grpc_server/bin/activate

# upgrade pip
python -m pip install --upgrade pip

# Install packages from requirements.txt
pip install -r requirements.txt

# Define the value for num_streams
num_streams=5

# Run the Python script to generate gRPC code
python code_geneartor.py $num_streams


echo "Virtual environment 'grpc_server' created and packages installed."