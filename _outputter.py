import json

import _number_helper

class Outputter:
    """Outputs properties in different formats"""

    def __init__(self):
        self.properties = []

    def add_property(self, name, value):
        name = name.replace(" ", "_")
        name = name.replace("(", "")
        name = name.replace(")", "")
        if not _number_helper.is_numeric(value):
            value = str(value)
        self.properties.append({name: value})

    def to_json(self):
        data = dict()
        data['properties'] = self.properties
        json_object = json.dumps(data, indent=2)
        return json_object

    def __str__(self):
        return "\n".join(self.properties)
