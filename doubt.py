# book_id = input('Enter book id : ')
# title = input('Enter book title : ')
# author = input('Enter author name : ')
# quant = int(input('Enter number of books : '))

# book_data = {}

# book_data[book_id] = {
#     'Title' : title,
#     'Author' : author,
#     'Quantity' : quant
# }


# book_data[book_id]['Quantity'] = quant+20
# print(book_data)

# print('Hello World  \n How are you?')





# from tkinter import *
# from tkinter import ttk
# import random

# # ---------------- Main Window ----------------
# root = Tk()
# root.title("Treeview Scrollbar Test")
# root.geometry("900x500")
# root.config(bg="#E4D6C3")

# # ---------------- Container Frame ----------------
# container = Frame(root, bg="#E4D6C3")
# container.pack(fill="both", expand=True, padx=20, pady=20)

# # ---------------- Treeview Frame ----------------
# tree_frame = Frame(container, bg="#E4D6C3")
# tree_frame.pack(fill="both", expand=True)

# # ---------------- Scrollbars ----------------
# y_scroll = Scrollbar(tree_frame, orient="vertical")
# x_scroll = Scrollbar(tree_frame, orient="horizontal")

# # ---------------- Treeview ----------------
# tree = ttk.Treeview(
#     tree_frame,
#     columns=("id", "title", "author", "year", "qty"),
#     show="headings",
#     yscrollcommand=y_scroll.set,
#     xscrollcommand=x_scroll.set
# )

# # Connect scrollbars
# y_scroll.config(command=tree.yview)
# x_scroll.config(command=tree.xview)

# # ---------------- Pack ----------------
# y_scroll.pack(side="right", fill="y")
# x_scroll.pack(side="bottom", fill="x")
# tree.pack(side="left", fill="both", expand=True)

# # ---------------- Headings ----------------
# tree.heading("id", text="ID")
# tree.heading("title", text="Book Title")
# tree.heading("author", text="Author")
# tree.heading("year", text="Year")
# tree.heading("qty", text="Quantity")

# # ---------------- Column widths ----------------
# tree.column("id", width=60, anchor="center")
# tree.column("title", width=250)
# tree.column("author", width=200)
# tree.column("year", width=80, anchor="center")
# tree.column("qty", width=80, anchor="center")

# # ---------------- Random Dummy Data ----------------
# titles = [
#     "Python Basics", "Data Structures", "Machine Learning",
#     "Digital Electronics", "Control Systems", "AI Fundamentals",
#     "Operating Systems", "DBMS Concepts"
# ]

# authors = [
#     "John Smith", "A. Tanenbaum", "Andrew Ng",
#     "Dennis Ritchie", "Guido van Rossum"
# ]

# for i in range(1, 51):
#     tree.insert(
#         "",
#         "end",
#         values=(
#             i,
#             random.choice(titles),
#             random.choice(authors),
#             random.randint(1995, 2024),
#             random.randint(1, 20)
#         )
#     )

# # ---------------- Run ----------------
# root.mainloop()




# import database

# from tkinter import *
# from tkinter import messagebox

# def main():
#     import admin_gui
#     database.create_tables()
#     root.destroy()
#     admin_gui.start_app()
    

# root = Tk()
# root.title('Library Management System')
# root.maxsize(350,200)
# root.minsize(350,200)
# root.config(bg='#E4D6C3')

# label_1 = Label(root, text='Select Your Role', bg='#E4D6C3', fg='#1B263B', font=('Arial', 20, 'bold'))
# label_1.grid(row=0, column=0, padx=60, pady=30, columnspan=3)

# btn_1 = Button(root, text='Admin', bg='#1B263B', fg='#E4D6C3', font=('Arial', 14, 'bold'), padx=8,pady=8, command=main)
# btn_1.grid(row=1, column=0, pady=18)

# btn_2 = Button(root, text='Student', bg='#1B263B', fg='#E4D6C3', font=('Arial', 15, 'bold'), padx=8,pady=8)
# btn_2.grid(row=1, column=2, pady=18)


# root.mainloop()



# import hashlib

# def check(password):
#     org_password = 'Krish@123'
#     org_hash_password = hashlib.sha256(org_password.encode()).digest()
#     hash_pass = hashlib.sha256(password.encode()).digest()

#     if org_hash_password == hash_pass:
#         return True
#     else:
#         return False

# password = input('Enter Password : ')

# print(check(password))


# import qrcode

# data = "Hello Krish!"

# img = qrcode.make(data)
# img.save("my_qr.png")


# import qrcode
# import os

# # Make sure folder exists
# if not os.path.exists("qrcodes"):
#     os.makedirs("qrcodes")

# book_id = "BOOK_101"
# qr = qrcode.make(book_id)

# file_path = os.path.join("qrcodes", f"{book_id}.png")
# qr.save(file_path)

# print("QR saved at:", file_path)

# from tkinter import * 
# from tkinter import font
# import student_gui


# class Student_Login:
#     def __init__(self, parent):
#         self.parent = parent
#         self.parent.withdraw()

#         self.window = Toplevel(parent)
#         self.window.title('Student Login')
#         self.window.protocol("WM_DELETE_WINDOW", self.on_close)
#         self.window.minsize(360,400)
#         self.window.maxsize(360,400)
#         self.window.config(bg= "#E4D6C3")

#         self._center_window()
#         self._set_ui()

#     def on_close(self):
#         self.window.destroy()
#         self.parent.deiconify()   # show main window again

    
#     def _center_window(self):

#         self.window.update_idletasks()
#         width = self.window.winfo_width()
#         height = self.window.winfo_height()
        
#         x = (self.window.winfo_screenwidth() // 2) - (width // 2)
#         y = (self.window.winfo_screenheight() // 2) - (height // 2)
#         self.window.geometry(f'{width}x{height}+{x}+{y}')


