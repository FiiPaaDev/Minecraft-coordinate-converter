import tkinter
from tkinter import ttk
from tkinter import *
import pyperclip
import plyer

#generate window
window = tkinter.Tk()
window.title("Minecraft Portal Teleportation System")

#generate frame
frame = tkinter.Frame(window)
frame.pack()

#/////////////////////////////////////////////////////////////////////////


overworld_frame = tkinter.LabelFrame(frame, text="Overworld Coordinate")
overworld_frame.grid(row=0, column=0, padx=10, pady=10)

overworld_x_label = tkinter.Label(overworld_frame, text="X coordinate")
overworld_x_label.grid(row=0, column=0)
overworld_z_label = tkinter.Label(overworld_frame, text="Z coordinate")
overworld_z_label.grid(row=0, column=1)

overworld_x_entry = tkinter.Entry(overworld_frame)
overworld_x_entry.grid(row=1, column=0)
overworld_y_entry = tkinter.Entry(overworld_frame)
overworld_y_entry.grid(row=1, column=1)

for widget in overworld_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

#/////////////////////////////////////////////////////////////////////////

def button_event():
    try:
        x_get = int(overworld_x_entry.get())
        y_get = int(overworld_y_entry.get())
        nether_x_entry.delete(0, tkinter.END)
        nether_y_entry.delete(0, tkinter.END)

        #///////////////////////////////////////////

        nether_x_entry_processed = round(x_get / 8)
        nether_y_entry_processed = round(y_get / 8)

        #///////////////////////////////////////////

        nether_x_entry.insert(0, nether_x_entry_processed)
        nether_y_entry.insert(0, nether_y_entry_processed)
    
    except Exception:
        return None
    
def paste_button():
    paste_content = pyperclip.paste()

    if "/tp" in paste_content:
        coordinate = paste_content
        numbers_str = coordinate.split()[1:]

        numbers = [num for num in numbers_str]

        x_data = int(numbers[0])
        z_data = int(numbers[2])

        overworld_x_entry.delete(0, tkinter.END)
        overworld_y_entry.delete(0, tkinter.END)
        overworld_x_entry.insert(0, x_data)
        overworld_y_entry.insert(0, z_data)
    else:
        overworld_x_entry.delete(0, tkinter.END)
        overworld_y_entry.delete(0, tkinter.END)
        plyer.notification.notify(
            title="Notification Title",
            message="The clipboard you pasting does not contain '/tp' !",
            timeout=5
        )

def delete_button():
    overworld_x_entry.delete(0, tkinter.END)
    overworld_y_entry.delete(0, tkinter.END)
    nether_x_entry.delete(0, tkinter.END)
    nether_y_entry.delete(0, tkinter.END)

button2 = tkinter.Button(frame, text="Paste", command=paste_button)
button2.grid(row=1, column=0, sticky="we", padx=10, pady=2)
button2.config(bg="light green")

button = tkinter.Button(frame, text="Convert", command=button_event)
button.grid(row=2, column=0, sticky="we", padx=10, pady=2)
button.config(bg="light blue")

button3 = tkinter.Button(frame, text="Delete", command=delete_button)
button3.grid(row=3, column=0, sticky="we", padx=10, pady=2)
button3.config(bg="orange")

#/////////////////////////////////////////////////////////////////////////

nether_frame = tkinter.LabelFrame(frame, text="Netherworld Coordinate")
nether_frame.grid(row=4, column=0, padx=10, pady=10)

nether_x_label = tkinter.Label(nether_frame, text="X coordinate")
nether_x_label.grid(row=0, column=0)
nether_y_label = tkinter.Label(nether_frame, text="Y coordinate")
nether_y_label.grid(row=0, column=1)

nether_x_entry = tkinter.Entry(nether_frame)
nether_x_entry.grid(row=1, column=0)
nether_y_entry = tkinter.Entry(nether_frame)
nether_y_entry.grid(row=1, column=1)

for widget in nether_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

window.mainloop()
