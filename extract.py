import os
import time
from datetime import datetime
import shutil

def extract_jpeg_files(directory, start_time, end_time):
    start_timestamp = time.mktime(start_time.timetuple())
    end_timestamp = time.mktime(end_time.timetuple())

    jpeg_files = []

    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            file_path = os.path.join(directory, filename)
            modified_time = os.path.getmtime(file_path)

            if start_timestamp <= modified_time <= end_timestamp:
                jpeg_files.append(file_path)

    return jpeg_files

def copy_extracted_files(file_paths, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for path in file_paths:
        shutil.copy(path, output_directory)

    print(f"Copied {len(file_paths)} files to {output_directory}")

if __name__ == "__main__":
    directory_path = r'PATH'
    start_date = datetime(2024, 10, 1)
    end_date = datetime(2024, 10, 9)

    jpeg_files = extract_jpeg_files(directory_path, start_date, end_date)
    print("JPEG files modified within the specified time period:")

    for jpeg_file in jpeg_files:
        print(jpeg_file)

    current_timestamp = int(time.time())
    output_directory = f'extraction_{current_timestamp}'
    copy_extracted_files(jpeg_files, output_directory)
