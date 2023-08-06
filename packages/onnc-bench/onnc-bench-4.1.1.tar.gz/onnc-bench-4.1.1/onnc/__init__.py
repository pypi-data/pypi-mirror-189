import os
import pkg_resources
from loguru import logger

protobuf_ver = pkg_resources.get_distribution("protobuf").version
if protobuf_ver > '3.20.3':
    if not os.environ.get('PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'):
        os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = "python"
        logger.warning(
            "Set environment variable: "
            "PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python. This will use "
            "pure-Python parsing and will be much slower. Alternatively, "
            "you can downgrade the protobuf package to 3.20.x or lower.")