#!python3
from sys import argv

import config
import util_file

def find_version_by(ir_version, opset_ai_version, versions):
    for version in versions:
        if version["ir_version"] == str(ir_version) and version["opset_version_ai_onnx"] == str(opset_ai_version):
            return version["onnx_version"]
    return None

def main(ir_version, opset_ai_version):
    versions = util_file.read_json_from_file(config.ONNX_VERSIONS_JSON_PATH)
    version = find_version_by(ir_version, opset_ai_version, versions)
    if version is None:
        print("Unknown ONNX version")
    else:
        print(f"ONNX version {version}")

if len(argv) != 3:
    print(f"USAGE: {argv[0]} <IR Version> <opset general version (ai.onnx)>")
    exit(1)

if __name__ == "__main__":
    main(argv[1], int(argv[2]))