#     def open_signup(self):
#         print('Sign Up')

#     def open_app(self, parent):
#         student_gui.start_app(parent)

#     def _set_ui(self):

#         title_lbl = Label(self.window, text='Student Login', font=('Arial', 28, 'bold'), bg='#E4D6C3', fg='#1B263B')
#         title_lbl.grid(row=0, column=0, padx= 55, pady=15)

#         user_label = Label(self.window, text='Enter Username : ', font=('Arial', 15, 'bold'), bg='#E4D6C3', fg='#1B263B')
#         user_label.grid(row=1, column=0, padx=10,pady=18, sticky='w')

#         self.user_entry = Entry(self.window, width=55, bg= '#d5bdaf', fg='black')
#         self.user_entry.grid(row=2, column=0, sticky='w', padx=15, pady=2) 

#         pass_label = Label(self.window, text='Enter Password : ', bg='#E4D6C3', fg='#1B263B', font=('Arial', 15, 'bold'))
#         pass_label.grid(row=3, column=0, sticky='w', padx=10, pady=18)

#         self.pass_entry = Entry(self.window, width=55, bg= '#d5bdaf', fg='black')
#         self.pass_entry.grid(row=4, column=0, sticky='w', padx=15, pady=2)

#         login_btn = Button(self.window, text='Login', bg='#1B263B', fg='#E4D6C3', font=('Arial', 20, 'bold'), padx=40, activebackground='#669bbc', command= lambda: self.open_app(self.window))
#         login_btn.grid(row=5, column=0, pady=20)

#         link_font = font.Font(underline=TRUE, family='Arial', size=18, weight='bold')

#         sign_label = Button(self.window, text='Sign Up', bg='#E4D6C3', fg= '#1B263B', font=link_font, cursor='hand2', command=self.open_signup, borderwidth=0, activebackground='#E4D6C3')
#         sign_label.grid(row=6, column=0)
#         # sign_label.bind("<Button-1>", self.open_signup)



# from tkinter import *
# from tkcalendar import DateEntry
# from tkinter import ttk, messagebox
# import database

# class Start_app:

#     def __init__(self, parent):
#         self.parent = parent
#         self.parent.withdraw()

#         self.window = Toplevel(parent) 
#         self.window.title('Library Management System')
#         self.window.geometry('1500x750')
#         self.window.config(bg= "#E4D6C3")
#         self.window.protocol("WM_DELETE_WINDOW", self.on_close)
#         self.set_header()
#         self.set_containers()
#         self.tree_styling()
#         self.insert_book_data()
#         self.issued_book_data()

#     def on_close(self):
#         self.window.destroy()
#         self.parent.deiconify()   # show main window again

        
#     # Header Frame---
#     def set_header(self):
#         header_frame = Frame(self.window, bg= '#1B263B',height= 85, relief='raised', bd=2)
#         header_frame.pack(fill='x') 
#         header_frame.pack_propagate(False)

#         header = Label(header_frame, text='Library Management System', bg= '#1B263B',fg='#E4D6C3', font=('Arial', 30, 'bold'), anchor='center')
#         header.pack(pady=15)

#     # Main frame
#     def set_containers(self):

#         main_container = Frame(self.window, bg="#E4D6C3")
#         main_container.pack(fill='both', expand=True)

#         # Left frame for buttons
#         button_frame = Frame(main_container, bg= "#E4D6C3", width=220)
#         button_frame.pack(fill='y', side='left', padx= 75, pady= 25)
#         button_frame.propagate(FALSE)

#         button_header = Label(button_frame, text='Operations', font=('Arial', 22, 'bold'), bg='#E4D6C3',fg= '#1B263B')
#         button_header.pack(pady=14)


#         button_config = [
#             ("Add Book", "#6f4518", self.add_book_dialog),
#             ('Add Quantity', "#335c67", self.add_quantity_dialog),
#             ('Remove Quantity', "#800f2f", self.rmv_quantity_dialog),
#             ('Issue Book', "#3a5a40", self.issue_book_dialog),
#             ('Return Book', "#c16200", self.return_book_dialog)
#         ]


#         for i, (text, color, func) in enumerate(button_config):
#             btn = Button(button_frame, text=text, bg= color, command=func, fg= '#E4D6C3', height=3, width=20, 
#                         activebackground='#1B263B', cursor='hand2', font=("Arial", 16, 'bold'))
#             btn.pack(padx=12, pady=12)



#         # books frame in right side
#         books_table = Frame(main_container, bg= "#E4D6C3", width= 1200, highlightbackground='#1B263B', highlightthickness=0.5)
#         books_table.pack(side='right', fill='y', padx=50, pady=25)
#         books_table.pack_propagate(False)


#         # viewing available books
#         self.avail_books = Frame(books_table, bg= '#E4D6C3', highlightbackground='#1B263B', highlightthickness=0.5)
#         self.avail_books.pack(side='top', fill='both', expand=True)
#         self.avail_books.pack_propagate(False)

#         avail_header = Frame(self.avail_books,bg='#1B263B', height=20)
#         avail_header.pack(side='top', fill='x')
#         avail_header.pack_propagate(False)

#         self.avail_scroll = Scrollbar(self.avail_books, orient='vertical')
#         self.avail_scroll.pack(side='right', fill='y')

#         avail_label = Label(avail_header, text='Available Books', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
#         avail_label.pack()
#         avail_label.pack_propagate(False)

#         self.issued_books = Frame(books_table, bg = '#E4D6C3',highlightbackground='#1B263B', highlightthickness=0.5)
#         self.issued_books.pack(side='bottom', fill='both', expand=True)
#         self.issued_books.pack_propagate(False)

