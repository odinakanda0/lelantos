import os
from datetime import datetime
import json

def create_env(env_name=""):
    if env_name == "":
        env_name = '.venv'
    curr_dir = os.getcwd()
    venv_dir = os.path.join(curr_dir, r'.venv')
    if not os.path.exists(venv_dir):
        os.makedirs(venv_dir)
        package_dir = os.path.join(venv_dir, r'packages')
        os.makedirs(package_dir)
        now = datetime.now()
        curr_time = now.strftime("%Y-%m-%d %H:%M:%S")
        time_data = {
            'created_at': curr_time
        }
        with open(".venv/meta.json", "w", encoding="utf-8") as file:
            json.dump(time_data, file, indent=4)

    else:
        print("A virtual environment (.venv) already exists")
        return 0
    return 1


def main():
    create_env()

if __name__=='__main__':
    main()
