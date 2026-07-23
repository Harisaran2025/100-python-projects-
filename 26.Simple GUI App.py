import tkinter as tk
#create the main window
root=tk.Tk()
root.title("Simple Gui App")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

title=tk.Label(root,text="Welcome to my Gui App",font=("Arial",18),bg="#f0f0f0")
title.pack(pady=20)

name_Label=tk.Label(root,text="Enter Your Name: ",font=("Arial",12),bg="#f0f0f0")
name_Label.pack

name_entry=tk.Entry(root,font=("Arial",12),width=30)
def greet_user():
    name=name_entry.get()
    if name:
        greeting_label.config(text=f"Hello ,{name}",fg="green")
    else:
        greeting_label.config(text="Please enter your name!: ",fg="red")

def reset():
    name_entry.delete(0,tk.END)
    greeting_label.config(text="")

greet_button=tk.Button(root,text="Greet Me",command=greet_user,font=("Arial",12),bg="#4CAF50",fg="white")
greet_button.pack(pady=5)

reset_button=tk.Button(root,text="Reset",command=reset,font=("Arial",12),bg="#f44336",fg="white")
reset_button.pack(pady=5)

greeting_label=tk.Label(root,text="",font=("Arial",14),bg="#f0f0f0")
greeting_label.pack(pady=20)

root.mainloop()
