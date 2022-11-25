"""
describe_onnx.py <path to onnx file> [--help --json]
"""
import os
import onnx

from optparse import OptionParser

import _outputter

#usage() - prints out the usage text, from the top of this file :-)
def print_usage():
    print(__doc__)

parser = OptionParser(usage=__doc__)
parser.add_option("-j", "--json", dest="output_as_json",
    action='store_const',
    const=True, default=False,
    help="Output as JSON")

(options, args) = parser.parse_args()

if len(args) != 1:
    print_usage()
    exit(1)

INPUT_ONNX = args[0]

def get_file_size_kb(filepath):
    file_stats = os.stat(filepath)
    return round(file_stats.st_size / 1024);

outputter = _outputter.Outputter()

def print_property(property, value):
    if options.output_as_json:
        outputter.add_property(property, value)
    else:
        print(f"{property}: {value}")

def print_text_only(text):
    if not options.output_as_json:
        print(text)

print_property(f"ONNX file", INPUT_ONNX)

print_property("file size (KB)", get_file_size_kb(INPUT_ONNX))

onnx_model = onnx.load(INPUT_ONNX)

print_property("described-with-onnx-library-version", onnx.__version__)

print_text_only("")

# versions - see https://github.com/onnx/onnx/blob/main/docs/Versioning.md
print_property("domain", onnx_model.domain)
print_property("ir_version", onnx_model.ir_version)
print_property("opset_import", onnx_model.opset_import)

print_text_only("")

# JSON like dump: onnx_model.__str__()

print_property("producer_name", onnx_model.producer_name)
print_property("producer_version", onnx_model.producer_version)

print_property("IR_VERSION_FIELD_NUMBER", onnx_model.IR_VERSION_FIELD_NUMBER)
print_property("OPSET_IMPORT_FIELD_NUMBER", onnx_model.OPSET_IMPORT_FIELD_NUMBER)
print_property("PRODUCER_VERSION_FIELD_NUMBER", onnx_model.PRODUCER_VERSION_FIELD_NUMBER)
print_property("MODEL_VERSION_FIELD_NUMBER", onnx_model.MODEL_VERSION_FIELD_NUMBER)

print_property("model_version", onnx_model.model_version)

if options.output_as_json:
    print(outputter.to_json())
else:
    print("[done]")
