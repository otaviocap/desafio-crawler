import os

from lib.utils.env import is_running_on_container


def test_env_on_container():
    os.environ["OS_ENV"] = "container"

    assert is_running_on_container()


def test_env_not_on_container():
    assert not is_running_on_container()
