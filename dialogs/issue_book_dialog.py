from tkinter import *
import database
from utils.scanner import scan_book, scan_student
from tkinter import messagebox
from tkcalendar import DateEntry 

class IssueBookDialog:
    def __init__(self, admin):
        self.admin = admin
        self.parent = admin.window
        self.issue_book()

    def issue_book(self):
        self.dialog = Toplevel(self.parent)
        self.dialog.geometry('810x680')
        self.admin._center_dialog(self.dialog)
        self.dialog.title('Issue Book')
        self.dialog.config(bg='#f7e1d7')
        self.dialog.transient(self.parent)

        
        book_label = Label(self.dialog, text='Issue Book', font=('Arial', 26, 'bold'), bg='#f7e1d7', fg='#370617')
        book_label.grid( row=1, column=0, padx=300,pady=12)

        book_scan_btn = Button(self.dialog, text='Scan Book QR', font=('Arial', 15, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.scan_book_data, activebackground='#1B263B', padx=5, pady=5)
        book_scan_btn.grid(row=2, column=0, padx= 40, pady=12, sticky='w')

        student_scan_btn = Button(self.dialog, text='Scan Student QR', font=('Arial', 15, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.scan_student_data, activebackground='#1B263B', padx=5, pady=5)
        student_scan_btn.grid(row=2, column=0, padx= 40, pady=12, sticky='e')

        id_label = Label(self.dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        id_label.grid(row=3, padx=40, pady=10)

        self.id_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 15, font=('Arial', 12, 'bold'))
        self.id_entry.grid(row=4,padx=40, pady=13)
        self.admin.add_placeholder(self.id_entry, 'Enter Book ID') 
        
        book_name = Label(self.dialog, text='Book Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        book_name.grid(row=5, column=0, sticky='w', padx=12, pady=6)

        name_label = Label(self.dialog, text='Student Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        name_label.grid(row=5, column=0, padx=145, sticky='e', pady=6)

        self.book_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        self.book_entry.grid(row=6, column=0, pady=6, padx=16, sticky='w')
        self.admin.add_placeholder(self.book_entry, 'Enter Book Name')

        self.name_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        self.name_entry.grid(row=6, column=0, padx=10, pady=6, sticky='e') 
        self.admin.add_placeholder(self.name_entry, 'Enter Student Name')


        book_author = Label(self.dialog, text='Book Author : ',  font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        book_author.grid(row=7, column=0, sticky='w', padx=12, pady=6)

        enroll_label = Label(self.dialog, text='Student Enrollment : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        enroll_label.grid(row=7, column=0,padx=85, sticky='e', pady=6)

        self.author_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        self.author_entry.grid(row=8, column=0,  pady=6, padx=16, sticky='w')
        self.admin.add_placeholder(self.author_entry, 'Enter Author Name')

        self.enroll_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        self.enroll_entry.grid(row=8, column=0, padx=10, pady=6, sticky='e') 
        self.admin.add_placeholder(self.enroll_entry, 'Enter Student Enrollment')

        date_label = Label(self.dialog, text='Issue Date: ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        date_label.grid(row=9, column=0, sticky='w', padx=12, pady=6)

        days_label = Label(self.dialog, text='Issue Days : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        days_label.grid(row=9, column=0,padx=182, sticky='e', pady=6)

        date_entry = DateEntry(self.dialog, width=40, background='#1B263B', foreground='#f7e1d7', borderwidth=2, date_pattern='dd-mm-yyyy',font=('Arial', 11, 'bold'))
        date_entry.grid(row=10, column=0,pady=6, padx=16, sticky='w' )

        days_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        days_entry.grid(row=10, column=0,padx=10, pady=6, sticky='e' )
        self.admin.add_placeholder(days_entry, 'Enter Number of days to Issue')

        def save():
            book_id = self.id_entry.get()
            stud_name = self.name_entry.get()
            stud_enrol = self.enroll_entry.get()
            iss_date = date_entry.get_date()
            iss_days = days_entry.get()
            book_title = self.book_entry.get() 
            book_author = self.author_entry.get()


            
            if not book_id or not stud_name or not stud_enrol or not iss_days or not book_title or not book_author or book_id == 'Enter Book ID' or stud_name == 'Enter Student Name' or stud_enrol == 'Enter Student Enrollment' or iss_days == 'Enter Number of days to Issue' or book_title == 'Enter Book Name' or book_author == 'Enter Author Name':
                messagebox.showerror('Error', 'All Details are Required!')
                return
            
            all_books = database.get_book_ids()

            check = False
            for (id,) in all_books:
                if id == int(book_id):
                    check = True
                    break
                

            if check == False:
                messagebox.showerror('Sorry', 'Book Not Availbale.')
                return 
        
            quant_check = database.book_quantity(book_id)
            # print(quant_check)

            if quant_check[0] == 0:
                messagebox.showinfo('Sorry', 'Out OF Stock!')
                return
            

            database.issue_book(book_id,stud_name,stud_enrol,book_title,book_author,iss_date,iss_days)
            self.admin.refresh_issue_tree()
            self.admin.refresh_books_tree()
            self.dialog.destroy()
            messagebox.showinfo('Success','Book Issued Successfully!')



        issue_btn = Button(self.dialog, text='Issue Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 18, 'bold'),padx=10, pady=10, command=save)
        issue_btn.grid(pady=40)
        self.dialog.grab_set()

    def scan_book_data(self):
        data = scan_book()
        
        # def add_detail_in_book(data):

        if not data.startswith('BOOK_'):
            messagebox.showerror('Error', 'Wrong QR! Please Scan a Book QR.')
            return 
        
        split_data = data.split('_')

        if len(split_data) != 2:
            messagebox.showerror('Error', 'Invalid QR Format!')
            return 

        book_id = split_data[1]

        if not book_id.isdigit():
            messagebox.showerror('Error', 'Invalid Book ID!')
            return 

        book_detail = database.get_book_details(book_id)

        if not book_detail:
            messagebox.showerror('Error', 'Book Not Found With This Book-Id!')
            return 
        

        self.book_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.id_entry.delete(0, END)


        self.book_entry.insert(0, book_detail[0])
        self.book_entry.config(fg='black')

        self.author_entry.insert(0, book_detail[1])
        self.author_entry.config(fg='black')

        self.id_entry.insert(0, book_id)
        self.id_entry.config(fg='black')

    
    def scan_student_data(self):
        data = scan_student()

        if ':' not in data:
            messagebox.showerror('Invalid!', 'Please Scan Valid Student QR!')
            return
    
        split_data = data.split(':')

        if len(split_data) != 2:
            messagebox.showerror('Inavlid!', 'Please Scan Valid Student QR!')
            return False
        
        student_name = split_data[0].strip()
        student_enroll = split_data[1].strip()

        if not student_enroll.isdigit():
            messagebox.showerror('Invalid!', 'Invalid Enrollment Number!')
            return False
        
        self.name_entry.delete(0, END)
        self.enroll_entry.delete(0, END)

        self.name_entry.insert(0,student_name)
        self.name_entry.config(fg='black')

        self.enroll_entry.insert(0,student_enroll)
        self.enroll_entry.config(fg='black')