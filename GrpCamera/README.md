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

```bash```

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
```

## change the camera source if needed on gRPserver.py
```python
## Change the camera source if needed
self.cap = cv2.VideoCapture(1)  # Open the default camera (change this as needed)
ret, frame = self.cap.read()

server.add_insecure_port('localhost:50053')  # Change the host and port as needed

VideoStreamServicer(number_streaming_ports=5)
number_streaming_ports=5; number of port allowed to be exposed to the client
```

## basic function of the client side.
```python
## sample code with the client side package GrpcCameraClient.py
```python
from GrpcCameraClient import GrpcCameraClient

# instance of the GrpcCameraClient
camera_client = GrpcCameraClient(host='localhost', port=50053, camera_id=1)

host is the ip of the grpc server
port is the port of the grpc server
camera_id is the camera id  is the port number of the camera

```

## sample code with the client side package GrpcCameraClient.py
```python
import numpy as np
import cv2
from GrpCamera.GrpcCameraClient import GrpcCameraClient

if __name__ == "__main__":

    camera_client = GrpcCameraClient(host='localhost', port=50053, camera_id=1)
    try:
        while True:

            frame = camera_client.read()
            if frame is not None:
                cv2.imshow("Stream1", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Stopping the client.")
```







