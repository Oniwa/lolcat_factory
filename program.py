import os  # TODO: Switch to pathlib for path stuff and things
import platform
import subprocess

import cat_service


def main():
    print_header()

    folder = get_or_create_output_folder()
    print(f'Found or created {folder}')
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('------------------------------')
    print('        LOLCat Factory')
    print('------------------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory at {full_path}')
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = f'lolcat_{i}'
        print(f'Downloading cat {name}')
        cat_service.get_cat(folder, name)

    print('Done')


def display_cats(folder):
    print('Displaying cats in OS window.')
    operating_system = platform.system()
    if operating_system == 'Darwin':
        subprocess.call(['open', folder])
    elif operating_system == 'Windows':
        folder = os.path.abspath(folder)
        subprocess.call(['explorer', folder])
    elif operating_system == 'Linux':
        subprocess.call(['xgd-open', folder])
    else:
        print(f"We don't support your os: {operating_system}")


if __name__ == '__main__':
    main()
