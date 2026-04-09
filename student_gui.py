from tkinter import *
from tkinter import ttk, messagebox 
import database, admin_gui


class Start_app:
    def __init__(self, parent, user_name):
        self.parent = parent
        self.user_name = user_name
        self.parent.withdraw()

        self.window = Toplevel(parent)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.window.title('Library Management System')
        self.window.config(bg= "#E4D6C3")
        self.window.minsize(1500,750)

        self._set_header()
        self._set_buttons()
        self._set_books()
        self._insert_book_data()
        self._issued_book_data()
        self._build_profile_page()
        self.tree_styling()
        
        

    def on_close(self):
        self.window.destroy()
        self.parent.deiconify()   # show main window again

    def _set_header(self):

        welcome_frame = Frame(self.window, bg= '#1B263B',height= 55, relief='raised', bd=2)
        welcome_frame.pack(fill='x') 
        welcome_frame.pack_propagate(False)

        welcome_label = Label(welcome_frame, text= f'Welcome, {self.user_name}', font=('Arial', 22, 'bold', 'italic'), fg='#E4D6C3', bg='#1B263B')
        welcome_label.pack(pady= 10)


    def _set_buttons(self):

        self.main_container = Frame(self.window, bg="#E4D6C3")
        self.main_container.pack(fill='both', expand=True)

        button_frame = Frame(self.main_container, bg="#E4D6C3", width= 220)
        button_frame.pack(fill='y', side='left', padx= 75, pady= 30)
        button_frame.propagate(FALSE)

        buttons_config = [
            ('Home', "#71570A" , self._home_page),
            ('My Profile', "#045640", self._my_profile),
            ('Search Book', "#7b1206", self._search_book),
            ('Request Book', "#900d71", self._request_book),
            ('Logout', "#0b3583", self.on_close)
        ]

        for i, (text, color, func) in enumerate(buttons_config):
            btn = Button(button_frame, text=text, bg=color, fg='#E4D6C3', height=2, width=20, command=func,
                        activebackground='#1B263B', cursor='hand2', font=('Arial', 19, 'bold'))
            btn.pack(padx=12, pady=25)

    def _request_book(self):
        dialog = Toplevel(self.window)
        dialog.geometry('400x350')
        admin_gui.Start_app._center_dialog(self.window, dialog)
        dialog.title('Request Book')
        dialog.config(bg='#f7e1d7')
        dialog.transient(self.window)
        dialog.grab_set()


        heading_label = Label(dialog, text='Request Book', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
        heading_label.grid(row=0, column=0, padx=100, pady=10)

        title_label = Label(dialog, text='Enter Book Title : ', font=('Arial', 16, 'bold'),  bg='#f7e1d7', fg='#1B263B')
        title_label.grid(row=1, column=0, pady=10, padx=6, sticky='w')

        self.title_entry = Entry(dialog, font=('Arial', 12, 'bold'),width=42, bg='#d5bdaf', fg='black')
        self.title_entry.grid(row=2, column=0, sticky='w', padx=10, pady=8)
        admin_gui.Start_app.add_placeholder(self.window, self.title_entry, 'Enter Book Name')

        author_label = Label(dialog, text='Enter Book Author : ', font=('Arial', 16, 'bold'),  bg='#f7e1d7', fg='#1B263B')
        author_label.grid(row=3, column=0, pady=10, padx=6, sticky='w')

        self.author_entry = Entry(dialog, font=('Arial', 12, 'bold'),width=42, bg='#d5bdaf', fg='black')
        self.author_entry.grid(row=4, column=0, sticky='w', padx=10, pady=8)
        admin_gui.Start_app.add_placeholder(self.window, self.author_entry, 'Enter Author Name')

        request_btn = Button(dialog, text='Send Request', font=('Arial', 15, 'bold'), padx=2, pady=2, fg='#f7e1d7', bg='#1B263B', activebackground='#1B263B')
        request_btn.grid(row=5, column=0, pady=20, padx=60)



    def _search_book(self):
        dialog = Toplevel(self.window)
        dialog.geometry('420x450')
        admin_gui.Start_app._center_dialog(self.window, dialog)
        dialog.title('Search Book')
        dialog.config(bg='#f7e1d7')
        dialog.transient(self.window)
        dialog.grab_set()

        def add_books():

            
            value = self.search_entry.get().strip()
            # print(value)
            book_names = database.search_book(value)
            # print(book_names)

            if book_names is None:
                admin_gui.Start_app.clear_tree(dialog, self.search_tree)
                self.search_tree.insert('', 'end', values=("No Books Found", ""))

            else:
                admin_gui.Start_app.clear_tree(dialog, self.search_tree)
                for i in book_names:
                    self.search_tree.insert('', 'end', values=i)

        heading_label = Label(dialog, text='Search BOOK', font=('Arial', 20, 'bold'), bg='#f7e1d7', fg='#370617')
        heading_label.grid(row=0, column=0, pady=10, padx=100)

        search_label = Label(dialog, text='Enter Book Title to Search : ', font=('Arial', 16, 'bold'), bg='#f7e1d7', fg='#1B263B')
        search_label.grid(row=1, column=0, pady=10, padx=6, sticky='w')

        self.search_entry = Entry(dialog, font=('Arial', 12, 'bold'),width=44, bg='#d5bdaf', fg='black')
        self.search_entry.grid(row=2, column=0, sticky='w', padx=10, pady=8)
        admin_gui.Start_app.add_placeholder(dialog, self.search_entry, 'Enter Book Title')

        # print(book_name)

        self.search_tree = ttk.Treeview(dialog, columns=("Book Name", "Book Author"), show='headings', height=8, style='Treeview')
        self.search_tree.heading('Book Name', text="Book Name", anchor='w')
        self.search_tree.heading('Book Author', text= 'Book Author', anchor='w')
        self.search_tree.column('Book Name', width=190)
        self.search_tree.column('Book Author', width=190)
        self.search_tree.grid(row=3, column=0, pady=20)

        search_btn = Button(dialog, text='Search Book', bg='#1B263B', font=('Arial', 16, 'bold'), fg='#f7e1d7', command=add_books, padx=2, pady=2)
        search_btn.grid(row=4, column=0, pady=15, padx=135)

    def _home_page(self):
        self.books_table.tkraise()


    def _my_profile(self):
        self.profile_frame.tkraise()

    def _fine_details(self):
        pass
    def _set_books(self):

        self.right_frame = Frame(self.main_container)
        self.right_frame.pack(side='right', fill='both', expand=True, padx=50, pady=54)

        self.books_table = Frame(self.right_frame, bg= "#E4D6C3", width= 1200, highlightbackground='#1B263B', highlightthickness=0.5)
        self.profile_frame = Frame(self.right_frame, bg='#E4D6C3')
        
        for frame in (self.books_table, self.profile_frame):
            frame.place(relheight=1, relwidth=1)

        # viewing available books
        self.avail_books = Frame(self.books_table, bg= '#E4D6C3', highlightbackground='#1B263B', highlightthickness=0.5)
        self.avail_books.pack(side='top', fill='both', expand=True)
        self.avail_books.pack_propagate(False)

        avail_header = Frame(self.avail_books,bg='#1B263B', height=25)
        avail_header.pack(side='top', fill='x')
        avail_header.pack_propagate(False)

        self.avail_scroll = Scrollbar(self.avail_books, orient='vertical')
        self.avail_scroll.pack(side='right', fill='y')

        avail_label = Label(avail_header, text='Available Books', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
        avail_label.pack()
        avail_label.pack_propagate(False)

        self.issued_books = Frame(self.books_table, bg = '#E4D6C3',highlightbackground='#1B263B', highlightthickness=0.5)
        self.issued_books.pack(side='bottom', fill='both', expand=True)
        self.issued_books.pack_propagate(False)

        issued_header = Frame(self.issued_books,bg='#1B263B', height=25)
        issued_header.pack(side='top', fill='x')
        issued_header.pack_propagate(False)

        self.issued_scroll = Scrollbar(self.issued_books, orient='vertical')
        self.issued_scroll.pack(side='right', fill='y')

        issued_label = Label(issued_header, text='Your Current Issued Books', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
        issued_label.pack()
        

        self.books_table.tkraise()

    def _build_profile_page(self):


        upper_frame = Frame(self.profile_frame, height=400)
        upper_frame.pack(fill='both', side='top', expand=True)
        upper_frame.pack_propagate(False)

        lower_frame = Frame(self.profile_frame, bg= '#E4D6C3', height=200, highlightbackground='#1B263B', highlightthickness=1)
        lower_frame.pack(fill='x', pady=15)
        lower_frame.pack_propagate(False)

        left_frame = Frame(upper_frame, bg='#045640', width=500)
        left_frame.pack(side='left',fill='y')
        left_frame.pack_propagate(False)

        upper_left_frame = Frame(left_frame, bg= '#1B263B', height=200)
        upper_left_frame.pack(side='top', fill='x')
        upper_left_frame.pack_propagate(False)


        upper_right_frame = Frame(upper_frame, bg="#9baf17",width=500)
        upper_right_frame.pack(side='right', fill='both')
        

        name_label = Label(upper_left_frame, text=f"Student Name           : {self.user_name.title()}", font=('Arial', 14, 'bold'), bg='#1B263B', fg='#f7e1d7')
        name_label.grid(row=0, column=0 , sticky='w', padx=10, pady= 5)

        enrol_label = Label(upper_left_frame, text=f"Student Enrollment  : {self.enrollment}", font=('Arial', 14, 'bold'), bg='#1B263B', fg='#f7e1d7')
        enrol_label.grid(row=1, column=0 , sticky='w', padx=10)

        id_label = Label(upper_left_frame, text= f"Membership ID         : LIB-{self.user_id}", font=('Arial', 14, 'bold'), bg='#1B263B', fg='#f7e1d7')
        id_label.grid(row=2, column=0 , sticky='w', padx=10, pady= 3) 

        

        issue_header = Frame(lower_frame, bg='#1B263B', height=25)
        issue_header.pack(side='top', fill='x')
        issue_header.pack_propagate(False)

        issue_label = Label(issue_header, text='Your Book Issue History', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
        issue_label.pack()


        history_scroll = Scrollbar(lower_frame, orient='vertical')
        history_scroll.pack(side='right', fill='y')


        self.history_data = ttk.Treeview(lower_frame, columns=("Book ID", "Book Name", "Book Author", "Issue Date", "Return Date", "Fine"),
                                         show='headings', style='Treeview')
        
        self.history_data.heading('Book ID', text='Book ID', anchor='center')
        self.history_data.heading('Book Name', text='Book Title', anchor='w')
        self.history_data.heading('Book Author', text='Book Author', anchor='w')
        self.history_data.heading('Issue Date', text= 'Issued Date', anchor='w')
        self.history_data.heading('Return Date', text='Return Date', anchor='w')
        self.history_data.heading('Fine', text='Fine Amount', anchor='w')
        self.history_data.column('Book ID', width=50, stretch=True)
        self.history_data.column('Book Name', width=220, stretch=True)
        self.history_data.column('Book Author', width=220, stretch=True)
        self.history_data.column('Issue Date', width=100, stretch=True)
        self.history_data.column('Return Date', width=100, stretch=True)
        self.history_data.column('Fine', width=150, stretch=True)

        self.history_data.pack(side='left', fill='both', expand=True)
        self.history_data.configure(yscrollcommand=history_scroll.set)
        history_scroll.config(command=self.history_data.yview)


        book_history = database.issue_history(self.enrollment, self.user_name)
        

        if book_history is None or not book_history:
            self.history_data.insert('', 'end', values = ('','','No Books Issued','','',''))
            self.history_data.config(selectmode='none')
            self.history_data.bind("<Button-1>", lambda e: "break")

        else:

            self.history_data.tag_configure('oddrow', background='#DDD0BE')
            self.history_data.tag_configure('evenrow', background='#E4D6C3')

            for index,i in enumerate(book_history):
                tag = 'evenrow' if index % 2 == 0 else 'oddrow'
                self.history_data.insert('', 'end', values=i, tags=(tag,))

        lower_left_frame = Frame(left_frame, bg='#1B263B', height=280)  
        lower_left_frame.pack(fill='x', pady=70)
        lower_left_frame.pack_propagate(False)

        current_books = database.get_current_issued_books(self.enrollment, self.user_name)
        available_slots = 3-(len(current_books[0]))

        total_fine = database.fine_paid_by_student(self.user_name,self.enrollment)
        
        books_label = Label(lower_left_frame, text= f'Current Books :-   {len(current_books[0])} / 3' ,font=('Arial', 14, 'bold'), bg='#1B263B', fg='#f7e1d7')
        books_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)

        available_label = Label(lower_left_frame, text= f'Available Slots :-   {available_slots} / 3' , font=('Arial', 14, 'bold'), bg='#1B263B', fg='#f7e1d7')
        available_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)

        total_books = Label(lower_left_frame, text= f'Total Books Issued :-   {len(book_history)}' ,font=('Arial', 14, 'bold'), bg='#1B263B', fg='#f7e1d7')
        total_books.grid(row=2, column=0, sticky='w', padx=10, pady=5)

        due_label = Label(lower_left_frame, text='Next Due :  ', font=('Arial', 14, 'bold'), bg='#1B263B', fg='#f7e1d7')
        due_label.grid(row=3, column=0, sticky='w', padx=10, pady=5) 
         

        fine_label = Label(lower_left_frame, text= f'Total Fine Paid :-  {sum(total_fine[0])} Rs.', font=('Arial', 14, 'bold'), bg='#1B263B', fg='#f7e1d7')
        fine_label.grid(row=3, column=0, sticky='w', padx=10, pady=5)



    def _insert_book_data(self):
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
            
        

    def _issued_book_data(self):
        self.issued_tree = ttk.Treeview(self.issued_books, columns=('Issued Book ID', 'Book ID', 'Book Name', 'Book Author', 'Issued Date', 'Due Date'), 
                                show='headings', height=12, style='Treeview')
        self.issued_tree.heading('Issued Book ID', text='Issued Book ID', anchor='w')
        self.issued_tree.heading('Book ID', text= 'Book ID', anchor='w')
        self.issued_tree.heading('Book Name', text='Book Name', anchor='w')
        self.issued_tree.heading('Book Author', text='Book Author', anchor='w')
        self.issued_tree.heading('Issued Date', text='Issued Date', anchor='w')
        self.issued_tree.heading('Due Date', text='Due Date', anchor='w')

        self.issued_tree.column('Issued Book ID', width=140)
        self.issued_tree.column('Book ID', width=100)
        self.issued_tree.column('Book Name', width=250)
        self.issued_tree.column('Book Author', width=250)
        self.issued_tree.column('Issued Date', width=150)
        self.issued_tree.column('Due Date', width=150)

        self.issued_tree.pack(fill='both', expand=True)
        self.issued_tree.configure(yscrollcommand=self.issued_scroll.set)
        self.issued_scroll.config(command=self.issued_tree.yview)

        user_detail = database.get_user(self.user_name, 'student')
        self.enrollment = user_detail[1]
        self.user_id = user_detail[2] 
        
        data = database.student_book_issued(self.enrollment)
        
        if data:
            for i in data:
                self.issued_tree.insert('', 'end', values=i)
        else:
            self.issued_tree.insert('', 'end', values=('','','','No Books Issued', '', ''))
            self.issued_tree.config(selectmode='none')
        

    def tree_styling(self):

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview', background = '#E4D6C3', foreground = '#1B263B', font = ('Arial', 11, 'bold'), fieldbackground="#E4D6C3")
        style.configure('Treeview.Heading', font = ('Arial', 13, 'bold'))
