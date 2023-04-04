import shutil
import os

# Get the path of the temp directory
temp_dir = os.environ["temp"]

# Delete the contents of the temp directory
for file in os.listdir(temp_dir):
    file_path = os.path.join(temp_dir, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(e)
