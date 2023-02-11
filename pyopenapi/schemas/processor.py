from pyopenapi.commons.buffer import Buffer
from pyopenapi.commons.utils import get_value_dict
from pyopenapi.data_type import DataType
from pyopenapi.options import ProcessorOption
from pyopenapi.schemas.processor_java import process_schema_lang_java


def process_schemas(options: ProcessorOption, buffer: Buffer, schemas):
    if schemas is not None:
        for key_schema in schemas:
            __process_schema__(options, buffer, key_schema, schemas[key_schema])


def __process_schema__(options: ProcessorOption, buffer: Buffer, key, schema):
    schema_data_type = DataType()
    schema_data_type.key = key
    schema_data_type.type = schema["type"]
    schema_data_type.properties = __process_schema_properties__(get_value_dict("properties", schema))

    if options.lang == "java":
        process_schema_lang_java(options, buffer, schema_data_type)


def __process_schema_properties__(properties):
    properties_schema = {}
    if properties is not None:
        for key_property in properties:
            property_value = properties[key_property]
            properties_schema[key_property] = __process_schema_property__(key_property, property_value)
    return properties_schema


def __process_schema_property__(key, property_value):
    property_type = DataType()
    property_type.key = key
    property_type.type = get_value_dict("type", property_value)
    property_type.format = get_value_dict("format", property_value)
    return property_type
