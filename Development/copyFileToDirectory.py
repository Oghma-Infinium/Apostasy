import shutil
import os

def copy_file_to_paths(src_file, dest_paths):
    for dest in dest_paths:
        os.makedirs(os.path.dirname(dest), exist_ok=True)

        shutil.copy2(src_file, dest)
        print(f"Copied {src_file} to {dest}")

source_file = r"F:\__testingscripts\sk_replacement.dds"
destination_paths = [
    r"F:\stuff\___work\_copy Test\textures\actors\AoM\dog\wolfwhite_sk.dds",
    # input any other files you want to replace.
    # Make sure they are comma separated.
    ]

copy_file_to_paths(source_file, destination_paths)