#         issued_header = Frame(self.issued_books,bg='#1B263B', height=20)
#         issued_header.pack(side='top', fill='x')
#         issued_header.pack_propagate(False)

#         self.issued_scroll = Scrollbar(self.issued_books, orient='vertical')
#         self.issued_scroll.pack(side='right', fill='y')


#         issued_label = Label(issued_header, text='Issued Books', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
#         issued_label.pack()
#         issued_label.pack_propagate(False)


#     def insert_book_data(self):
#         self.book_tree = ttk.Treeview(self.avail_books, columns=("Book ID", "Book Title", "Book Author", "Quantity"), 
#                                 show='headings', height=12, style='Treeview')
#         self.book_tree.heading('Book ID', text='Book ID', anchor='w')
#         self.book_tree.heading('Book Title', text='Book Title', anchor='w')
#         self.book_tree.heading('Book Author', text='Book Author', anchor='w')
#         self.book_tree.heading('Quantity', text='Quantity', anchor='center')
#         self.book_tree.column('Book ID', width=80)
#         self.book_tree.column('Book Title', width= 350)
#         self.book_tree.column('Book Author', width= 300)
#         self.book_tree.column('Quantity', width= 80,anchor='center')

#         self.book_tree.pack(fill='both', expand=True)
#         self.book_tree.configure(yscrollcommand=self.avail_scroll.set)
#         self.avail_scroll.config(command=self.book_tree.yview)

#         book_data = database.get_books()
#         for i in book_data:
#             self.book_tree.insert('', 'end', values=i)


#     def issued_book_data(self):

#         self.issued_tree = ttk.Treeview(self.issued_books, columns=('Issued Book ID', 'Book ID', 'Student Name', 'Student Enrollment', 'Issued Date', 'Issued Days'),
#                                 show='headings', height=12, style='Treeview')
#         self.issued_tree.heading('Issued Book ID', text='Issued Book ID', anchor='w')
#         self.issued_tree.heading('Book ID', text= 'Book ID', anchor='w')
#         self.issued_tree.heading('Student Name', text='Student Name', anchor='w')
#         self.issued_tree.heading('Student Enrollment', text='Student Enrollment', anchor='w')
#         self.issued_tree.heading('Issued Date', text='Issued Date', anchor='w')
#         self.issued_tree.heading('Issued Days', text='Issued Days', anchor='w')

#         self.issued_tree.column('Issued Book ID', width=140)
#         self.issued_tree.column('Book ID', width=100)
#         self.issued_tree.column('Student Name', width=250)
#         self.issued_tree.column('Student Enrollment', width=250)
#         self.issued_tree.column('Issued Date', width=150)
#         self.issued_tree.column('Issued Days', width=150)

#         self.issued_tree.pack(fill='both', expand=True)
#         self.issued_tree.configure(yscrollcommand=self.issued_scroll.set)
#         self.issued_scroll.config(command=self.issued_tree.yview)

#         issued_data = database.get_issued_books()

#         for i in issued_data:
#             self.issued_tree.insert('','end', values=i)

#     def tree_styling(self):

#         style = ttk.Style()
#         style.theme_use('default')
#         style.configure('Treeview', background = '#E4D6C3', foreground = '#1B263B', font = ('Arial', 11, 'bold'), fieldbackground="#E4D6C3")
#         style.configure('Treeview.Heading', font = ('Arial', 13, 'bold'))



#     def clear_tree(self,tree):
#         for item in tree.get_children():
#             tree.delete(item)


#     def refresh_books_tree(self):
#         self.clear_tree(self.book_tree)        # remove old rows
#         data = database.get_books()  # fetch updated data

#         for row in data:
#             self.book_tree.insert('', 'end', values=row)

#     def refresh_issue_tree(self):
#         self.clear_tree(self.issued_tree)        # remove old rows
#         data = database.get_issued_books()  # fetch updated data

#         for row in data:
#             self.issued_tree.insert('', 'end', values=row)



#     def add_placeholder(self,entry, text):
#         entry.insert(0, text)
#         entry.config(fg="#495057")

#         def on_focus_in(e):
#             if entry.get() == text:
#                 entry.delete(0, END)
#                 entry.config(fg="black")

#         def on_focus_out(e):
#             if entry.get() == "":
#                 entry.insert(0, text)
#                 entry.config(fg="#495057")

#         entry.bind("<FocusIn>", on_focus_in)
#         entry.bind("<FocusOut>", on_focus_out)



#     def add_book_dialog(self):
#         dialog = Toplevel(self.window)
#         dialog.title('Add New Book')
#         dialog.geometry('450x400')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(self.window)         # keeps the dialogbox a child of root window, if root is minimized then dialog also minmizes
#         dialog.grab_set()         # makes the root window un-interactive, only current active


#         book_label = Label(dialog, text='Add New Book', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)

#         title_label = Label(dialog, text='Title : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         title_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         title_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
#         title_entry.grid(row=2, column=0, padx=13, pady=1, sticky='w') 
#         self.add_placeholder(title_entry, 'Enter Book Title')

#         author_label = Label(dialog, text='Author : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         author_label.grid(row=3, column=0, padx=10, pady=12, sticky='w')

#         author_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
#         author_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w')
#         self.add_placeholder(author_entry, 'Enter Author Name')

#         quant_label = Label(dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         quant_label.grid(row=5, column=0, padx=10, pady=12, sticky='w')

#         quant_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
#         quant_entry.grid(row=6, column=0, padx=13, pady=1, sticky='w')
#         self.add_placeholder(quant_entry, 'Enter Book Quantity')


        
#         def save():
#             title = title_entry.get()
#             author = author_entry.get()
#             quant_str = quant_entry.get()

