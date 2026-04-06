from tkinter import *
from tkinter import ttk
import database
from dialogs import add_book_dialog, add_quantity_dialog, remv_quantity_dialog, issue_book_dialog, return_book_dialog

class Start_app:

    def __init__(self, parent):
        self.parent = parent
        self.parent.withdraw()

        self.window = Toplevel(parent) 
        self.window.title('Library Management System')
        self.window.geometry('1500x780')
        self.window.config(bg= "#E4D6C3")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.set_header()
        self.set_buttons()
        self.set_book_containers()
        self.tree_styling()
        self.insert_book_data()
        self.issued_book_data()

    def on_close(self):
        self.window.destroy()
        self.parent.deiconify()   # show main window again

        
    # Header Frame---
    def set_header(self):
        header_frame = Frame(self.window, bg= '#1B263B',height= 85, relief='raised', bd=2)
        header_frame.pack(fill='x') 
        header_frame.pack_propagate(False)

        header = Label(header_frame, text='Library Management System', bg= '#1B263B',fg='#E4D6C3', font=('Arial', 30, 'bold'), anchor='center')
        header.pack(pady=15)

    # Main frame
    def set_buttons(self):

        self.main_container = Frame(self.window, bg="#E4D6C3")
        self.main_container.pack(fill='both', expand=True)

        # Left frame for buttons
        button_frame = Frame(self.main_container, bg= "#E4D6C3", width=220)
        button_frame.pack(fill='y', side='left', padx= 75, pady= 25)
        button_frame.propagate(FALSE)

        button_header = Label(button_frame, text='Operations', font=('Arial', 22, 'bold'), bg='#E4D6C3',fg= '#1B263B')
        button_header.pack(pady=14)

        button_config = [
            ("Add Book", "#6f4518", self.open_add_book_dialog),
            ('Add Quantity', "#335c67", self.open_add_quantity_dialog),
            ('Remove Quantity', "#800f2f", self.open_rmv_quantity_dialog),
            ('Issue Book', "#3a5a40", self.open_issue_book_dialog),
            ('Return Book', "#c16200", self.open_return_book_dialog)
        ]


        for i, (text, color, func) in enumerate(button_config):
            btn = Button(button_frame, text=text, bg= color, command=func, fg= '#E4D6C3', height=3, width=20, 
                        activebackground='#1B263B', cursor='hand2', font=("Arial", 16, 'bold'))
            btn.pack(padx=12, pady=12)

    def set_book_containers(self):

        # books frame in right side
        books_table = Frame(self.main_container, bg= "#E4D6C3", width= 1200, highlightbackground='#1B263B', highlightthickness=0.5)
        books_table.pack(side='right', fill='y', padx=50, pady=25)
        books_table.pack_propagate(False)


        # viewing available books
        self.avail_books = Frame(books_table, bg= '#E4D6C3', highlightbackground='#1B263B', highlightthickness=0.5)
        self.avail_books.pack(side='top', fill='both', expand=True)
        self.avail_books.pack_propagate(False)

        avail_header = Frame(self.avail_books,bg='#1B263B', height=20)
        avail_header.pack(side='top', fill='x')
        avail_header.pack_propagate(False)

        self.avail_scroll = Scrollbar(self.avail_books, orient='vertical')
        self.avail_scroll.pack(side='right', fill='y')

        avail_label = Label(avail_header, text='Available Books', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
        avail_label.pack()
        avail_label.pack_propagate(False)

        self.issued_books = Frame(books_table, bg = '#E4D6C3',highlightbackground='#1B263B', highlightthickness=0.5)
        self.issued_books.pack(side='bottom', fill='both', expand=True)
        self.issued_books.pack_propagate(False)

        issued_header = Frame(self.issued_books,bg='#1B263B', height=20)
        issued_header.pack(side='top', fill='x')
        issued_header.pack_propagate(False)

        self.issued_scroll = Scrollbar(self.issued_books, orient='vertical')
        self.issued_scroll.pack(side='right', fill='y')


        issued_label = Label(issued_header, text='Issued Books', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
        issued_label.pack()
        issued_label.pack_propagate(False)


    def insert_book_data(self):
        self.book_tree = ttk.Treeview(self.avail_books, columns=("Book ID", "Book Title", "Book Author", "Quantity"), 
                                show='headings', height=12, style='Treeview')
        self.book_tree.heading('Book ID', text='Book ID', anchor='w')
        self.book_tree.heading('Book Title', text='Book Title', anchor='w')
        self.book_tree.heading('Book Author', text='Book Author', anchor='w')
        self.book_tree.heading('Quantity', text='Quantity', anchor='center')
        self.book_tree.column('Book ID', width=80)
        self.book_tree.column('Book Title', width= 350)
        self.book_tree.column('Book Author', width= 300)
        self.book_tree.column('Quantity', width= 80,anchor='center')

        self.book_tree.pack(fill='both', expand=True)
        self.book_tree.configure(yscrollcommand=self.avail_scroll.set)
        self.avail_scroll.config(command=self.book_tree.yview)

        book_data = database.get_books()
        for i in book_data:
            self.book_tree.insert('', 'end', values=i)


    def issued_book_data(self):

        self.issued_tree = ttk.Treeview(self.issued_books, columns=('Issued Book ID', 'Book ID', 'Student Name', 'Student Enrollment', 'Issued Date', 'Issued Days'),
                                show='headings', height=12, style='Treeview')
        self.issued_tree.heading('Issued Book ID', text='Issued Book ID', anchor='w')
        self.issued_tree.heading('Book ID', text= 'Book ID', anchor='w')
        self.issued_tree.heading('Student Name', text='Student Name', anchor='w')
        self.issued_tree.heading('Student Enrollment', text='Student Enrollment', anchor='w')
        self.issued_tree.heading('Issued Date', text='Issued Date', anchor='w')
        self.issued_tree.heading('Issued Days', text='Issued Days', anchor='w')

        self.issued_tree.column('Issued Book ID', width=140)
        self.issued_tree.column('Book ID', width=100)
        self.issued_tree.column('Student Name', width=250)
        self.issued_tree.column('Student Enrollment', width=250)
        self.issued_tree.column('Issued Date', width=150)
        self.issued_tree.column('Issued Days', width=150)

        self.issued_tree.pack(fill='both', expand=True)
        self.issued_tree.configure(yscrollcommand=self.issued_scroll.set)
        self.issued_scroll.config(command=self.issued_tree.yview)

        issued_data = database.get_issued_books()

        for i in issued_data:
            self.issued_tree.insert('','end', values=i)

    def tree_styling(self):

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview', background = '#E4D6C3', foreground = '#1B263B', font = ('Arial', 11, 'bold'), fieldbackground="#E4D6C3")
        style.configure('Treeview.Heading', font = ('Arial', 13, 'bold'))


    def clear_tree(self,tree):
        for item in tree.get_children():
            tree.delete(item)


    def refresh_books_tree(self):
        self.clear_tree(self.book_tree)        # remove old rows
        data = database.get_books()            # fetch updated data

        for row in data:
            self.book_tree.insert('', 'end', values=row)

    def refresh_issue_tree(self):
        self.clear_tree(self.issued_tree)        # remove old rows
        data = database.get_issued_books()  # fetch updated data

        for row in data:
            self.issued_tree.insert('', 'end', values=row)


    def add_placeholder(self,entry, text):
        entry.insert(0, text)
        entry.config(fg="grey")

        def on_focus_in(e):
            if entry.get() == text:
                entry.delete(0, END)
                entry.config(fg="black")

        def on_focus_out(e):
            if entry.get() == "":
                entry.insert(0, text)
                entry.config(fg="black")

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)


    def _center_dialog(self, window):

        window.update_idletasks()

        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)

        window.geometry(f"{width}x{height}+{x}+{y}")


    def open_add_book_dialog(self):
        add_book_dialog.AddBookDialog(self)
         
        # dialog = Toplevel(self.window)
        # dialog.geometry('450x400')
        # self._center_dialog(dialog)
        # dialog.title('Add New Book')
        # dialog.config(bg='#f7e1d7')
        # dialog.transient(self.window)         # keeps the dialogbox a child of root window, if root is minimized then dialog also minmizes
        # dialog.grab_set()         # makes the root window un-interactive, only current active


        # book_label = Label(dialog, text='Add New Book', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
        # book_label.grid( pady=12)

        # title_label = Label(dialog, text='Title : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # title_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

        # self.title_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
        # self.title_entry.grid(row=2, column=0, padx=13, pady=1, sticky='w') 
        # self.add_placeholder(self.title_entry, 'Enter Book Title')

        # author_label = Label(dialog, text='Author : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # author_label.grid(row=3, column=0, padx=10, pady=12, sticky='w')

        # self.author_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
        # self.author_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w')
        # self.add_placeholder(self.author_entry, 'Enter Author Name')

        # quant_label = Label(dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # quant_label.grid(row=5, column=0, padx=10, pady=12, sticky='w')

        # self.quant_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 45, font=('Arial', 12, 'bold'))
        # self.quant_entry.grid(row=6, column=0, padx=13, pady=1, sticky='w')
        # self.add_placeholder(self.quant_entry, 'Enter Book Quantity')


        
        # def save():
        #     title = self.title_entry.get().strip()
        #     author = self.author_entry.get().strip()
        #     quant_str = self.quant_entry.get().strip()

        #     if title == 'Enter Book Title' or author == 'Enter Author Name' or quant_str == 'Enter Book Quantity' or not title or not author or not quant_str:
        #         messagebox.showerror('Error', 'All details are required!')
        #         return
        #     title_pattern = r"^[A-Za-z0-9\s\.\,\:\-\'\(\)]{2,}$"
        #     if not re.match(title_pattern, title):
        #         messagebox.showerror(
        #             'Error',
        #             'Invalid Book Title!\nOnly letters, numbers and . , : - \' ( ) allowed.'
        #         )
        #         return 

        #     # 🔹 Author Validation
        #     author_pattern = r"^[A-Za-z\s\.\-']{2,}$"
        #     if not re.match(author_pattern, author):
        #         messagebox.showerror(
        #             'Error',
        #             'Invalid Author Name!\nOnly letters, spaces, . - \' allowed.'
        #         )
        #         return

        #     # 🔹 Quantity Validation
        #     if not quant_str.isdigit() or int(quant_str) <= 0:
        #         messagebox.showerror('Error', 'Quantity must be a positive number!')
        #         return

        #     quant = int(quant_str)
        #     database.add_book(title,author,quant)
        #     self.refresh_books_tree()
        #     dialog.destroy()

        #     messagebox.showinfo('Success','Book Added Successfully!')


        # add_btn = Button(dialog, text='Add Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
        # add_btn.grid(row=7, column=0,pady=25)

        

        
    def open_add_quantity_dialog(self):
        add_quantity_dialog.AddQuantityDialog(self) 
        
    #     dialog = Toplevel(self.window)
    #     dialog.geometry('400x330')
    #     self._center_dialog(dialog)
    #     dialog.title('Update Book Quantity')
    #     dialog.config(bg='#f7e1d7')
    #     dialog.transient(self.window)
    #     dialog.grab_set()

    #     book_label = Label(dialog, text='Add Quantity', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
    #     book_label.grid( pady=12)
        
    #     id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
    #     id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

    #     id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
    #     id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
    #     self.add_placeholder(id_entry, 'Enter Book ID')

    #     amt_label = Label(dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
    #     amt_label.grid(row=3, column=0, padx=10, pady=14, sticky='w')

    #     amt_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
    #     amt_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
    #     self.add_placeholder(amt_entry, 'Enter Quantity to Add')


    #     def save ():
    #         book_id = id_entry.get()
    #         amt_str = amt_entry.get()

    #         if book_id == 'Enter Book ID' or amt_str == 'Enter Quantity to Add' or not book_id.isdigit() or not amt_str.replace("-", '').isnumeric():
    #             dialog.destroy()
    #             messagebox.showerror('Error', 'Please Enter Valid Details!')
    #         else:
    #             amt = int(amt_str)
    #             if amt < 0:
    #                 dialog.destroy()
    #                 messagebox.showerror('Error', 'Negative value cannot be added! ')
    #             else:
    #                 database.add_quantity(amt,book_id)
    #                 self.refresh_books_tree()
    #                 dialog.destroy()
    #                 messagebox.showinfo('Success','Quantity Updated Successfully!')


    #     btn_1 = Button(dialog, text= 'Update Quantity', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
    #     btn_1.grid(pady=30)

    def open_rmv_quantity_dialog(self):
        remv_quantity_dialog.RemoveQuantityDialog(self) 
    #     dialog = Toplevel(self.window)
    #     dialog.geometry('400x330')
    #     self._center_dialog(dialog)
    #     dialog.title('Update Book Quantity')
    #     dialog.config(bg='#f7e1d7')
    #     dialog.transient(self.window)
    #     dialog.grab_set()
        
    #     book_label = Label(dialog, text='Remove Quantity', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
    #     book_label.grid( pady=12)

    #     id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
    #     id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

    #     id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
    #     id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
    #     self.add_placeholder(id_entry, 'Enter Book ID')

    #     amt_label = Label(dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
    #     amt_label.grid(row=3, column=0, padx=10, pady=14, sticky='w')

    #     amt_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
    #     amt_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
    #     self.add_placeholder(amt_entry, 'Enter Quantity to Remove')

    #     def save ():
    #         book_id = id_entry.get()
    #         amt_str = amt_entry.get()

    #         if book_id == 'Enter Book ID' or amt_str == 'Enter Quantity to Remove' or not book_id.isdigit() or not amt_str.replace("-", '').isnumeric():
    #             dialog.destroy()
    #             messagebox.showerror('Error', 'Please Enter Valid Details!')

    #         else:
    #             amt = int(amt_str)
    #             if amt < 0:
    #                 dialog.destroy()
    #                 messagebox.showerror('Error', 'Please enter positive quantity.')
    #             else:
    #                 database.remv_quantity(amt,book_id)
    #                 self.refresh_books_tree()
    #                 dialog.destroy()
    #                 messagebox.showinfo('Success','Quantity Updated Successfully!')


    #     btn_1 = Button(dialog, text= 'Update Quantity', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, command=save)
    #     btn_1.grid(pady=30)


    def open_issue_book_dialog(self):
        issue_book_dialog.IssueBookDialog(self)
        # dialog = Toplevel(self.window)
        # dialog.geometry('810x680')
        # self._center_dialog(dialog)
        # dialog.title('Issue Book')
        # dialog.config(bg='#f7e1d7')
        # dialog.transient(self.window)

        
        # book_label = Label(dialog, text='Issue Book', font=('Arial', 26, 'bold'), bg='#f7e1d7', fg='#370617')
        # book_label.grid( row=1, column=0, padx=300,pady=12)

        # book_scan_btn = Button(dialog, text='Scan Book QR', font=('Arial', 15, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.scan_book, activebackground='#1B263B', padx=5, pady=5)
        # book_scan_btn.grid(row=2, column=0, padx= 40, pady=12, sticky='w')

        # student_scan_btn = Button(dialog, text='Scan Student QR', font=('Arial', 15, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.scan_student, activebackground='#1B263B', padx=5, pady=5)
        # student_scan_btn.grid(row=2, column=0, padx= 40, pady=12, sticky='e')

        # id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # id_label.grid(row=3, padx=40, pady=10)

        # self.id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 15, font=('Arial', 12, 'bold'))
        # self.id_entry.grid(row=4,padx=40, pady=13)
        # self.add_placeholder(self.id_entry, 'Enter Book ID') 
        
        # book_name = Label(dialog, text='Book Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # book_name.grid(row=5, column=0, sticky='w', padx=12, pady=6)

        # name_label = Label(dialog, text='Student Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # name_label.grid(row=5, column=0, padx=145, sticky='e', pady=6)

        # self.book_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # self.book_entry.grid(row=6, column=0, pady=6, padx=16, sticky='w')
        # self.add_placeholder(self.book_entry, 'Enter Book Name')

        # self.name_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # self.name_entry.grid(row=6, column=0, padx=10, pady=6, sticky='e') 
        # self.add_placeholder(self.name_entry, 'Enter Student Name')


        # book_author = Label(dialog, text='Book Author : ',  font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # book_author.grid(row=7, column=0, sticky='w', padx=12, pady=6)

        # enroll_label = Label(dialog, text='Student Enrollment : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # enroll_label.grid(row=7, column=0,padx=85, sticky='e', pady=6)

        # self.author_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # self.author_entry.grid(row=8, column=0,  pady=6, padx=16, sticky='w')
        # self.add_placeholder(self.author_entry, 'Enter Author Name')

        # self.enroll_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # self.enroll_entry.grid(row=8, column=0, padx=10, pady=6, sticky='e') 
        # self.add_placeholder(self.enroll_entry, 'Enter Student Enrollment')

        # date_label = Label(dialog, text='Issue Date: ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # date_label.grid(row=9, column=0, sticky='w', padx=12, pady=6)

        # days_label = Label(dialog, text='Issue Days : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # days_label.grid(row=9, column=0,padx=182, sticky='e', pady=6)

        # date_entry = DateEntry(dialog, width=40, background='#1B263B', foreground='#f7e1d7', borderwidth=2, date_pattern='dd-mm-yyyy',font=('Arial', 11, 'bold'))
        # date_entry.grid(row=10, column=0,pady=6, padx=16, sticky='w' )

        # days_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # days_entry.grid(row=10, column=0,padx=10, pady=6, sticky='e' )
        # self.add_placeholder(days_entry, 'Enter Number of days to Issue')

        

        # def save():
        #     book_id = self.id_entry.get()
        #     stud_name = self.name_entry.get()
        #     stud_enrol = self.enroll_entry.get()
        #     iss_date = date_entry.get_date()
        #     iss_days = days_entry.get()
        #     book_title = self.book_entry.get() 
        #     book_author = self.author_entry.get()


            
        #     if not book_id or not stud_name or not stud_enrol or not iss_days or not book_title or not book_author or book_id == 'Enter Book ID' or stud_name == 'Enter Student Name' or stud_enrol == 'Enter Student Enrollment' or iss_days == 'Enter Number of days to Issue' or book_title == 'Enter Book Name' or book_author == 'Enter Author Name':
        #         messagebox.showerror('Error', 'All Details are Required!')
        #         return
            
        #     all_books = database.get_book_ids()

        #     check = False
        #     for (id,) in all_books:
        #         if id == int(book_id):
        #             check = True
        #             break
                

        #     if check == False:
        #         messagebox.showerror('Sorry', 'Book Not Availbale.')
        #         return 
        
        #     quant_check = database.book_quantity(book_id)
        #     # print(quant_check)

        #     if quant_check[0] == 0:
        #         messagebox.showinfo('Sorry', 'Out OF Stock!')
        #         return
            

        #     database.issue_book(book_id,stud_name,stud_enrol,book_title,book_author,iss_date,iss_days)
        #     self.refresh_issue_tree()
        #     self.refresh_books_tree()
        #     dialog.destroy()
        #     messagebox.showinfo('Success','Book Issued Successfully!')


        # issue_btn = Button(dialog, text='Issue Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 18, 'bold'),padx=10, pady=10, command=save)
        # issue_btn.grid(pady=40)

           
        # dialog.grab_set()

        

    def open_return_book_dialog(self):
        return_book_dialog.ReturnBookDialog(self)
        # dialog = Toplevel(self.window)
        # dialog.geometry('810x540')
        # self._center_dialog(dialog)
        # dialog.title('Return Book')
        # dialog.config(bg='#f7e1d7')
        # dialog.transient(self.window)
        # dialog.grab_set()

        
        # book_label = Label(dialog, text='Return Book', font=('Arial', 22, 'bold'), bg='#f7e1d7', fg='#370617')
        # book_label.grid(row=1, column=0, pady=12, padx=300)

        # book_scan_btn = Button(dialog, text='Scan Book QR', font=('Arial', 15, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.scan_book, activebackground='#1B263B', padx=5, pady=5)
        # book_scan_btn.grid(row=2, column=0, padx= 40, pady=12, sticky='w')

        # student_scan_btn = Button(dialog, text='Scan Student QR', font=('Arial', 15, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.scan_student, activebackground='#1B263B', padx=5, pady=5)
        # student_scan_btn.grid(row=2, column=0, padx= 40, pady=12, sticky='e')

        # id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # id_label.grid(row=3, column=0, padx=12, pady=10, sticky='w')

        # fine_label = Label(dialog,text='Fine (if any) : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # fine_label.grid(row=3, column=0, padx=168, pady=10, sticky='e')

        # self.fine_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 20, font=('Arial', 12, 'bold'))
        # self.fine_entry.grid(row=4, column=0, padx=147, pady=6, sticky='e')
        # self.add_placeholder(self.fine_entry, 'Fine Amount')

        # fine_btn = Button(dialog, text='Calculate Fine', font=('Arial', 11, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.calculate_fine, activebackground='#1B263B', padx=5, pady=5)
        # fine_btn.grid(row=4, column=0, padx=10, pady=6, sticky='e')

        # self.id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # self.id_entry.grid(row=4, column=0, padx=16, pady=6, sticky='w') 
        # self.add_placeholder(self.id_entry, 'Enter Book ID')

        # book_name = Label(dialog, text='Book Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # book_name.grid(row=5, column=0, sticky='w', padx=12, pady=6)

        # name_label = Label(dialog, text='Student Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # name_label.grid(row=5, column=0, padx=145, sticky='e', pady=6)

        # self.book_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # self.book_entry.grid(row=6, column=0, pady=6, padx=16, sticky='w')
        # self.add_placeholder(self.book_entry, 'Enter Book Name')


        # self.name_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # self.name_entry.grid(row=6, column=0, padx=10, pady=6, sticky='e') 
        # self.add_placeholder(self.name_entry, 'Enter Student Name')


        # book_author = Label(dialog, text='Book Author : ',  font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # book_author.grid(row=7, column=0, sticky='w', padx=12, pady=6)

        # enroll_label = Label(dialog, text='Student Enrollment : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        # enroll_label.grid(row=7, column=0,padx=85, sticky='e', pady=6)

        # self.author_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # self.author_entry.grid(row=8, column=0,  pady=6, padx=16, sticky='w')
        # self.add_placeholder(self.author_entry, 'Enter Book Author')


        # self.enroll_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        # self.enroll_entry.grid(row=8, column=0, padx=10, pady=6, sticky='e') 
        # self.add_placeholder(self.enroll_entry, 'Enter Student Enrollment')

        # def save():
            
        #     book_id = self.id_entry.get()
        #     stud_name = self.name_entry.get()
        #     stud_enrol = self.enroll_entry.get()
            
        #     book_title = self.book_entry.get() 
        #     book_author = self.author_entry.get()
        #     fine = self.fine_entry.get()

        #     if not book_id or not stud_name or not stud_enrol or not book_title or not book_author or book_id == 'Enter Book ID' or stud_name == 'Enter Student Name' or stud_enrol == 'Enter Student Enrollment' or book_title == 'Enter Book Name' or book_author == 'Enter Author Name':
        #         messagebox.showerror('Error', 'All Details are Required!')
        #         return
            
        #     split_fine = fine.split(' ')
        #     rupees = split_fine[0]
        #     symbol = split_fine[1]
            
        #     if not fine or fine == 'Fine Amount' or not rupees.isdigit() or not len(split_fine) == 2 or not symbol == 'Rs.':
        #         messagebox.showerror('Error', 'Calculate Fine Properly!')
        #         return

        #     check = database.return_book(book_id,stud_enrol)
        #     if check == False:
        #         # dialog.destroy()
        #         messagebox.showerror('Error', 'No matching record found! Please check the details and try again.')
        #         return
        #     elif check == True:
        #         self.refresh_issue_tree()
        #         self.refresh_books_tree()
        #         dialog.destroy()
        #         messagebox.showinfo('Success','Book Returned Successfully!')


        # ret_btn = Button(dialog, text='Return Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 18, 'bold'),padx=10, pady=10, command=save)
        # ret_btn.grid(pady=25)

        
    # def scan_student(self):
    #     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #     detector = cv2.QRCodeDetector()

    #     while True:
    #         ret, frame = cap.read()
    #         data, bbox, _ = detector.detectAndDecode(frame)

    #         if data:
    #             if self.add_detail_in_student(data):
    #                 break   # 🔥 stop loop after detection

    #         cv2.imshow("QR Scanner", frame)

    #         if cv2.waitKey(1) == 27:   # ESC key
    #             break

    #     cap.release()
    #     cv2.destroyAllWindows()

    # def add_detail_in_student(self, data):
    #     data = data.strip()
    #     if ':' not in data:
    #         messagebox.showerror('Invalid!', 'Please Scan Valid Student QR!')
    #         return False
        
    #     split_data = data.split(':')

    #     if len(split_data) != 2:
    #         messagebox.showerror('Inavlid!', 'Please Scan Valid Student QR!')
    #         return False
        
    #     student_name = split_data[0].strip()
    #     student_enroll = split_data[1].strip()

    #     if not student_enroll.isdigit():
    #         messagebox.showerror('Invalid!', 'Invalid Enrollment Number!')
    #         return False
        
    #     self.name_entry.delete(0, END)
    #     self.enroll_entry.delete(0, END)

    #     self.name_entry.insert(0,student_name)
    #     self.name_entry.config(fg='black')

    #     self.enroll_entry.insert(0,student_enroll)
    #     self.enroll_entry.config(fg='black')

    #     return True

    # def scan_book(self):
    #     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #     detector = cv2.QRCodeDetector()

    #     while True:
    #         ret, frame = cap.read()
    #         data, bbox, _ = detector.detectAndDecode(frame)

    #         if data:

    #             if self.add_detail_in_book(data):
    #                 break   # 🔥 stop loop after detection

    #         cv2.imshow("QR Scanner", frame)

    #         if cv2.waitKey(1) == 27:   # ESC key
    #             break

    #     cap.release()
    #     cv2.destroyAllWindows()

    # def add_detail_in_book(self, data):

    #     if not data.startswith('BOOK_'):
    #         messagebox.showerror('Error', 'Wrong QR! Please Scan a Book QR.')
    #         return False
        
    #     split_data = data.split('_')

    #     if len(split_data) != 2:
    #         messagebox.showerror('Error', 'Invalid QR Format!')
    #         return False

    #     book_id = split_data[1]

    #     if not book_id.isdigit():
    #         messagebox.showerror('Error', 'Invalid Book ID!')
    #         return False

    #     book_detail = database.get_book_details(book_id)

    #     if not book_detail:
    #         messagebox.showerror('Error', 'Book Not Found With This Book-Id!')
    #         return False
        
        
    #     self.book_entry.delete(0, END)
    #     self.author_entry.delete(0, END)
    #     self.id_entry.delete(0, END)


    #     self.book_entry.insert(0, book_detail[0])
    #     self.book_entry.config(fg='black')

    #     self.author_entry.insert(0, book_detail[1])
    #     self.author_entry.config(fg='black')

    #     self.id_entry.insert(0, book_id)
    #     self.id_entry.config(fg='black')
        
    #     return True