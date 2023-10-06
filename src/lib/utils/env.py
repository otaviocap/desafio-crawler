import os


def is_running_on_container() -> bool:
    try:
        return os.environ["OS_ENV"] == "container"
    except:
        return False
