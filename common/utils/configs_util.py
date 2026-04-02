"""Helpers for loading environment-specific test configuration."""

import json
import logging
import os
from typing import Any

from common.utils.env_loader import get_env

logger = logging.getLogger(__name__)
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_DIR = os.path.abspath(os.path.dirname(os.path.dirname(CURRENT_DIR)))


def load_config(env_name: str = "us") -> dict[str, Any]:
    """Loads config for the given environment and applies env var overrides."""
    env_name = env_name or "us"
    rel_path = f"common/config/{env_name}.json"
    config = load_file_from_root(rel_path)
    overrides = {
        "ui_base_url": get_env("UI_BASE_URL"),
        "api_base_url": get_env("API_BASE_URL"),
        "ui_username": get_env("UI_USERNAME"),
        "ui_password": get_env("UI_PASSWORD"),
        "shared_auth_base_url": get_env("SHARED_AUTH_BASE_URL"),
        "shared_auth_endpoint": get_env("SHARED_AUTH_ENDPOINT"),
        "shared_auth_expected_text": get_env("SHARED_AUTH_EXPECTED_TEXT"),
    }
    for key, value in overrides.items():
        if value:
            config[key] = value
    return config


def load_file_from_root(rel_file: str) -> dict[str, Any]:
    """Loads a JSON file relative to the repository root."""
    env_file_path = f"{CONFIG_DIR}/{rel_file}"
    with open(env_file_path, encoding="utf-8") as handle:
        return json.load(handle)


def create_directory_if_necessary(directory: str) -> None:
    """Creates a directory if it does not already exist."""
    if not os.path.exists(directory):
        try:
            logger.info("Creating directory: %s", directory)
            os.makedirs(directory)
        except FileExistsError:
            logger.info("Directory already exists")
