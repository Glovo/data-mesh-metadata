from cerberus import Validator
import yaml


def _load_doc(data_file):
    with open(data_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exception:
            raise exception


def validate_schema(data_file, schema_file):
    schema = _load_doc(schema_file)
    v = Validator(schema)
    doc = _load_doc(data_file)
    result = v.validate(doc, schema)
    return result, v.errors


if __name__ == '__main__':
    validate_schema()
