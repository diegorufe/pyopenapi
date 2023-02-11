from pyopenapi.commons.buffer import Buffer
from pyopenapi.commons.utils import get_value_dict
from pyopenapi.options import ProcessorOption
from pyopenapi.schemas.processor import process_schemas


def process(options: ProcessorOption, data):
    buffer = Buffer()
    if data is not None:
        __process_components__(options, buffer, data, "schemas")
    return buffer


def __process_components__(options: ProcessorOption, buffer: Buffer, data, key):
    components = get_value_dict("components", data)
    if components is not None:
        if key in components:
            if key == "schemas":
                process_schemas(options, buffer, get_value_dict(key, components))
