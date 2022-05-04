#Python GUI with Tkinter
# import tkinter as tk
# root = tk.Tk()
# root.title("Medium Article")
# # Button
# btn = tk.Button(root, text="Click Me!", command=lambda: print("Welcome Pythoneer!"))
# btn.pack()
# # Entry
# entry = tk.Entry(root)
# entry.pack()
# # Label
# label = tk.Label(root, text="Medium")
# label.pack()
# # Text
# text = tk.Text(root, height=2, width=30)
# text.pack()
# # Listbox
# listbox = tk.Listbox(root, height=2, width=30)
# listbox.pack()
# # Scrollbar
# scrollbar = tk.Scrollbar(root)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# # messagebox
# tk.messagebox.showinfo("Title", "Your Message")
# # Radio Button
# var = tk.IntVar()
# radio = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
# radio.pack()
# radio = tk.Radiobutton(root, text="Option 2", variable=var, value=2)
# radio.pack()
# # Check Button
# var = tk.IntVar()
# check = tk.Checkbutton(root, text="Option 1", variable=var)
# check.pack()
# check = tk.Checkbutton(root, text="Option 2", variable=var)
# check.pack()
# # Dropdown
# var = tk.StringVar()
# dropdown = tk.OptionMenu(root, var, "Option 1", "Option 2", "Option 3")
# dropdown.pack()
# # Status Bar
# status = tk.Label(root, text="Preparing to do Something...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
# status.pack(side=tk.BOTTOM, fill=tk.X)
# # File Input
# def open_file():
#     file = tk.filedialog.askopenfile(parent=root, mode='rb', title='Select a file')
#     if file != None:
#         contents = file.read()
#         file.close()
#         text.insert(tk.END, contents)
# # Folder Input
# def folder():
#     folder = tk.filedialog.askdirectory(parent=root, title='Select a folder')
#     label.config(text=folder)
# root.mainloop()



from tkinter import *
root = Tk()
label1 = Label(root,text="This is a tutorial about Python Tkinter")
label1.pack(side=TOP,expand=True)
label2 = Label(root,text="Do you wish to learn?",fg="blue")
label2.pack(side=TOP,expand=True)
button1 = Button(root, text="Accept", fg="green",command=root.destroy)
button1.pack(side=LEFT,expand=True)
button2 = Button(root, text="Close", fg="red",command=root.destroy)
button2.pack(side=RIGHT,expand=True)
root.mainloop()