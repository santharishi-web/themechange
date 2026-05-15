from tkinter import*
from PIL import Image,ImageTk

root=Tk()
root.title("Theme Changer")

mode=StringVar()
mode.set("light")

def change_theme():
    if mode.get()=="dark":
       root.config(bg="black")
       label.config(bg="black",fg="white")
    else:
       root.config(bg="white")
       label.config(fg="black",bg="white")

label=Label(root,text="tkinter theme changer",font=("Arial",20,"bold"))
label.pack(pady=30)

Radiobutton(root ,text="Light Mode",variable=mode,value="light" ,command=change_theme ,font=("Arial",12 ,"italic")).pack(pady=5)
Radiobutton(root ,text="Dark Mode",variable=mode,value="dark" ,command=change_theme,font=("Arial",12)).pack(pady=5)

root.mainloop()