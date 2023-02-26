#!python3
import json
import urllib.request

import config
import util_file
import util_string

VERSIONING_MD_URL = "https://raw.githubusercontent.com/onnx/onnx/main/docs/Versioning.md"

TEMP_PATH = "temp/versioning.md"

print(f"Downloading file from {VERSIONING_MD_URL}...")
urllib.request.urlretrieve(VERSIONING_MD_URL, TEMP_PATH)
print("[done]")

md_lines = util_file.read_lines_from_file(TEMP_PATH)

def build_onnx_version(onnx_version, ir_version, opset_version_ai_onnx):
        return {
            "onnx_version": onnx_version,
            "ir_version": ir_version,
            "opset_version_ai_onnx": opset_version_ai_onnx
        }

"""
Parse MD lines like this:

1.0|3|1|1|-
"""
def parse_versions_out_of_md_line(line):
    versions = line.split('|')
    if len(versions) < 3:
         return None
    return build_onnx_version(versions[0], versions[1], versions[2])

"""
Parse MD lines like this:

## Released Versions

ONNX version|IR version|Opset version ai.onnx|Opset version ai.onnx.ml|Opset version ai.onnx.training
------------|-------------------|---------------------|------------------------|------------------------------
1.0|3|1|1|-
1.1|3|5|1|-
1.1.2|3|6|1|-
"""
def parse_versions_out_of_md(md_lines):
    versions = []
    # just one # so more robust
    RELEASE_VERSIONS_HEADER = "# Released Versions"
    next_line_index = 0
    line = md_lines[next_line_index]
    next_line_index = next_line_index + 1
    while(RELEASE_VERSIONS_HEADER not in line):
        line = md_lines[next_line_index]
        next_line_index = next_line_index + 1

    TABLE_DATA_START = "--|--"
    while(TABLE_DATA_START not in line):
        line = md_lines[next_line_index]
        next_line_index = next_line_index + 1
    
    while(not util_string.is_blank(line)):
        line = md_lines[next_line_index]
        next_line_index = next_line_index + 1

        version = parse_versions_out_of_md_line(line)
        if version:
            versions.append(version)

    return versions


versions = parse_versions_out_of_md(md_lines)

print(f"Writing {len(versions)} ONNX versions to {config.ONNX_VERSIONS_JSON_PATH} ...")

json_object = json.dumps(versions, indent=2)

util_file.write_to_file(json_object, config.ONNX_VERSIONS_JSON_PATH)

print("[done]")
