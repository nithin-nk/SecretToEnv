import base64
import json

import yaml


def get_secrets_from_json_file(file_path: str) -> dict:
    """
    Extract secrets from the given JSON file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as fp:
            data = json.load(fp)
        output = {}
        for key, value in data["data"].items():
            output[key] = base64.b64decode(value).decode("utf-8")
        return output
    except FileNotFoundError as e:
        print(f"File not found '{file_path}' - {e}")
    except Exception as e:
        print(f"Invalid input file '{file_path}' - {e}")


def get_secrets_from_yaml_file(file_path: str) -> dict:
    """
    Extract secrets from the given YAML file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as fp:
            data = yaml.safe_load(fp)
        output = {}
        for key, value in data["data"].items():
            output[key] = base64.b64decode(value).decode("utf-8")
        return output
    except FileNotFoundError as e:
        print(f"File not found '{file_path}' - {e}")
    except Exception as e:
        print(f"Invalid input file '{file_path}' - {e}")


if __name__ == "__main__":
    # opt = get_secrets_from_json_file("my-secret.json")
    opt = get_secrets_from_yaml_file("my-secret.yaml")
    print(opt)
