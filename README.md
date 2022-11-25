# onnx-tools README

Small command line tools in Python for working with ONNX files:

- Create a simple ONNX file with given opset version. This can used for testing parsing, consuming and executing a ONNX file.
- Dump out a summary of the properties of an ONNX file

## Dependencies

`python3 -m pip install onnx==1.12.0`

## Usage

| script | purpose | usage |
|---|---|---|
| `create_example_onnx_with_version.py` | Create a simple ONNX file with given opset version. This can used for testing parsing, consuming and executing a ONNX file. | `python3 create_example_onnx_with_version.py <output file path> <general opset version>` |
| `describe_onnx.py` | Dump out a summary of the properties of an ONNX file. Properties include: general opset version, IR version, file size, producer, producer version ... | `python3 describe_onnx.py <onnx file path>` |

### Example usage with output

#### create_example_onnx_with_version.py

```
python3 create_example_onnx_with_version.py ~/temp/my-model_v13.pnnx 13
```

```
onnx library version 1.12.0
Saved new ONNX file to ~/temp/my-model_v13.pnnx with target general opset version 13
```

#### describe_onnx.py

```
python3 describe_onnx.py ~/temp/my-model.onnx
```

```
Loading ONNX file at '~/temp/my-model.onnx'
 - file size 6 KB
 - loading via onnx library version 1.12.0

This input file uses:

 - domain = ''
 - ir_version = '8'
 - opset_import = '[version: 17
]'


producer_name 'onnx-cli'
producer_version ''
 - IR_VERSION_FIELD_NUMBER = '1'
 - OPSET_IMPORT_FIELD_NUMBER = '8'
 - PRODUCER_VERSION_FIELD_NUMBER = '3'
 - MODEL_VERSION_FIELD_NUMBER = '5'
 - model_version = '0'
 ```

## References

- [ONNX versions](https://github.com/onnx/onnx/blob/main/docs/Versioning.md)

## Licence

MIT
