import os
import shutil

# Define the directory to organize
directory = r'D:\Users\RYZEN 3 3200G\Downloads'

# Define the file type categories and their corresponding extensions
file_type = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

# Create subdirectories for each file type
for folder in file_type.keys():
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to their respective subdirectories
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()

        for folder, extensions in file_type.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                break

