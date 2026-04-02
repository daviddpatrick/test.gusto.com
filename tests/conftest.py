import pytest


def pytest_addoption(parser):
    parser.addoption("--test_env", default="us", help="Named config in common/config/<env>.json")
