import pickle
import os


AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def load_blob(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def write_temp(name, content):
    path = "/tmp/" + name
    with open(path, "w") as f:
        f.write(content)
    return path


def list_dir(user_path):
    os.system("ls " + user_path)
