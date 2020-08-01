import os

ROOT_DIRECTORY = "/wa"

try:
    if not os.path.exists(ROOT_DIRECTORY):
        os.mkdir(ROOT_DIRECTORY)
except:
    pass


def touch(fname, times=None):
    """ Touch file in given path """
    with open(fname, 'a'):
        os.utime(fname, times)


def get_pwd():
    """ Returns present working directory """
    return os.getcwd()


def is_balena():
    """
    Check if the environment is Balena
    :return: True if Balena
    """
    return os.environ.get("BALENA")