#             if title == 'Enter Book Title' or author == 'Enter Author Name' or quant_str == 'Enter Book Quantity' or not quant_str.isdigit() or not author.isalpha() or title.isnumeric():
#                 dialog.destroy()
#                 messagebox.showerror('Error', 'Please Enter Valid Details!')
#             else:
#                 quant = int(quant_str)
#                 database.add_book(title,author,quant)
#                 self.refresh_books_tree()
#                 dialog.destroy()

#                 messagebox.showinfo('Success','Book Added Successfully!')


        

#         add_btn = Button(dialog, text='Add Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         add_btn.grid(row=7, column=0,pady=25)

        

        
#     def add_quantity_dialog(self):
#         dialog = Toplevel(self.window)
#         dialog.title('Update Book Quantity')
#         dialog.geometry('400x330')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(self.window)
#         dialog.grab_set()

#         book_label = Label(dialog, text='Add Quantity', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)
        
#         id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
#         self.add_placeholder(id_entry, 'Enter Book ID')

#         amt_label = Label(dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         amt_label.grid(row=3, column=0, padx=10, pady=14, sticky='w')

#         amt_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         amt_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
#         self.add_placeholder(amt_entry, 'Enter Quantity to Add')


#         def save ():
#             book_id = id_entry.get()
#             amt_str = amt_entry.get()

#             if book_id == 'Enter Book ID' or amt_str == 'Enter Quantity to Add' or not book_id.isdigit() or not amt_str.replace("-", '').isnumeric():
#                 dialog.destroy()
#                 messagebox.showerror('Error', 'Please Enter Valid Details!')
#             else:
#                 amt = int(amt_str)
#                 if amt < 0:
#                     dialog.destroy()
#                     messagebox.showerror('Error', 'Negative value cannot be added! ')
#                 else:
#                     database.add_quantity(amt,book_id)
#                     self.refresh_books_tree()
#                     dialog.destroy()
#                     messagebox.showinfo('Success','Quantity Updated Successfully!')


#         btn_1 = Button(dialog, text= 'Update Quantity', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         btn_1.grid(pady=30)

#     def rmv_quantity_dialog(self):
#         dialog = Toplevel(self.window)
#         dialog.title('Update Book Quantity')
#         dialog.geometry('400x330')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(self.window)
#         dialog.grab_set()
        
#         book_label = Label(dialog, text='Remove Quantity', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)

#         id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
#         self.add_placeholder(id_entry, 'Enter Book ID')

#         amt_label = Label(dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         amt_label.grid(row=3, column=0, padx=10, pady=14, sticky='w')

#         amt_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         amt_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
#         self.add_placeholder(amt_entry, 'Enter Quantity to Remove')

#         def save ():
#             book_id = id_entry.get()
#             amt_str = amt_entry.get()

#             if book_id == 'Enter Book ID' or amt_str == 'Enter Quantity to Remove' or not book_id.isdigit() or not amt_str.replace("-", '').isnumeric():
#                 dialog.destroy()
#                 messagebox.showerror('Error', 'Please Enter Valid Details!')

#             else:
#                 amt = int(amt_str)
#                 if amt < 0:
#                     dialog.destroy()
#                     messagebox.showerror('Error', 'Please enter positive quantity.')
#                 else:
#                     database.remv_quantity(amt,book_id)
#                     self.refresh_books_tree()
#                     dialog.destroy()
#                     messagebox.showinfo('Success','Quantity Updated Successfully!')


#         btn_1 = Button(dialog, text= 'Update Quantity', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         btn_1.grid(pady=30)


#     def issue_book_dialog(self):

#         dialog = Toplevel(self.window)
#         dialog.title('Issue Book')
#         dialog.geometry('420x630')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(self.window)

        
#         book_label = Label(dialog, text='Issue Book', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)

#         id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
#         self.add_placeholder(id_entry, 'Enter Book ID to Issue')

#         name_label = Label(dialog, text='Student Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         name_label.grid(row=3, column=0, padx=10, pady=18, sticky='w')

#         name_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         name_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
#         self.add_placeholder(name_entry, 'Enter Student Name')


#         enroll_label = Label(dialog, text='Student Enrollment : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         enroll_label.grid(row=5, column=0, padx=10, pady=18, sticky='w')

#         enroll_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         enroll_entry.grid(row=6, column=0, padx=13, pady=1, sticky='w') 
#         self.add_placeholder(enroll_entry, 'Enter Student Enrollment')

#         date_label = Label(dialog, text='Issue Date: ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         date_label.grid(row=7, column=0, padx=10, pady=18, sticky='w')

#         date_entry = DateEntry(dialog, width=40, background='#1B263B', foreground='#f7e1d7', borderwidth=2, date_pattern='dd-mm-yyyy',font=('Arial', 11, 'bold'))
#         date_entry.grid(row=8, column=0, padx=13, pady=1, sticky='w')

#         days_label = Label(dialog, text='Issue Days : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         days_label.grid(row=9, column=0, padx=10, pady=18, sticky='w')

#         days_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         days_entry.grid(row=10, column=0, padx=13, pady=1, sticky='w')
#         self.add_placeholder(days_entry, 'Enter Number off days to Issue')

#         def save():
#             book_id = id_entry.get()
#             stud_name = name_entry.get()
#             stud_enrol = int(enroll_entry.get())
#             iss_date = date_entry.get()
#             iss_days = days_entry.get()

#             database.issue_book(book_id,stud_name,stud_enrol,iss_date,iss_days)
#             self.refresh_issue_tree()
#             dialog.destroy()
#             messagebox.showinfo('Success','Book Issued Successfully!')



#         issue_btn = Button(dialog, text='Issue Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         issue_btn.grid(pady=25)

#         dialog.grab_set()

        

