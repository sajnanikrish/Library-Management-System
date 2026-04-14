from tkinter import *
import database
from tkinter import ttk


class ViewIssueHistory: 
    def __init__(self, admin):
        self.admin = admin
        self.parent = admin.window
        self.view_books()
        self.tree_styling()
        

    def view_books(self):

        self.dialog = Toplevel(self.parent)
        self.dialog.geometry('1290x550')
        self.admin._center_dialog(self.dialog)
        self.dialog.title('View Issue History')
        self.dialog.config(bg='#f7e1d7')
        self.dialog.transient(self.parent)         # keeps the dialogbox a child of root window, if root is minimized then self.dialog also minmizes
        self.dialog.grab_set()  

        heading_label = Label  (self.dialog, text='Issue History', font=('Arial', 24, 'bold'), bg='#f7e1d7', fg='#370617')
        heading_label.grid(row=0, column=0, pady=12, padx=270) 

        issue_table_frame = Frame(self.dialog, bg='#f7e1d7', width=1300)
        issue_table_frame.grid(row=1, column=0, padx=20, pady=25)

        issue_table = ttk.Treeview(issue_table_frame, columns=('Book ID', 'Student Enrollment', 'Student Name', 'Book Name', 'Book Author', 'Issue Date', 'Return Date', 'Fine Amount'),
                                   show='headings', height=14, style='Treeview')
        issue_table.heading('Book ID', text='Book ID', anchor='w')
        issue_table.heading('Student Enrollment', text='Student Enrollment', anchor='w')
        issue_table.heading('Student Name', text='Student Name',anchor='w')
        issue_table.heading('Book Name', text='Book Name', anchor='w')
        issue_table.heading('Book Author', text='Book Author',anchor='w')
        issue_table.heading('Issue Date', text='Issue Date', anchor='w')
        issue_table.heading('Return Date', text='Return Date', anchor='w')
        issue_table.heading('Fine Amount', text='Fine Amount', anchor='w')
        issue_table.column('Book ID', width=70)
        issue_table.column('Student Enrollment', width=175)
        issue_table.column('Student Name', width=220)
        issue_table.column('Book Name', width=200)
        issue_table.column('Book Author', width=200)
        issue_table.column('Issue Date', width=125)
        issue_table.column('Return Date', width=125)
        issue_table.column('Fine Amount', width=120)

        issue_table.pack(side='left', fill='x')

        history_scroll = Scrollbar(issue_table_frame, orient='vertical')
        history_scroll.pack(side='right', fill='y')

        issue_table.configure(yscrollcommand=history_scroll.set)
        history_scroll.config(command=issue_table.yview)

        data = database.book_issue_history()

        if data == []:
            issue_table.insert('', 'end', values=('','','','No Issue History','','','',''))
            return
        
        for index,i in enumerate(data):
            issue_table.insert('', 'end', values=i)

    def tree_styling(self):

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview', background = '#E4D6C3', foreground = '#1B263B', font = ('Arial', 11, 'bold'), fieldbackground="#E4D6C3")
        style.configure('Treeview.Heading', font = ('Arial', 13, 'bold'))

    