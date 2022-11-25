import os
import onnx
import sys

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} <input onnx file>")
    exit(1)

INPUT_ONNX = sys.argv[1]

def get_file_size_kb(filepath):
    file_stats = os.stat(filepath)
    return round(file_stats.st_size / 1024);

print(f"Loading ONNX file at '{INPUT_ONNX}")

print(f" - file size {get_file_size_kb(INPUT_ONNX)} KB")

onnx_model = onnx.load(INPUT_ONNX)

print(f" - loading via onnx library version {onnx.__version__}")
print("")

print("This input file uses:")
print("")

# import pdb
# pdb.set_trace()

# versions - see https://github.com/onnx/onnx/blob/main/docs/Versioning.md
print(f" - domain = '{onnx_model.domain}'")
print(f" - ir_version = '{onnx_model.ir_version}'")
print(f" - opset_import = '{onnx_model.opset_import}'")

print("")
print("")

# JSON like dump: onnx_model.__str__()

print(f"producer_name '{onnx_model.producer_name}'")
print(f"producer_version '{onnx_model.producer_version}'")

print(f" - IR_VERSION_FIELD_NUMBER = '{onnx_model.IR_VERSION_FIELD_NUMBER}'")
print(f" - OPSET_IMPORT_FIELD_NUMBER = '{onnx_model.OPSET_IMPORT_FIELD_NUMBER}'")
print(f" - PRODUCER_VERSION_FIELD_NUMBER = '{onnx_model.PRODUCER_VERSION_FIELD_NUMBER}'")
print(f" - MODEL_VERSION_FIELD_NUMBER = '{onnx_model.MODEL_VERSION_FIELD_NUMBER}'")

print(f" - model_version = '{onnx_model.model_version}'")


