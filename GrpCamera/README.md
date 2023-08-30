# Video Streaming Pipeline with gRPC

This repository contains a Python implementation for a video streaming pipeline using gRPC. The code sets up a gRPC server that streams video frames from a camera to multiple clients. Clients can connect to different streams to receive video frames in real-time.

## Requirements

Before running the code, ensure you have the following libraries installed:

- gRPC: `pip install grpcio grpcio-tools`
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`


# Video Streaming Pipeline with gRPC - Installation

To set up and run the video streaming pipeline with gRPC, follow these steps:


## Prerequisite for grpc server
- install python3-venv      # Create and Activate Virtual Environment
- install python 

## Installation

- git clone https://github.com/Adebolajo77/Grpc_camera_server.git
- cd Grpc_camera_server
- sudo chmod +x install.sh
- ./install.sh

## or 


## . Create and Activate Virtual Environment

Run the following commands in your terminal:

```bash

# Create the virtual environment
python3 -m venv grpc_server

# Activate the virtual environment
source grpc_server/bin/activate

## Usage
1. Clone or download this repository.

2. Install the required libraries using the commands provided above requirements.txt.

3. Run the server python code_geneartor.py 10.    10 is the number of ports you want to exposed to the client

4. Adjust the camera source if needed in the code:
```bash


