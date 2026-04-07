from tkinter import *
import database 
from tkinter import messagebox
from utils.scanner import scan_book, scan_student


class ReturnBookDialog:
    def __init__(self, admin):
        self.admin = admin
        self.parent = admin.window
        self.return_book()

    def return_book(self):
        dialog = Toplevel(self.parent)
        dialog.geometry('810x540')
        self.admin._center_dialog(dialog)
        dialog.title('Return Book')
        dialog.config(bg='#f7e1d7')
        dialog.transient(self.parent)
        dialog.grab_set()

        
        book_label = Label(dialog, text='Return Book', font=('Arial', 22, 'bold'), bg='#f7e1d7', fg='#370617')
        book_label.grid(row=1, column=0, pady=12, padx=300)

        book_scan_btn = Button(dialog, text='Scan Book QR', font=('Arial', 15, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.scan_book_data, activebackground='#1B263B', padx=5, pady=5)
        book_scan_btn.grid(row=2, column=0, padx= 40, pady=12, sticky='w')

        student_scan_btn = Button(dialog, text='Scan Student QR', font=('Arial', 15, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.scan_student_data, activebackground='#1B263B', padx=5, pady=5)
        student_scan_btn.grid(row=2, column=0, padx= 40, pady=12, sticky='e')

        id_label = Label(dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        id_label.grid(row=3, column=0, padx=12, pady=10, sticky='w')

        fine_label = Label(dialog,text='Fine (if any) : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        fine_label.grid(row=3, column=0, padx=168, pady=10, sticky='e')

        self.fine_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 20, font=('Arial', 12, 'bold'))
        self.fine_entry.grid(row=4, column=0, padx=147, pady=6, sticky='e')
        self.admin.add_placeholder(self.fine_entry, 'Fine Amount')

        fine_btn = Button(dialog, text='Calculate Fine', font=('Arial', 11, 'bold'), bg='#1B263B', fg='#f7e1d7', command= self.calculate_fine, activebackground='#1B263B', padx=5, pady=5)
        fine_btn.grid(row=4, column=0, padx=10, pady=6, sticky='e')

        self.id_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        self.id_entry.grid(row=4, column=0, padx=16, pady=6, sticky='w') 
        self.admin.add_placeholder(self.id_entry, 'Enter Book ID')

        book_name = Label(dialog, text='Book Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        book_name.grid(row=5, column=0, sticky='w', padx=12, pady=6)

        name_label = Label(dialog, text='Student Name : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        name_label.grid(row=5, column=0, padx=145, sticky='e', pady=6)

        self.book_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        self.book_entry.grid(row=6, column=0, pady=6, padx=16, sticky='w')
        self.admin.add_placeholder(self.book_entry, 'Enter Book Name')


        self.name_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        self.name_entry.grid(row=6, column=0, padx=10, pady=6, sticky='e') 
        self.admin.add_placeholder(self.name_entry, 'Enter Student Name')


        book_author = Label(dialog, text='Book Author : ',  font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        book_author.grid(row=7, column=0, sticky='w', padx=12, pady=6)

        enroll_label = Label(dialog, text='Student Enrollment : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        enroll_label.grid(row=7, column=0,padx=85, sticky='e', pady=6)

        self.author_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        self.author_entry.grid(row=8, column=0,  pady=6, padx=16, sticky='w')
        self.admin.add_placeholder(self.author_entry, 'Enter Book Author')


        self.enroll_entry = Entry(dialog, bg='#d5bdaf', fg='black', width= 35, font=('Arial', 12, 'bold'))
        self.enroll_entry.grid(row=8, column=0, padx=10, pady=6, sticky='e') 
        self.admin.add_placeholder(self.enroll_entry, 'Enter Student Enrollment')

        def save():
            
            book_id = self.id_entry.get()
            stud_name = self.name_entry.get()
            stud_enrol = self.enroll_entry.get()
            
            book_title = self.book_entry.get() 
            book_author = self.author_entry.get()
            fine = self.fine_entry.get()

            if not book_id or not stud_name or not stud_enrol or not book_title or not book_author or book_id == 'Enter Book ID' or stud_name == 'Enter Student Name' or stud_enrol == 'Enter Student Enrollment' or book_title == 'Enter Book Name' or book_author == 'Enter Author Name':
                messagebox.showerror('Error', 'All Details are Required!')
                return
            
            split_fine = fine.split(' ')
            rupees = split_fine[0]
            symbol = split_fine[1]
            
            if not fine or fine == 'Fine Amount' or not rupees.isdigit() or not len(split_fine) == 2 or not symbol == 'Rs.':
                messagebox.showerror('Error', 'Calculate Fine Properly!')
                return

            check = database.return_book(book_id,stud_enrol, stud_name, book_title, book_author, fine)
            if check == False:
                # dialog.destroy()
                messagebox.showerror('Error', 'No matching record found! Please check the details and try again.')
                return
            elif check == True:
                self.admin.refresh_issue_tree()
                self.admin.refresh_books_tree()
                dialog.destroy()
                messagebox.showinfo('Success','Book Returned Successfully!')


        ret_btn = Button(dialog, text='Return Book', background='#1B263B', fg='#d5bdaf', font = ('Arial', 18, 'bold'),padx=10, pady=10, command=save)
        ret_btn.grid(pady=25)

    def calculate_fine(self):
        
        book_id = self.id_entry.get().strip()
        stud_name = self.name_entry.get().strip()
        stud_enrol = self.enroll_entry.get().strip()

        check = database.calculate_fine(book_id,stud_name,stud_enrol)

        if check == False:
            fine = 0
            self.fine_entry.delete(0, END)
            self.fine_entry.insert(0, f'{fine} Rs.')
            return
        
        elif check == None:
            messagebox.showerror('Error', 'Records Not Found')
            return


        else:
            fine = int(check) * 5

            self.fine_entry.delete(0, END)
            self.fine_entry.insert(0, f'{fine} Rs.')
            self.fine_entry.config(fg='black')
            return

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
