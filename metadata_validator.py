import os
from os import listdir
from os.path import exists

from model import ValidationException
from validator import validate_schema

DOMAIN_CONFIG_FILE = "domain.metadata.yaml"
DOMAIN_SCHEMA_FILE = "schema/domain_schema.yaml"

PRODUCT_SCHEMA_FILE = "schema/product_schema.yaml"


def handle_validation_results(file_name, result, error_message):
    if result:
        print(f"{file_name} successfully validated!!")
    else:
        raise ValidationException(f"Failed to validate {file_name}. Errors: {error_message}")


def validate(base_path):
    base_folder_elements = listdir(base_path)

    domain_file = next(filter(lambda x: x == DOMAIN_CONFIG_FILE, base_folder_elements), None)
    if domain_file:
        result, error_message = validate_schema(f"{base_path}/{domain_file}", DOMAIN_SCHEMA_FILE)
    else:
        raise ValidationException(f"Cannot find {DOMAIN_CONFIG_FILE} in the base path")

    handle_validation_results(domain_file, result, error_message)

    all_folders = next(os.walk(base_path))[1]
    product_config_files = map(lambda x: f"{x}/{x}.yml", all_folders)
    for product_config_file in product_config_files:
        if exists(f"{base_path}/{product_config_file}"):
            result, error_message = validate_schema(f"{base_path}/{product_config_file}", PRODUCT_SCHEMA_FILE)
            handle_validation_results(product_config_file, result, error_message)


if __name__ == '__main__':
    validate("metadata")