#     def return_book_dialog(self):
#         dialog = Toplevel(self.window)
#         dialog.title('Return Book')
#         dialog.geometry('400x420')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(self.window)
#         dialog.grab_set()

        
#         book_label = Label(dialog, text='Return Book', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)

#         id_label = Label(dialog, text='Issued Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
#         self.add_placeholder(id_entry, 'Enter Issued Book ID')

#         enroll_label = Label(dialog, text='Student Enrollment : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         enroll_label.grid(row=3, column=0, padx=10, pady=18, sticky='w')

#         enroll_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         enroll_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
#         self.add_placeholder(enroll_entry, 'Enter Student Enrollment')

#         def save():
#             issued_book_id = id_entry.get()
#             stud_enrol = int(enroll_entry.get())

#             database.return_book(issued_book_id,stud_enrol)
#             self.refresh_issue_tree()
#             dialog.destroy()
#             messagebox.showinfo('Success','Book Returned Successfully!')


#         ret_btn = Button(dialog, text='Return Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         ret_btn.grid(pady=25)











# from tkinter import *
# from tkcalendar import DateEntry
# from tkinter import ttk, messagebox
# import database

# def start_app(parent):
#     parent.withdraw()

#     admin_window = Toplevel(parent) 
#     def on_close():
#         admin_window.destroy()
#         parent.deiconify()   # show main window again

#     admin_window.protocol("WM_DELETE_WINDOW", on_close)

#     admin_window.title('Library Management System')
#     admin_window.geometry('1500x750')
#     admin_window.config(bg= "#E4D6C3")


#     # Header Frame---
#     header_frame = Frame(admin_window, bg= '#1B263B',height= 85, relief='raised', bd=2)
#     header_frame.pack(fill='x') 
#     header_frame.pack_propagate(False)

#     header = Label(header_frame, text='Library Management System', bg= '#1B263B',fg='#E4D6C3', font=('Arial', 30, 'bold'), anchor='center')
#     header.pack(pady=15)

#     # Main frame
#     main_container = Frame(admin_window, bg="#E4D6C3")
#     main_container.pack(fill='both', expand=True)

#     # Left frame for buttons
#     button_frame = Frame(main_container, bg= "#E4D6C3", width=220)
#     button_frame.pack(fill='y', side='left', padx= 75, pady= 25)
#     button_frame.propagate(FALSE)

#     button_header = Label(button_frame, text='Operations', font=('Arial', 22, 'bold'), bg='#E4D6C3',fg= '#1B263B')
#     button_header.pack(pady=14)


#     button_config = [
#         ("Add Book", "#6f4518", lambda: add_book_dialog()),
#         ('Add Quantity', "#335c67", lambda: add_quantity_dialog()),
#         ('Remove Quantity', "#800f2f", lambda: rmv_quantity_dialog()),
#         ('Issue Book', "#3a5a40", lambda: issue_book_dialog()),
#         ('Return Book', "#c16200", lambda: return_book_dialog())
#     ]


#     for i, (text, color, func) in enumerate(button_config):
#         btn = Button(button_frame, text=text, bg= color, command=func, fg= '#E4D6C3', height=3, width=20, 
#                     activebackground='#1B263B', cursor='hand2', font=("Arial", 16, 'bold'))
#         btn.pack(padx=12, pady=12)



#     # books frame in right side
#     books_table = Frame(main_container, bg= "#E4D6C3", width= 1200, highlightbackground='#1B263B', highlightthickness=0.5)
#     books_table.pack(side='right', fill='y', padx=50, pady=25)
#     books_table.pack_propagate(False)


#     # viewing available books
#     avail_books = Frame(books_table, bg= '#E4D6C3', highlightbackground='#1B263B', highlightthickness=0.5)
#     avail_books.pack(side='top', fill='both', expand=True)
#     avail_books.pack_propagate(False)

#     avail_header = Frame(avail_books,bg='#1B263B', height=20)
#     avail_header.pack(side='top', fill='x')
#     avail_header.pack_propagate(False)

#     avail_scroll = Scrollbar(avail_books, orient='vertical')
#     avail_scroll.pack(side='right', fill='y')

#     avail_label = Label(avail_header, text='Available Books', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
#     avail_label.pack()
#     avail_label.pack_propagate(False)


#     book_tree = ttk.Treeview(avail_books, columns=("Book ID", "Book Title", "Book Author", "Quantity"), 
#                             show='headings', height=12, style='Treeview')
#     book_tree.heading('Book ID', text='Book ID', anchor='w')
#     book_tree.heading('Book Title', text='Book Title', anchor='w')
#     book_tree.heading('Book Author', text='Book Author', anchor='w')
#     book_tree.heading('Quantity', text='Quantity', anchor='center')
#     book_tree.column('Book ID', width=80)
#     book_tree.column('Book Title', width= 350)
#     book_tree.column('Book Author', width= 300)
#     book_tree.column('Quantity', width= 80,anchor='center')

#     book_tree.pack(fill='both', expand=True)
#     book_tree.configure(yscrollcommand=avail_scroll.set)


#     book_data = database.get_books()
#     for i in book_data:
#         book_tree.insert('', 'end', values=i)




#     # viewing issued books 
#     issued_books = Frame(books_table, bg = '#E4D6C3',highlightbackground='#1B263B', highlightthickness=0.5)
#     issued_books.pack(side='bottom', fill='both', expand=True)
#     issued_books.pack_propagate(False)

#     issued_header = Frame(issued_books,bg='#1B263B', height=20)
#     issued_header.pack(side='top', fill='x')
#     issued_header.pack_propagate(False)

#     issued_scroll = Scrollbar(issued_books, orient='vertical')
#     issued_scroll.pack(side='right', fill='y')


