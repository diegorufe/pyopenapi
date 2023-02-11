import yaml
from yaml.loader import SafeLoader

from pyopenapi.options import ProcessorOption
from pyopenapi.processor import process

# Open the file and load the file
with open('example.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    options = ProcessorOption()
    options.base_package = "com.example"
    print(process(options, data).data)
