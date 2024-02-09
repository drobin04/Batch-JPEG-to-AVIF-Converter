# This is the script for tkinter GUI Converter

import time
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

# pip install pillow-avif-plugin
from PIL import Image
import pillow_avif
import os
import sys


def select_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, directory)

def convert():
    directory = directory_entry.get()
    convertjpegsfromdirectory(directory)

# Define a function to get a list of all files in a directory (recursively), excluding video files
def get_all_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.jpg','.jpeg','.JPG','.JPEG')):
                filepath = os.path.join(root, filename)
                all_files.append(filepath)
                
    return all_files

def append_text(text):
    output_text.insert(tk.END, text + '\n')
    output_text.see(tk.END)

def convertjpegsfromdirectory(directoryvalue):
    print(directoryvalue)
    append_text('About to convert jpegs in directory: ' + directoryvalue)
    print('About to convert jpegs in directory: ' + directoryvalue)
    files = get_all_files(directoryvalue) # Gets all files of a specific type inside the given folder
    for file in files:
        avif_file = file + '.AVIF'
        if os.path.exists(avif_file):
            #now remove original file since we're done
            if skip_deletion.get() == 0:  # Check the state of the checkbox
                os.remove(file)  # Delete the old file
            continue  # skip if .AVIF version already exists
        try:
            JPGimg = Image.open(file)
            append_text('processing: ' + file)
            window.update()
            time.sleep(0.1)  # Introduce a small delay to allow GUI updates
            print('processing: ' + file)
            JPGimg.save(avif_file, 'AVIF')
            if os.path.exists(avif_file):
                #now remove original file since we're done
                if skip_deletion.get() == 0:  # Check the state of the checkbox
                    os.remove(file)  # Delete the old file
                #append_text('AVIF file already exists for file ' + avif_file)
        except Exception as e:
            append_text(f"Error converting {file} to .AVIF, filename: {avif_file} Error: {e}")
        
    append_text("Operation completed...")
    print("Operation completed...")


window = tk.Tk()
window.title("Directory Converter")

directory_label = tk.Label(window, text="Directory:")
directory_label.pack()

directory_entry = tk.Entry(window)
directory_entry.pack()

select_button = tk.Button(window, text="Select Directory", command=select_directory)
select_button.pack()

convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack()

# Add the checkbox widget
skip_deletion = tk.IntVar()
skip_deletion_checkbox = tk.Checkbutton(window, text='Skip Deletion Of Old JPG Files', variable=skip_deletion)
skip_deletion_checkbox.pack()

output_text = scrolledtext.ScrolledText(window)
output_text.pack()

window.mainloop()

