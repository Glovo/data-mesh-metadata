from os import listdir

from model import ValidationException
from validator import validate_schema


def validate(base_path):
    all = listdir(base_path)

    if len(all) != 2:
        raise ValidationException(f"Metadata folder should have one directory and one file, instead {all}")

    domain_file = next(filter(lambda x: ".yml" in x, all), None)
    result, error_message = validate_schema(f"{base_path}/{domain_file}", "./schema/domain_schema.yml")

    if result:
        print("Successful validation")
    else:
        print("Validation failed")
        print(error_message)
        exit(1)


if __name__ == '__main__':
    validate("metadata")