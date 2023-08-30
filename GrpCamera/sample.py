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