#     issued_label = Label(issued_header, text='Issued Books', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
#     issued_label.pack()
#     issued_label.pack_propagate(False)



#     issued_tree = ttk.Treeview(issued_books, columns=('Issued Book ID', 'Book ID', 'Student Name', 'Student Enrollment', 'Issued Date', 'Issued Days'),
#                             show='headings', height=12, style='Treeview')
#     issued_tree.heading('Issued Book ID', text='Issued Book ID', anchor='w')
#     issued_tree.heading('Book ID', text= 'Book ID', anchor='w')
#     issued_tree.heading('Student Name', text='Student Name', anchor='w')
#     issued_tree.heading('Student Enrollment', text='Student Enrollment', anchor='w')
#     issued_tree.heading('Issued Date', text='Issued Date', anchor='w')
#     issued_tree.heading('Issued Days', text='Issued Days', anchor='w')

#     issued_tree.column('Issued Book ID', width=140)
#     issued_tree.column('Book ID', width=100)
#     issued_tree.column('Student Name', width=250)
#     issued_tree.column('Student Enrollment', width=250)
#     issued_tree.column('Issued Date', width=150)
#     issued_tree.column('Issued Days', width=150)

#     issued_tree.pack(fill='both', expand=True)

#     issued_data = database.get_issued_books()

#     for i in issued_data:
#         issued_tree.insert('','end', values=i)

#     style = ttk.Style()
#     style.theme_use('default')
#     style.configure('Treeview', background = '#E4D6C3', foreground = '#1B263B', font = ('Arial', 11, 'bold'), fieldbackground="#E4D6C3")
#     style.configure('Treeview.Heading', font = ('Arial', 13, 'bold'))



#     def clear_tree(tree):
#         for item in tree.get_children():
#             tree.delete(item)


#     def refresh_books_tree():
#         clear_tree(book_tree)        # remove old rows
#         data = database.get_books()  # fetch updated data

#         for row in data:
#             book_tree.insert('', 'end', values=row)

#     def refresh_issue_tree():
#         clear_tree(issued_tree)        # remove old rows
#         data = database.get_issued_books()  # fetch updated data

#         for row in data:
#             issued_tree.insert('', 'end', values=row)



#     def add_placeholder(entry, text):
#         entry.insert(0, text)
#         entry.config(fg="#495057")

#         def on_focus_in(e):
#             if entry.get() == text:
#                 entry.delete(0, END)
#                 entry.config(fg="black")

#         def on_focus_out(e):
#             if entry.get() == "":
#                 entry.insert(0, text)
#                 entry.config(fg="#495057")

#         entry.bind("<FocusIn>", on_focus_in)
#         entry.bind("<FocusOut>", on_focus_out)



#     def add_book_dialog():
#         dialog = Toplevel(admin_window)
#         dialog.title('Add New Book')
#         dialog.geometry('450x400')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(admin_window)         # keeps the dialogbox a child of root window, if root is minimized then dialog also minmizes
#         dialog.grab_set()         # makes the root window un-interactive, only current active


#         book_label = Label(dialog, text='Add New Book', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)

#         title_label = Label(dialog, text='Title : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         title_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         title_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
#         title_entry.grid(row=2, column=0, padx=13, pady=1, sticky='w') 
#         add_placeholder(title_entry, 'Enter Book Title')

#         author_label = Label(dialog, text='Author : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         author_label.grid(row=3, column=0, padx=10, pady=12, sticky='w')

#         author_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
#         author_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w')
#         add_placeholder(author_entry, 'Enter Author Name')

#         quant_label = Label(dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         quant_label.grid(row=5, column=0, padx=10, pady=12, sticky='w')

#         quant_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
#         quant_entry.grid(row=6, column=0, padx=13, pady=1, sticky='w')
#         add_placeholder(quant_entry, 'Enter Book Quantity')


        
#         def save():
#             title = title_entry.get()
#             author = author_entry.get()
#             quant_str = quant_entry.get()

#             if title == 'Enter Book Title' or author == 'Enter Author Name' or quant_str == 'Enter Book Quantity' or not quant_str.isdigit() or not author.isalpha() or title.isnumeric():
#                 dialog.destroy()
#                 messagebox.showerror('Error', 'Please Enter Valid Details!')
#             else:
#                 quant = int(quant_str)
#                 database.add_book(title,author,quant)
#                 refresh_books_tree()
#                 dialog.destroy()

#                 messagebox.showinfo('Success','Book Added Successfully!')


        

#         add_btn = Button(dialog, text='Add Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         add_btn.grid(row=7, column=0,pady=25)

        

        
#     def add_quantity_dialog():
#         dialog = Toplevel(admin_window)
#         dialog.title('Update Book Quantity')
#         dialog.geometry('400x330')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(admin_window)
#         dialog.grab_set()

#         book_label = Label(dialog, text='Add Quantity', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)
        
#         id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
#         add_placeholder(id_entry, 'Enter Book ID')

#         amt_label = Label(dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         amt_label.grid(row=3, column=0, padx=10, pady=14, sticky='w')

#         amt_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         amt_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
#         add_placeholder(amt_entry, 'Enter Quantity to Add')


#         def save ():
#             id = id_entry.get()
#             amt_str = amt_entry.get()

#             if id == 'Enter Book ID' or amt_str == 'Enter Quantity to Add' or not id.isdigit() or not amt_str.replace("-", '').isnumeric():
#                 dialog.destroy()
#                 messagebox.showerror('Error', 'Please Enter Valid Details!')
#             else:
#                 amt = int(amt_str)
#                 if amt < 0:
#                     dialog.destroy()
#                     messagebox.showerror('Error', 'Negative value cannot be added! ')
#                 else:
#                     database.add_quantity(amt,id)
#                     refresh_books_tree()
#                     dialog.destroy()
#                     messagebox.showinfo('Success','Quantity Updated Successfully!')


