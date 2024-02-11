# This is the script for tkinter GUI Converter

import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import scrolledtext

# pip install pillow-avif-plugin
from PIL import Image
import pillow_avif
import os
import sys

def guiprint(text):
    append_text(text)
    print(text)

def select_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, directory)

def convert():
    directory = directory_entry.get()
    convertjpegsfromdirectory(directory)

def scanonly():
    directory = directory_entry.get()
    scanonly_jpegsfromdirectory(directory)

# Define a function to get a list of all files in a directory (recursively), excluding video files
def get_all_files(directory):
    all_files = []
    for window, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.jpg','.jpeg','.JPG','.JPEG')):
                filepath = os.path.join(window, filename)
                all_files.append(filepath)
                
    return all_files

def append_text(text):
    output_text.insert(tk.END, text + '\n')
    output_text.see(tk.END)

def convertjpegsfromdirectory(directoryvalue):
    guiprint('About to convert jpegs in directory: ' + directoryvalue)
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
                #guiprint('AVIF file already exists for file ' + avif_file)
        except Exception as e:
            guiprint(f"Error converting {file} to .AVIF, filename: {avif_file} Error: {e}")
        
    guiprint("Operation completed...")

def scanonly_jpegsfromdirectory(directoryvalue):
    guiprint('About to scan for convertible jpegs in directory: ' + directoryvalue)
    files = get_all_files(directoryvalue) # Gets all files of a specific type inside the given folder
    for file in files:
        avif_file = file + '.AVIF'
        if os.path.exists(avif_file):
            #now remove original file since we're done
            if skip_deletion.get() == 0:  # Check the state of the checkbox
                #os.remove(file)  # Delete the old file
                guiprint("Existing AVIF found for " + file + ", would have deleted original JPEG")
            continue  # skip if .AVIF version already exists
        try:
            guiprint('Scan Found: ' + file)
            window.update()
            time.sleep(0.1)  # Introduce a small delay to allow GUI updates
        except Exception as e:
            guiprint(f"Error converting {file} to .AVIF, filename: {avif_file} Error: {e}")
        
    guiprint("Operation completed...")

window = tk.Tk()

#setting title
window.title("Batch JPEG To AVIF Converter")
#setting window size
width=580
height=228
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)
window.resizable(width=False, height=False)

GLabel_383=tk.Label(window)
ft = tkFont.Font(family='Times',size=10)
GLabel_383["font"] = ft
GLabel_383["fg"] = "#333333"
GLabel_383["justify"] = "center"
GLabel_383["text"] = "Directory:"
GLabel_383.place(x=10,y=20,width=70,height=25)

directory_entry=tk.Entry(window)
directory_entry["borderwidth"] = "1px"
directory_entry.place(x=80,y=20,width=380,height=31)

GButton_151=tk.Button(window)
GButton_151["bg"] = "#e9e9ed"
ft = tkFont.Font(family='Times',size=10)
GButton_151["font"] = ft
GButton_151["fg"] = "#000000"
GButton_151["justify"] = "center"
GButton_151["text"] = "Select Directory"
GButton_151.place(x=465,y=20,width=103,height=31)
GButton_151["command"] = select_directory

skip_deletion = tk.IntVar()
skip_deletion_checkbox=tk.Checkbutton(window)
ft = tkFont.Font(family='Times',size=10)
skip_deletion_checkbox["font"] = ft
skip_deletion_checkbox["fg"] = "#333333"
skip_deletion_checkbox["justify"] = "center"
skip_deletion_checkbox["text"] = "Skip Deletion of Old JPEG Files"
skip_deletion_checkbox.place(x=20,y=60,width=203,height=43)
skip_deletion_checkbox["offvalue"] = "0"
skip_deletion_checkbox["onvalue"] = "1"
skip_deletion_checkbox["variable"] = skip_deletion

output_text=scrolledtext.ScrolledText(window)
output_text["borderwidth"] = "1px"
output_text.place(x=10,y=110,width=559,height=99)

scan_only=tk.Button(window)
scan_only["bg"] = "#e9e9ed"
ft = tkFont.Font(family='Times',size=10)
scan_only["font"] = ft
scan_only["fg"] = "#000000"
scan_only["justify"] = "center"
scan_only["text"] = "Scan Only"
scan_only.place(x=310,y=60,width=124,height=40)
scan_only["command"] = scanonly

convert_button=tk.Button(window)
convert_button["bg"] = "#e9e9ed"
ft = tkFont.Font(family='Times',size=10)
convert_button["font"] = ft
convert_button["fg"] = "#000000"
convert_button["justify"] = "center"
convert_button["text"] = "Convert All"
convert_button.place(x=440,y=60,width=126,height=41)
convert_button["command"] = convert


window.mainloop()

