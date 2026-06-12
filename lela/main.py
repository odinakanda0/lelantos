import os
import sys
import json
import subprocess
from datetime import datetime

def create_env(env_name=""):
    if env_name == "":
        env_name = '.venv'
    curr_dir = os.getcwd()
    venv_dir = os.path.join(curr_dir, rf'{env_name}')
    if not os.path.exists(venv_dir):
        os.makedirs(venv_dir)
        package_dir = os.path.join(venv_dir, r'packages')
        os.makedirs(package_dir)
        bin_dir = os.path.join(venv_dir, r'bin')
        os.makedirs(bin_dir)
        python_version=sys.version.split(' ')[0]
        python_path_components=sys.executable.split('/')
        python_home="/".join(python_path_components[:-1])
        python_executable="/".join(python_path_components)
        version_data = {
            "python_version": python_version
        }
        create_symlink = subprocess.run(["ln", "-s", f"{python_executable}", f"{bin_dir}"], capture_output=True, text=True)
        print(create_symlink.stdout.strip())
        
        with open(os.path.join(venv_dir, "pyvenv.cfg"), "w") as file:
            file.write(f"home = {python_home}\n")
            file.write(f"version = {python_version}\n")
            file.write(f"executable = {python_executable}\n")
            file.write("include-system-site-packages = false\n")

        with open(os.path.join(venv_dir, "metadata.json"), "w", encoding="utf-8") as file:
            json.dump(version_data, file, indent=4)

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
