import os
import glob
import zipfile

def rename_and_extract_zip(zip_filename):
    # Remove file extension to get the zip name
    zip_name = os.path.splitext(zip_filename)[0]

    # Open the zip file
    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        # Loop through each file in the zip file
        for file_info in zip_file.infolist():
            # Check if the file has a .py extension
            if file_info.filename.endswith('.py'):
                # Rename the .py file using the zip name
                new_filename = f"{zip_name}_{os.path.basename(file_info.filename)}"
                file_info.filename = new_filename

            # Extract the file to the same directory as the zip file
            zip_file.extract(file_info, path=os.path.dirname(zip_filename))

def process_all_zip_files_in_directory(directory):
    # Find all zip files in the directory
    zip_files = glob.glob(os.path.join(directory, '*.zip'))

    # Process each zip file
    for zip_filename in zip_files:
        print(f"Processing {zip_filename}...")
        rename_and_extract_zip(zip_filename)

if __name__ == "__main__":
    directory = input("Enter the directory path containing zip files: ")
    process_all_zip_files_in_directory(directory)
