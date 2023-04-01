import tkinter as tk
import os
from PIL import Image, ImageTk
#path variables
# Get the current working directory
cwd = os.getcwd()
# Construct the path to the images directory
images_dir = os.path.join(cwd, 'images')
# Access an image file within the images directory
grey_tick = os.path.join(images_dir, 'grey_tick.png')
green_tick = os.path.join(images_dir, 'green_tick.png')
# Function to execute part1.py
def execute_part1():
    os.system('python part1.py')
    tick_img = Image.open(green_tick).resize((50,50))
    tick_icon = ImageTk.PhotoImage(tick_img)
    tick_label1.config(image=tick_icon)
    tick_label1.image = tick_icon

# Function to execute part2.py
def execute_part2():
    os.system('python part2.py')
    tick_img = Image.open(green_tick).resize((50,50))
    tick_icon = ImageTk.PhotoImage(tick_img)
    tick_label2.config(image=tick_icon)
    tick_label2.image = tick_icon

# Function to execute part3.py
def execute_part3():
    os.system('python part3.py')
    tick_img = Image.open(green_tick).resize((50,50))
    tick_icon = ImageTk.PhotoImage(tick_img)
    tick_label3.config(image=tick_icon)
    tick_label3.image = tick_icon

# Create the main window
root = tk.Tk()
root.geometry('200x250')

# Create the buttons and icons
button1 = tk.Button(root, text='PART 1', command=execute_part1)
button2 = tk.Button(root, text='PART 2', command=execute_part2)
button3 = tk.Button(root, text='PART 3', command=execute_part3)

tick_img = Image.open(grey_tick).resize((50,50))
tick_icon = ImageTk.PhotoImage(tick_img)
tick_label1 = tk.Label(root, image=tick_icon)
tick_label2 = tk.Label(root, image=tick_icon)
tick_label3 = tk.Label(root, image=tick_icon)

# Add the buttons and icons to the window using grid layout
button1.grid(row=0, column=0, padx=10, pady=10)
tick_label1.grid(row=0, column=1, padx=10, pady=10)
button2.grid(row=1, column=0, padx=10, pady=10)
tick_label2.grid(row=1, column=1, padx=10, pady=10)
button3.grid(row=2, column=0, padx=10, pady=10)
tick_label3.grid(row=2, column=1, padx=10, pady=10)

# Center the column of widgets
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start the GUI event loop
root.mainloop()