#         btn_1 = Button(dialog, text= 'Update Quantity', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         btn_1.grid(pady=30)

#     def rmv_quantity_dialog():
#         dialog = Toplevel(admin_window)
#         dialog.title('Update Book Quantity')
#         dialog.geometry('400x330')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(admin_window)
#         dialog.grab_set()
        
#         book_label = Label(dialog, text='Remove Quantity', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)

#         id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
#         add_placeholder(id_entry, 'Enter Book ID')

#         amt_label = Label(dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         amt_label.grid(row=3, column=0, padx=10, pady=14, sticky='w')

#         amt_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         amt_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
#         add_placeholder(amt_entry, 'Enter Quantity to Remove')

#         def save ():
#             id = id_entry.get()
#             amt_str = amt_entry.get()

#             if id == 'Enter Book ID' or amt_str == 'Enter Quantity to Add' or not id.isdigit() or not amt_str.replace("-", '').isnumeric():
#                 dialog.destroy()
#                 messagebox.showerror('Error', 'Please Enter Valid Details!')

#             else:
#                 amt = int(amt_str)
#                 if amt < 0:
#                     dialog.destroy()
#                     messagebox.showerror('Error', 'Please enter positive quantity.')
#                 else:
#                     database.remv_quantity(amt,id)
#                     refresh_books_tree()
#                     dialog.destroy()
#                     messagebox.showinfo('Success','Quantity Updated Successfully!')


#         btn_1 = Button(dialog, text= 'Update Quantity', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         btn_1.grid(pady=30)


#     def issue_book_dialog():

#         dialog = Toplevel(admin_window)
#         dialog.title('Issue Book')
#         dialog.geometry('420x630')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(admin_window)

        
#         book_label = Label(dialog, text='Issue Book', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)

#         id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
#         add_placeholder(id_entry, 'Enter Book ID to Issue')

#         name_label = Label(dialog, text='Student Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         name_label.grid(row=3, column=0, padx=10, pady=18, sticky='w')

#         name_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         name_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
#         add_placeholder(name_entry, 'Enter Student Name')


#         enroll_label = Label(dialog, text='Student Enrollment : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         enroll_label.grid(row=5, column=0, padx=10, pady=18, sticky='w')

#         enroll_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         enroll_entry.grid(row=6, column=0, padx=13, pady=1, sticky='w') 
#         add_placeholder(enroll_entry, 'Enter Student Enrollment')

#         date_label = Label(dialog, text='Issue Date: ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         date_label.grid(row=7, column=0, padx=10, pady=18, sticky='w')

#         date_entry = DateEntry(dialog, width=40, background='#1B263B', foreground='#f7e1d7', borderwidth=2, date_pattern='dd-mm-yyyy',font=('Arial', 11, 'bold'))
#         date_entry.grid(row=8, column=0, padx=13, pady=1, sticky='w')

#         days_label = Label(dialog, text='Issue Days : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         days_label.grid(row=9, column=0, padx=10, pady=18, sticky='w')

#         days_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         days_entry.grid(row=10, column=0, padx=13, pady=1, sticky='w')
#         add_placeholder(days_entry, 'Enter Number off days to Issue')
#         print(name_entry.get())

#         def save():
#             book_id = id_entry.get()
#             stud_name = name_entry.get()
#             stud_enrol = int(enroll_entry.get())
#             iss_date = date_entry.get()
#             iss_days = days_entry.get()

#             database.issue_book(book_id,stud_name,stud_enrol,iss_date,iss_days)
#             refresh_issue_tree()
#             dialog.destroy()
#             messagebox.showinfo('Success','Book Issued Successfully!')



#         issue_btn = Button(dialog, text='Issue Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         issue_btn.grid(pady=25)

#         dialog.grab_set()

        

#     def return_book_dialog():
#         dialog = Toplevel(admin_window)
#         dialog.title('Return Book')
#         dialog.geometry('400x420')
#         dialog.config(bg='#f7e1d7')
#         dialog.transient(admin_window)
#         dialog.grab_set()

        
#         book_label = Label(dialog, text='Return Book', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
#         book_label.grid( pady=12)

#         id_label = Label(dialog, text='Issued Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

#         id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
#         add_placeholder(id_entry, 'Enter Issued Book ID')

#         enroll_label = Label(dialog, text='Student Enrollment : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
#         enroll_label.grid(row=3, column=0, padx=10, pady=18, sticky='w')

#         enroll_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
#         enroll_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
#         add_placeholder(enroll_entry, 'Enter Student Enrollment')

#         def save():
#             issued_book_id = id_entry.get()
#             stud_enrol = int(enroll_entry.get())

#             database.return_book(issued_book_id,stud_enrol)
#             refresh_issue_tree()
#             dialog.destroy()
#             messagebox.showinfo('Success','Book Returned Successfully!')


#         ret_btn = Button(dialog, text='Return Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
#         ret_btn.grid(pady=25)



# import cv2

# cap = cv2.VideoCapture(0)
# detector = cv2.QRCodeDetector()

# while True:
#     ret, frame = cap.read()
#     data, bbox, _ = detector.detectAndDecode(frame)

#     if data:
#         print("QR Code Data:", data)

#     cv2.imshow("QR Scanner", frame)

#     if cv2.waitKey(1) == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()


# import cv2

# cap = cv2.VideoCapture(0)
# detector = cv2.QRCodeDetector()

# while True:
#     ret, frame = cap.read()
#     data, bbox, _ = detector.detectAndDecode(frame)

#     if data:
#         print("QR Code Data:", data)
#         break   # 🔥 stop loop after detection

#     cv2.imshow("QR Scanner", frame)

#     if cv2.waitKey(1) == 27:   # ESC key
#         break

