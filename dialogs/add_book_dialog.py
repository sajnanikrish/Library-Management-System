from tkinter import *
import database
from tkinter import messagebox
import re

class AddBookDialog: 
    def __init__(self, admin):
        self.admin = admin
        self.parent = admin.window
        self.add_books()

    def add_books(self):

        self.dialog = Toplevel(self.parent)
        self.dialog.geometry('428x400')
        self.admin._center_dialog(self.dialog)
        self.dialog.title('Add New Book')
        self.dialog.config(bg='#f7e1d7')
        self.dialog.transient(self.parent)         # keeps the dialogbox a child of root window, if root is minimized then self.dialog also minmizes
        self.dialog.grab_set()         # makes the root window un-interactive, only current active


        book_label = Label  (self.dialog, text='Add New Book', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
        book_label.grid(row=0, column=0, pady=12)

        title_label = Label (self.dialog, text='Title : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        title_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

        self.title_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
        self.title_entry.grid(row=2, column=0, padx=13, pady=1, sticky='w') 
        self.admin.add_placeholder(self.title_entry, 'Enter Book Title')
        # admin_gui.Start_app.add_placeholder(self.dialog, self.title_entry, 'Enter Book Title') 

        author_label = Label(self.dialog, text='Author : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        author_label.grid(row=3, column=0, padx=10, pady=12, sticky='w')

        self.author_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
        self.author_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w')
        self.admin.add_placeholder(self.author_entry, 'Enter Author Name')
        # admin_gui.Start_app.add_placeholder(self.dialog, self.author_entry, 'Enter Author Name')

        quant_label = Label(self.dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        quant_label.grid(row=5, column=0, padx=10, pady=12, sticky='w')

        self.quant_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
        self.quant_entry.grid(row=6, column=0, padx=13, pady=1, sticky='w')
        self.admin.add_placeholder(self.quant_entry, 'Enter Book Quantity')


        
        def save():
            title = self.title_entry.get().strip()
            author = self.author_entry.get().strip()
            quant_str = self.quant_entry.get().strip()

            if title == 'Enter Book Title' or author == 'Enter Author Name' or quant_str == 'Enter Book Quantity' or not title or not author or not quant_str:
                messagebox.showerror('Error', 'All details are required!')
                return
            title_pattern = r"^[A-Za-z0-9\s\.\,\:\-\'\(\)]{2,}$"
            if not re.match(title_pattern, title):
                messagebox.showerror(
                    'Error',
                    'Invalid Book Title!\nOnly letters, numbers and . , : - \' ( ) allowed.'
                )
                return 

            # 🔹 Author Validation
            author_pattern = r"^[A-Za-z\s\.\-']{2,}$"
            if not re.match(author_pattern, author):
                messagebox.showerror(
                    'Error',
                    'Invalid Author Name!\nOnly letters, spaces, . - \' allowed.'
                )
                return

            # 🔹 Quantity Validation
            if not quant_str.isdigit() or int(quant_str) <= 0:
                messagebox.showerror('Error', 'Quantity must be a positive number!')
                return

            quant = int(quant_str)
            database.add_book(title,author,quant)
            self.admin.refresh_books_tree()
            self.dialog.destroy()

            messagebox.showinfo('Success','Book Added Successfully!')


        add_btn = Button(self.dialog, text='Add Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10,  activebackground='#669bbc',command=save)
        add_btn.grid(row=7, column=0,pady=25)
