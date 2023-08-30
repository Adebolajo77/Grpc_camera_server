import queue
import threading
import time
import cv2
import asyncio
import grpc
import numpy as np
import pipeline_pb2 as pb2
import pipeline_pb2_grpc as pb2_grpc


class GrpcCameraClient:

    def __init__(self, host='localhost', port=50053, camera_id=1):
        self.port = port
        self.host = host
        self.stub = None
        self.camera_id = camera_id
        self.queue_port = queue.Queue(maxsize=1)

        thread = threading.Thread(target=self.start_async)
        thread.start()

    async def stream(self, stub):
        method_name = f"Stream{self.camera_id}"
        stream_method = getattr(stub, method_name)

        async for response in stream_method(pb2.StreamRequest()):
            frame_data = response.frame
            frame_array = np.frombuffer(frame_data, dtype=np.uint8)
            frame = cv2.imdecode(frame_array, flags=cv2.IMREAD_COLOR)
            if self.queue_port.qsize() == 0:
                self.queue_port.put(frame)
            await asyncio.sleep(0.001)

    async def connect(self):
        async with grpc.aio.insecure_channel(f'{self.host}:{self.port}') as channel:
            self.stub = pb2_grpc.StreamingPipelineStub(channel)
            await self.stream(self.stub)

    def start(self):
        asyncio.run(self.connect())

    def start_async(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.connect())

    def read(self):
        if self.queue_port.qsize() == 0:
            return None
        return self.queue_port.get()

