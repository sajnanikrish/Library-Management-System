from tkinter import *
from tkinter import ttk
import database
from dialogs import add_book_dialog, add_quantity_dialog, remv_quantity_dialog, issue_book_dialog, return_book_dialog, issue_history_dialog

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

        left_frame = Frame(self.main_container, bg="#E4D6C3", width= 280)
        left_frame.pack(fill='y', side='left')
        left_frame.propagate(FALSE)

        menu_frame = Frame(left_frame, bg="#1B263B")
        self.menu_visible = False

        def toggle_menu():
            # global menu_visible
            if self.menu_visible:
                menu_frame.pack_forget()   # hide menu
                self.menu_visible = False
            else:
                menu_frame.pack(side="left", fill="both", pady=4)
                self.menu_visible = True


        menu_button = Button(left_frame, text="☰", font=("Arial", 14), command=toggle_menu)
        menu_button.pack(side='top', padx=10, pady=12, anchor='w')

        
        buttons_config = [
            ("Add Book",self.open_add_book_dialog),
            ('Add Quantity',self.open_add_quantity_dialog),
            ('Remove Quantity',self.open_rmv_quantity_dialog),
            ('Issue Book', self.open_issue_book_dialog),
            ('Return Book', self.open_return_book_dialog),
            ('Issue History', self.view_issue_history),
            ('Log Out', self.on_close)
        ]
        for i, (text, func) in enumerate(buttons_config):
            btn = Button(menu_frame, text=text, bg='#1B263B', fg='#E4D6C3', height=1, width=15, command=func,
                        activebackground="#0555E8", activeforeground='white', cursor='hand2', font=('Arial', 16, 'bold'), anchor='w', bd=0, highlightthickness=0, relief='flat')
            btn.pack(padx=10, pady=8)

    def set_book_containers(self):

        # books frame in right side
        books_table = Frame(self.main_container, bg= "#E4D6C3", width= 1200)
        books_table.pack(side='right', fill='y', padx=70, pady=45)
        books_table.pack_propagate(False)


        # viewing available books
        self.avail_books = Frame(books_table, bg= '#E4D6C3', highlightbackground='#1B263B', highlightthickness=2)
        self.avail_books.pack(side='top', fill='both', expand=True, pady=20)
        self.avail_books.pack_propagate(False)

        avail_header = Frame(self.avail_books,bg='#1B263B', height=30)
        avail_header.pack(side='top', fill='x')
        avail_header.pack_propagate(False)

        self.avail_scroll = Scrollbar(self.avail_books, orient='vertical')
        self.avail_scroll.pack(side='right', fill='y')

        avail_label = Label(avail_header, text='Available Books', bg='#1B263B', fg='#E4D6C3',font=('Arial', 14, 'bold'), anchor='center')
        avail_label.pack()
        avail_label.pack_propagate(False)

        self.issued_books = Frame(books_table, bg = '#E4D6C3',highlightbackground='#1B263B', highlightthickness=2)
        self.issued_books.pack(side='bottom', fill='both', expand=True, pady=15)
        self.issued_books.pack_propagate(False)

        issued_header = Frame(self.issued_books,bg='#1B263B', height=30)
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
    
        self.book_tree.tag_configure('oddrow', background='#DDD0BE')
        self.book_tree.tag_configure('evenrow', background='#E4D6C3')

        for index,i in enumerate(book_data):
            tag = 'evenrow' if index % 2 == 0 else 'oddrow'
            self.book_tree.insert('', 'end', values=i, tags=(tag,))


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

        self.issued_tree.tag_configure('oddrow', background='#DDD0BE')
        self.issued_tree.tag_configure('evenrow', background='#E4D6C3')

        for index, i in enumerate(issued_data):
            tag = 'evenrow' if index % 2 == 0 else 'oddrow'
            self.issued_tree.insert('','end', values=i, tags=(tag,))

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
        

        
    def open_add_quantity_dialog(self):
        add_quantity_dialog.AddQuantityDialog(self) 


    def open_rmv_quantity_dialog(self):
        remv_quantity_dialog.RemoveQuantityDialog(self) 


    def open_issue_book_dialog(self):
        issue_book_dialog.IssueBookDialog(self)
       

    def open_return_book_dialog(self):
        return_book_dialog.ReturnBookDialog(self)

    def view_issue_history(self):
        issue_history_dialog.ViewIssueHistory(self)
    