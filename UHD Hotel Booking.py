import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#setting up window 
root.geometry("500x500") 
root.title("Uhd Hotel Booking")

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='Homepage')
notebook.add(frame2, text='Avaliavle Hotels')


#label example
#label = tk.Label (root, text="Choose a hotel", font=('Arial', 18))
#label.pack(padx=20, pady=20)

#if you want to add a textbox to type in comments 
#textbox = tk.Text(root, height=3, font=('Arial', 12))
#textbox.pack()

root.mainloop()
