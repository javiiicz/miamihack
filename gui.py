import tkinter as tk
from PIL import Image, ImageTk
from openai_script import main

def on_button_click():
    main()

# Create the main window
root = tk.Tk()

# Set the title
root.title("Math Visualizer")

root.geometry("1280x720")

frame = tk.Frame(root)
frame.pack(expand=True)

title_label = tk.Label(frame, text="Math Visualizer", font=("Cal Sans", 60))
title_label.pack(side="left")

image = Image.open("logo.jpeg")
w, h = image.size
new_width = 300
aspect_ratio = h / w
new_height = int(new_width * aspect_ratio)
image = image.resize((new_width, new_height))
logo = ImageTk.PhotoImage(image)
image_label = tk.Label(frame, image=logo, width=300, height=new_height)
image_label.pack(side="left", padx=15)

button = tk.Button(root, text="Start", height=5, width=10, font=("Cal Sans", 15), command=on_button_click)
button.pack(side="top",pady=(0,150),)

# Run the application
root.mainloop()
