from tkinter import *
import database, admin_gui
from tkinter import ttk


class SearchBook: 
    def __init__(self, admin):
        self.admin = admin
        self.parent = admin.window
        self._search_book()

    def _search_book(self):
        self.dialog = Toplevel(self.parent)
        self.dialog.geometry('420x450')
        self.admin._center_dialog(self.dialog)
        self.dialog.title('Search Book')
        self.dialog.config(bg='#f7e1d7')
        self.dialog.transient(self.parent)
        self.dialog.grab_set()

        def add_books():

            
            value = self.search_entry.get().strip()
            # print(value)
            book_names = database.search_book(value)
            # print(book_names)

            if book_names is None:
                admin_gui.Start_app.clear_tree(self.dialog, self.search_tree)
                self.search_tree.insert('', 'end', values=("No Books Found", ""))

            else:
                admin_gui.Start_app.clear_tree(self.dialog, self.search_tree)
                for i in book_names:
                    self.search_tree.insert('', 'end', values=i)

        heading_label = Label(self.dialog, text='Search BOOK', font=('Arial', 20, 'bold'), bg='#f7e1d7', fg='#370617')
        heading_label.grid(row=0, column=0, pady=10, padx=100)

        search_label = Label(self.dialog, text='Enter Book Title to Search : ', font=('Arial', 16, 'bold'), bg='#f7e1d7', fg='#1B263B')
        search_label.grid(row=1, column=0, pady=10, padx=6, sticky='w')

        self.search_entry = Entry(self.dialog, font=('Arial', 12, 'bold'),width=44, bg='#d5bdaf', fg='black')
        self.search_entry.grid(row=2, column=0, sticky='w', padx=10, pady=8)
        admin_gui.Start_app.add_placeholder(self.dialog, self.search_entry, 'Enter Book Title')

        # print(book_name)

        self.search_tree = ttk.Treeview(self.dialog, columns=("Book Name", "Book Author"), show='headings', height=8, style='Treeview')
        self.search_tree.heading('Book Name', text="Book Name", anchor='w')
        self.search_tree.heading('Book Author', text= 'Book Author', anchor='w')
        self.search_tree.column('Book Name', width=190)
        self.search_tree.column('Book Author', width=190)
        self.search_tree.grid(row=3, column=0, pady=20)

        search_btn = Button(self.dialog, text='Search Book', bg='#1B263B', font=('Arial', 16, 'bold'), fg='#f7e1d7', command=add_books, padx=2, pady=2)
        search_btn.grid(row=4, column=0, pady=15, padx=135)