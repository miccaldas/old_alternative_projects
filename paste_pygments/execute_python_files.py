import os
import subprocess


def access_py_files():
    directory = "/home/mic/python/paste_pygments/python_config_files/"
    for file in os.listdir(directory):
        cmd = "python " + file
        subprocess.run(cmd, cwd=directory, shell=True)


if __name__ == "__main__":
    access_py_files()