# cap.release()
# cv2.destroyAllWindows() 


# import cv2

# # Faster startup on Windows
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# # Lower resolution for speed
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# qr_detector = cv2.QRCodeDetector()
# barcode_detector = cv2.barcode.BarcodeDetector()

# print("Scanning...")

# # Skip initial dark frames (camera warm-up)
# for _ in range(15):
#     cap.read()

# scanned_data = None

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # ---------------- QR Detection ----------------
#     qr_data, qr_bbox, _ = qr_detector.detectAndDecode(frame)

#     if qr_data:
#         scanned_data = qr_data
#         print("QR Code:", scanned_data)

#         if qr_bbox is not None:
#             qr_bbox = qr_bbox.astype(int)
#             for i in range(len(qr_bbox)):
#                 pt1 = tuple(qr_bbox[i][0])
#                 pt2 = tuple(qr_bbox[(i + 1) % len(qr_bbox)][0])
#                 cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

#     # ---------------- Barcode Detection ----------------
#     decoded_info, decoded_type, points = barcode_detector.detectAndDecode(frame)

#     if decoded_info and not scanned_data:
#         # Handle both string and list cases
#         if isinstance(decoded_info, list):
#             data = decoded_info[0]
#         else:
#             data = decoded_info

#         if data:
#             scanned_data = data
#             print("Barcode:", scanned_data)

#             if points is not None:
#                 points = points.astype(int)
#                 for i in range(len(points[0])):
#                     pt1 = tuple(points[0][i])
#                     pt2 = tuple(points[0][(i + 1) % len(points[0])])
#                     cv2.line(frame, pt1, pt2, (255, 0, 0), 2)

#     cv2.imshow("QR + Barcode Scanner", frame)

#     # 🔥 Auto-stop after first successful scan
#     if scanned_data:
#         cv2.waitKey(1000)  # show result for 1 second
#         break

#     if cv2.waitKey(1) == 27:  # ESC
#         break

# cap.release()
# cv2.destroyAllWindows()

# print("Final Scanned Data:", scanned_data)



# import qrcode
# import os

# # Make sure folder exists
# if not os.path.exists("qrcodes"):
#     os.makedirs("qrcodes")

# book_id = "BOOK_1"
# qr = qrcode.make(book_id)

# file_path = os.path.join("qrcodes", f"{book_id}.png")
# qr.save(file_path)

# print("QR saved at:", file_path)




# import tkinter as tk

# root = tk.Tk()
# root.geometry("600x400")
# root.title("Sliding Menu Example")

# menu_width = 200
# menu_visible = False

# # Top bar
# topbar = tk.Frame(root, bg="lightblue", height=50)
# topbar.pack(fill="x")

# # Menu Frame
# menu_frame = tk.Frame(root, bg="lightgray", width=menu_width, height=400)
# menu_frame.place(x=-menu_width, y=0)   # start hidden outside

# # Menu buttons
# tk.Button(menu_frame, text="Dashboard").pack(fill="x", pady=10)
# tk.Button(menu_frame, text="Add Book").pack(fill="x", pady=10)
# tk.Button(menu_frame, text="Issue Book").pack(fill="x", pady=10)
# tk.Button(menu_frame, text="Return Book").pack(fill="x", pady=10)

# # Animation functions
# def slide_in():
#     x = menu_frame.winfo_x()
#     if x < 0:
#         menu_frame.place(x=x+10, y=0)
#         root.after(10, slide_in)

# def slide_out():
#     x = menu_frame.winfo_x()
#     if x > -menu_width:
#         menu_frame.place(x=x-10, y=0)
#         root.after(10, slide_out)

# def toggle_menu():
#     global menu_visible
#     if menu_visible:
#         slide_out()
#         menu_visible = False
#     else:
#         slide_in()
#         menu_visible = True

# # Hamburger Button
# menu_button = tk.Button(topbar, text="☰", font=("Arial",16), command=toggle_menu)
# menu_button.pack(side="left", padx=10, pady=5)

# root.mainloop()



# from tkcalendar import DateEntry
# from datetime import timedelta
# import tkinter as tk

# root = tk.Tk()

# date_entry = DateEntry(root)
# date_entry.pack(pady=10)

# def add_days():
#     selected_date = date_entry.get_date()   # returns datetime.date
#     new_date = selected_date + timedelta(days=15)
#     print(new_date)

# btn = tk.Button(root, text="Add 15 days", command=add_days)
# btn.pack()

# root.mainloop()



# my_list = [1,2,[3,4,5]]
# # print(my_list)
# a = my_list[2].pop(2)
# print(a)


# from tkinter import *

# root = Tk()
# root.geometry("400x300")

# container = Frame(root)
# container.pack(fill="both", expand=True)

# # Create two frames
# frame1 = Frame(container, bg="lightblue")
# frame2 = Frame(container, bg="lightgreen")

# # Place them in the SAME position
# for frame in (frame1, frame2):
#     frame.place(relwidth=1, relheight=1)

# # Content of frame1
# Label(frame1, text="HOME PAGE", font=("Arial", 20), bg="lightblue").pack(pady=40)
# Button(frame1, text="Go to Profile", command=lambda: frame2.tkraise()).pack()

# # Content of frame2
# Label(frame2, text="PROFILE PAGE", font=("Arial", 20), bg="lightgreen").pack(pady=40)
# Button(frame2, text="Go to Home", command=lambda: frame1.tkraise()).pack()

# # Show first frame
# frame1.tkraise()

# root.mainloop()

# import database

# data = database.get_current_issued_books(240170117059,'KRISH GURMUKHDAS SAJNANI')

# data.append((2,"2026-04-25"))
# # print(data)

# a = [i[1] for i in data ]
# print(a)