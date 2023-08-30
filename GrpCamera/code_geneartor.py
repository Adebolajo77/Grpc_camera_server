import os
from grpc_tools import protoc


def generate_proto_file(num_streams):
    # Define the content of the proto file
    proto_content = f"""
syntax = "proto3";

package pipeline;

service StreamingPipeline {{
{generate_rpc_methods(num_streams)}
}}

message StreamRequest {{
  // Add fields here if needed
}}

{generate_stream_response_messages(num_streams)}
"""

    # Write the content to a .proto file
    proto_file_path = os.path.join(os.getcwd(), 'pipeline.proto')
    with open(proto_file_path, 'w') as file:
        file.write(proto_content)

    return proto_file_path


def generate_rpc_methods(num_streams):
    rpc_methods = []
    for i in range(num_streams):
        rpc_methods.append(f"  rpc Stream{i + 1}(StreamRequest) returns (stream StreamResponse{i + 1});")
    return '\n'.join(rpc_methods)


def generate_stream_response_messages(num_streams):
    stream_response_messages = []
    for i in range(num_streams):
        stream_response_messages.append(f"message StreamResponse{i + 1} {{\n  bytes frame = 1;\n}}")
    return '\n\n'.join(stream_response_messages)


if __name__ == '__main__':
    num_streams = 24  # Number of streams
    proto_file_path = generate_proto_file(num_streams)

    protoc.main((
        '',
        f'-I{os.getcwd()}',
        '--python_out=.',
        '--pyi_out=.',
        '--grpc_python_out=.',
        proto_file_path,
    ))
