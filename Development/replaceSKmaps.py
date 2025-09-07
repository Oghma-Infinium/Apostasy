import shutil
import os
import logging

"""
source_file: the file that should be the base to copy from, in my case it's a 16x16 blank sk map
target_root: the parent folder/directory that you want to find all subsurface maps from (*_sk.dds)
output_root: the folder where the new files will be output (all files will be a copy of source_file with the paths maintained)
log_path: log will list which files were edited

dry_run: When set to True, will only produce a log to tell you which files will be changed.
         When set to False, will actually run the script in its entirety

"""
source_file = r"F:\__testingscripts\sk_replacement.dds"

target_root = r"F:\ApostasyRE\mods"

output_root = r"F:\__testingscripts\_output"

log_path = r"F:\__testingscripts\_logs\replaceSKmaps.log.txt"

dry_run = True

# main function

def replace_all_sk_files(src_file, target_root, output_root, log_file=None, dry_run=False):
    if not dry_run:
        os.makedirs(output_root, exist_ok=True)
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    handlers = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file, mode="w", encoding="utf-8"))

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=handlers
    )

    replaced_count = 0

    for dirpath, _, filenames in os.walk(target_root):
        for filename in filenames:
            if filename.endswith("_sk.dds"):

                rel_path = os.path.relpath(os.path.join(dirpath, filename), target_root)

                dest_file = os.path.join(output_root, rel_path)

                if dry_run:
                    logging.info(f"[DRY RUN] Would create: {dest_file}")
                else:
                    os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                    shutil.copy2(src_file, dest_file)
                    logging.info(f"Created: {dest_file}")

                replaced_count += 1

    logging.info(f"Total files {'found' if dry_run else 'created'}: {replaced_count}")

replace_all_sk_files(source_file, target_root, output_root, log_file=log_path, dry_run=dry_run)
