import database
import student_login
import admin_login
from tkinter import *


def open_admin(): 
    admin_login.Admin_Login(root)

def open_student():
    student_login.Student_Login(root)

root = Tk()
root.title('Library Management System')
root.maxsize(350,200)
root.minsize(350,200)
root.config(bg='#E4D6C3')

root.update_idletasks()

width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
geom = '350x200'

root.geometry(f"{width}x{height}+{x}+{y}")


# database.generate_qr_for_existing_books()

database.create_tables()
label_1 = Label(root, text='Select Your Role', bg='#E4D6C3', fg='#1B263B', font=('Arial', 20, 'bold'))
label_1.grid(row=0, column=0, padx=60, pady=30, columnspan=3)

btn_1 = Button(root, text='Admin', bg='#1B263B', fg="#E4D6C3", font=('Arial', 16, 'bold'), padx=8,pady=8, activebackground='#669bbc' ,command=open_admin)
btn_1.grid(row=1, column=0, pady=18)

btn_2 = Button(root, text='Student', bg='#1B263B', fg='#E4D6C3', font=('Arial', 16, 'bold'), padx=8,pady=8, activebackground='#669bbc', command=open_student)
btn_2.grid(row=1, column=2, pady=18)

def on_root_close():
    root.destroy()
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_root_close)

root.mainloop()

