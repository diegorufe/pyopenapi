import os
from pathlib import Path

from pyopenapi.commons.buffer import Buffer
from pyopenapi.data_type import DataType
from pyopenapi.options import ProcessorOption

__formats__java_lang_types__ = {"string": "String", "integer": "Integer"}


def process_schema_lang_java(options: ProcessorOption, buffer: Buffer, schema: DataType):
    script_dir = os.path.dirname(__file__)
    template = Path(script_dir + '/templates/JavaTemplate.txt').read_text()
    template = template.replace("[SCHEMA_NAME]", schema.key)

    properties_builder = ""

    if schema.properties is not None:
        for key_property in schema.properties:
            property_value: DataType = schema.properties[key_property]
            properties_builder = properties_builder + "\n"

            properties_builder = properties_builder + "\tprivate " + __formats__java_lang_types__[property_value.type]

            properties_builder = properties_builder + " " + property_value.key

            properties_builder = properties_builder + ";\n"

    template = template.replace("[SCHEMA_PROPERTIES]", properties_builder)
    template = template.replace("[SCHEMA_PACKAGE]", options.base_package)

    if options.output == ":memory:":
        if "components" not in buffer.data:
            buffer.data["components"] = {}

        if "schemas" not in buffer.data["components"]:
            buffer.data["components"]["schemas"] = {}

        schemas = buffer.data["components"]["schemas"]
        schemas[schema.key] = template
    else:
        # TODO Store in external path
        pass
