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





# while True:

#     print('1 to view available books.')
#     print('2 to add new book.')
#     print('3 to update book quantity(Increment)')
#     print('4 to update book quantity(Decrement)')
#     print('5 to issue book')
#     print('6 to return book')
#     print('7 to view issued books')

#     choice = int(input('Enter your choice : '))

#     if choice == 1:
#         book_data = database.get_books()
#         print(f"{'ID':<10}{'Title':<20}{'Author':<15}{'Quantity'}")
#         print("-" * 60)
#         for i in book_data:
#             print(f"{i[0]:<10}{i[1]:<20}{i[2]:<15}{i[3]}")


#     elif choice == 2:
#         title = input('Enter book title : ')
#         author = input('Enter author name : ')
#         quant = int(input('Enter number of books : '))
#         database.add_book(title,author,quant)
        


#     elif choice == 3:
#         id_inp = input('Enter the book id to update : ')
#         amt = int(input('Enter the amount to add quantity : '))
#         database.add_quantity(amt,id_inp)

#     elif choice == 4:
#         id_inp = input('Enter the book id to update : ')
#         amt = int(input('Enter the amount to remove from quantity : '))
#         database.remv_quantity(amt,id_inp)
    

#     elif choice == 5:
#         iss_id = input('Enter Book ID to issue : ')
#         stud_name = input('Enter student name : ')
#         stud_enrol = int(input("Enter student enrollment number : "))
#         iss_date = input('Enter issue date(DD-MM-YYYY) : ')
#         iss_days = int(input('Enter number of days for book to be issued : '))
#         database.issue_book(iss_id,stud_name,stud_enrol,iss_date,iss_days)


#     elif choice == 6:
#         ret_id = input('Enter issued book id to return : ')
#         ret_enrl = input('Enter student Enrollment Number : ')

#         database.return_book(ret_id,ret_enrl)


#     elif choice == 7:

#         ret_data = database.get_issued_books()
#         print(f"{'Issued Book ID':<10}{'Book ID':<10}{'Student Name' : <20}{'Student Enrollment':<20}{'Issue Date':<15}{'Issue Days'}")
#         print('-'*100)
#         for i in ret_data:
#             print(f"{i[0]:<10}{i[1]:<10}{i[2]:<20}{i[3]:<20}{i[4]:<15}{i[5]}")

#     else: 
#         print('Please enter valid input(1-7)')

#     inp = int(input('Enter 1 to continue and 2 to end : '))
#     if inp == 2:
#         break
#     else:
#         continue



