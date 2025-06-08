import os
import json
import joblib
import yaml
import base64

from box import ConfigBox
from box.exceptions import BoxValueError
from segmentation import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: Any other errors.

    Returns:
        ConfigBox: ConfigBox object containing YAML data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories from a given list.

    Args:
        path_to_directories (list): List of directory paths.
        verbose (bool, optional): Logs creation messages if True. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Dictionary to be saved.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns its content.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: JSON data as a ConfigBox object.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary data using joblib.

    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Loaded object.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: File size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def decode_image(img_string: str, file_name: str):
    """Decodes a base64 image string and saves it as a file.

    Args:
        img_string (str): Base64 image string.
        file_name (str): Output file name.
    """
    img_data = base64.b64decode(img_string)
    with open(file_name, 'wb') as f:
        f.write(img_data)


def encode_image_into_base64(image_path: str) -> bytes:
    """Encodes an image file into a base64 string.

    Args:
        image_path (str): Path to the image file.

    Returns:
        bytes: Base64 encoded string.
    """
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read())
