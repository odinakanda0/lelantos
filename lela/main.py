import os
import json
import subprocess
from datetime import datetime

def create_env(env_name=""):
    #TODO: Custom env names and directories
    """
    if env_name == "":
        env_name = '.venv'

    """

    #TODO: Allow users choose their version of python

    curr_dir = os.getcwd()
    venv_dir = os.path.join(curr_dir, r'.venv')
    if not os.path.exists(venv_dir):
        os.makedirs(venv_dir)
        package_dir = os.path.join(venv_dir, r'packages')
        os.makedirs(package_dir)
        bin_dir = os.path.join(venv_dir, r'bin')
        os.makedirs(bin_dir)
        now = datetime.now()
        curr_time = now.strftime("%Y-%m-%d %H:%M:%S")
        time_data = {
            'created_at': curr_time
        }
        with open(".venv/metadata.json", "w", encoding="utf-8") as file:
            json.dump(time_data, file, indent=4)

    else:
        print("A virtual environment (.venv) already exists")
        return 0
    return 1


def activate_env():
    pass

def deactivate_env():
    pass

def delete_env():
    pass

def main():
    create_env()

if __name__=='__main__':
    main()
