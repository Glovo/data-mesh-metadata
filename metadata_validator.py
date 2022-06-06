from os import listdir
from os.path import join

from model import ValidationException
from validator import validate_schema


def print_results(file_name, result, error_message):
    if result:
        print(f"{file_name} successfully validated!!")
    else:
        print("Validation failed")
        print(error_message)
        exit(1)

def validate(base_path):
    base_folder_elements = listdir(base_path)

    if len(base_folder_elements) != 2:
        raise ValidationException(f"Metadata folder should have one directory and one file, instead {base_folder_elements}")

    domain_file = next(filter(lambda x: ".yml" in x, base_folder_elements), None)
    result, error_message = validate_schema(f"{base_path}/{domain_file}", "./schema/domain_schema.yml")

    print_results(domain_file, result, error_message)

    product_files =  listdir(join(base_path, "products"))

    for product in product_files:
        result, error_message = validate_schema(f"{base_path}/products/{product}", "./schema/product_schema.yml")

        print_results(product, result, error_message)


if __name__ == '__main__':
    validate("metadata")