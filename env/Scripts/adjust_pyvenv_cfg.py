import os
import sys

def adjust_pyvenv_cfg():
    # Get the path of the virtual environment directory (parent directory of this script)
    venv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Define the path to the pyvenv.cfg file
    cfg_file = os.path.join(venv_path, 'pyvenv.cfg')

    new_home = os.path.join(venv_path, 'Scripts')

    # Read the current pyvenv.cfg contents
    with open(cfg_file, 'r') as file:
        lines = file.readlines()

    # Modify the 'home' line
    with open(cfg_file, 'w') as file:
        for line in lines:
            if line.startswith('home ='):
                file.write(f'home = {new_home}\n')
            else:
                file.write(line)

    print(f"Updated {cfg_file} with home = {new_home}")

if __name__ == '__main__':
    adjust_pyvenv_cfg()
