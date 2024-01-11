# pip install pillow-avif-plugin
from PIL import Image
import pillow_avif
import os
import sys
import time

selected_item = "C:\\Users\\Douglas\\Pictures\\test"
print(selected_item)
input('About to convert jpegs in directory: ' + selected_item + 'Press any continue...')

directories = [selected_item]

# Define a function to get a list of all files in a directory (recursively), excluding video files
def get_all_files(directory):
    print("About to check files in directory: " + directory)
    all_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            print("get_all_files: " + filename)
            if filename.endswith(('.jpg','.jpeg','.JPG','.JPEG')):
                filepath = os.path.join(root, filename)
                all_files.append(filepath)
                
    return all_files


# Loop over the directories and process each file
for directory in directories:
    print("Beginning work on directory: " + directory)
    # Loop over the directories and process each file
    files = get_all_files(directory) # Gets all files of a specific type
    for file in files:
        print("About to start work on file: " + file)
        start_time = time.time()
        avif_file = file + '.AVIF'
        if os.path.exists(avif_file):
            #now remove original file since we're done
            print("Existing AVIF already found, skipping - this file exists: " + avif_file)
            os.remove(file)
            continue  # skip if .AVIF version already exists

        try:
            JPGimg = Image.open(file)
            
            JPGimg.save(avif_file, 'AVIF')
            endtime = time.time()

            print(file + " completed. Time: " + str(endtime - start_time) + " Seconds.")

            if os.path.exists(avif_file):
                #now remove original file since we're done
                os.remove(file)
        except Exception as e:
            print(f"Error converting {file} to .AVIF, filename: {avif_file} Error: {e}")

input("Operation completed. Press any key to close...")