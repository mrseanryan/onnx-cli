import onnx

from sys import argv

import _onnx_example_creator

def main(output_filepath, output_opset_general_version) -> None:
    model_def = _onnx_example_creator.create(output_opset_general_version)
    onnx.save(model_def, output_filepath)
    print(f"Saved new ONNX file to {output_filepath} with target general opset version {output_opset_general_version}")


if len(argv) != 3:
    print(f"USAGE: {argv[0]} <output file path> <opset general version>")
    exit(1)

print(f"onnx library version {onnx.__version__}")

if __name__ == "__main__":
    main(argv[1], int(argv[2]))
