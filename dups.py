import os
import re
from collections import defaultdict

def find_latest_duplicate_files(directory):
    file_versions = defaultdict(list)

    # Scan the directory for duplicate files
    for filename in os.listdir(directory):
        # Extract the base name, version, and extension of the file
        match = re.match(r'^(.+?)(?:\((\d+)\))?(\..+)$', filename)
        if match:
            base_name, version, extension = match.groups()
            if version is None:
                version = 0
            else:
                version = int(version)
            file_versions[(base_name, extension)].append((version, filename))

    # Determine the latest version of each file
    latest_files = {}
    for (base_name, extension), versions in file_versions.items():
        latest_version, latest_file = max(versions)
        latest_files[(base_name, extension)] = latest_file

    return latest_files

def remove_older_duplicate_files(directory, latest_files):
    for filename in os.listdir(directory):
        match = re.match(r'^(.+?)(?:\((\d+)\))?(\..+)$', filename)
        if match:
            base_name, version, extension = match.groups()
            latest_file = latest_files.get((base_name, extension))
            if latest_file is not None and latest_file != filename:
                os.remove(os.path.join(directory, filename))
                print(f"Deleted {filename}")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    latest_files = find_latest_duplicate_files(directory)
    remove_older_duplicate_files(directory, latest_files)
