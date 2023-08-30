import asyncio
import threading
import types

import grpc
import cv2
import numpy as np

import pipeline_pb2 as pb2
import pipeline_pb2_grpc as pb2_grpc
import asyncio


class VideoStreamServicer(pb2_grpc.StreamingPipelineServicer):
    def __init__(self, number_streaming_ports=5):
        self.clients = []
        self.cap = cv2.VideoCapture(1)  # Open the default camera (change this as needed)

        self.num_streams = number_streaming_ports  # Number of stream functions needed
        self.queues = [asyncio.Queue(maxsize=1) for _ in range(self.num_streams)]

        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.producer())

        # Dynamically generate stream methods
        for i in range(self.num_streams):
            setattr(self, f"Stream{i + 1}", types.MethodType(self.generate_stream_method(i), self))

    async def producer(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Could not read frame.")
            else:
                for q in self.queues:
                    if q.qsize() == 0:
                        await q.put(frame)
            await asyncio.sleep(0.01)

    def generate_stream_method(self, stream_index):
        async def stream_method(self, request, context):
            client = context.peer()
            print(f"Client connected to Stream{stream_index + 1}: {client}")
            try:
                while True:
                    frame = await self.queues[stream_index].get()
                    _, encoded_frame = cv2.imencode('.jpg', frame)
                    yield getattr(pb2, f"StreamResponse{stream_index + 1}")(frame=encoded_frame.tobytes())
            finally:
                pass

        return stream_method


async def serve():
    server = grpc.aio.server()
    pb2_grpc.add_StreamingPipelineServicer_to_server(VideoStreamServicer(number_streaming_ports=5), server)
    server.add_insecure_port('[::]:50053')  # Change the port as needed

    await server.start()
    print("Server started...")
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
