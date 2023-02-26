# onnx-tools README

Command line tools in Python for working with ONNX files:

- Create a simple ONNX file with given opset version. This can used for testing parsing, consuming and executing a ONNX file.
- Dump out a summary of the properties of an ONNX file

## Dependencies

`python3 -m pip install onnx==1.12.0`

## Usage

| script | purpose | usage |
|---|---|---|
| `create_example_onnx_with_version.py` | Create a simple ONNX file with given opset version. This can used for testing parsing, consuming and executing a ONNX file. | `python3 create_example_onnx_with_version.py <output file path> <general opset version>` |
| `describe_onnx.py` | Dump out a summary of the properties of an ONNX file. Properties include: general opset version, IR version, file size, producer, producer version. Output can also be in JSON format. | `python3 describe_onnx.py <onnx file path> [--json]` |
| `map_ir_and_opset-ai-onnx_to_onnx_version.py` | Takes an IR version and opset version (for the 'ai.onnx' domain) and maps that to the closest ONNX version. | `python3 map_ir_and_opset-ai-onnx_to_onnx_version <IR version> <opset version>` |
| `update_map_ir-opset_to_onnx-version.py` | Updates the map that is used by `map_ir_and_opset-ai-onnx_to_onnx_version.py` by downloading a small markdown file from the onnx github repository. | `python3 update_map_ir-opset_to_onnx-version.py` |

### Example usage with output

#### create_example_onnx_with_version.py

```
python3 create_example_onnx_with_version.py ~/temp/my-model_v13.pnnx 13
```

OUTPUT:
```
onnx library version 1.12.0
Saved new ONNX file to ~/temp/my-model_v13.pnnx with target general opset version 13
```

#### describe_onnx.py

```
python3 describe_onnx.py ~/temp/my-model.onnx
```

OUTPUT:
```
ONNX file: ./temp/new_onnx_1.onnx
file size (KB): 6
described-with-onnx-library-version: 1.12.0

domain: 
ir_version: 8
opset_import: [version: 17
]

producer_name: onnx-cli
producer_version: 
IR_VERSION_FIELD_NUMBER: 1
OPSET_IMPORT_FIELD_NUMBER: 8
PRODUCER_VERSION_FIELD_NUMBER: 3
MODEL_VERSION_FIELD_NUMBER: 5
model_version: 0
[done]
 ```


#### describe_onnx.py with JSON output

```
python3 describe_onnx.py ~/temp/my-model.onnx --json
```

OUTPUT:
```
{
  "properties": {
    "ONNX_file": "./temp/new_onnx_1.onnx",
    "file_size_KB": 6,
    "described-with-onnx-library-version": "1.12.0",
    "domain": "",
    "ir_version": 8,
    "opset_import": "[version: 17\n]",
    "producer_name": "onnx-cli",
    "producer_version": "",
    "IR_VERSION_FIELD_NUMBER": 1,
    "OPSET_IMPORT_FIELD_NUMBER": 8,
    "PRODUCER_VERSION_FIELD_NUMBER": 3,
    "MODEL_VERSION_FIELD_NUMBER": 5,
    "model_version": 0
  }
}
```

#### update_map_ir-opset_to_onnx-version.py

```
python3 update_map_ir-opset_to_onnx-version.py
```

OUTPUT:
```
Downloading file from https://raw.githubusercontent.com/onnx/onnx/main/docs/Versioning.md...
[done]
Writing 19 ONNX versions to data/onnx-versions.json ...
[done]
```

#### map_ir_and_opset-ai-onnx_to_onnx_version.py

```
python3 map_ir_and_opset-ai-onnx_to_onnx_version.py 7 13
```

OUTPUT:
```
ONNX version 1.8.0
```

Example of looser match, by IR version and an opset version that is lower than the max supported for that ONNX version:
```
python3 map_ir_and_opset-ai-onnx_to_onnx_version.py 8 11
```

OUTPUT:
```
ONNX version 1.10.0
```

## References

- [ONNX versions - official spec](https://github.com/onnx/onnx/blob/main/docs/Versioning.md)
- [Blog post - with more tools](https://antipatterns.blogspot.com/2022/11/versions-and-properties-of-onnx-machine.html)

## Licence

MIT
