from tkinter import *
import database
from tkinter import messagebox



class RemoveQuantityDialog:
    def __init__(self, admin):
        self.admin = admin
        self.parent = admin.window
        self.remove_quant()

    def remove_quant(self):
        self.dialog = Toplevel(self.parent)
        self.dialog.geometry('400x330')
        self.admin._center_dialog(self.dialog)
        self.dialog.title('Update Book Quantity')
        self.dialog.config(bg='#f7e1d7')
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        book_label = Label(self.dialog, text='Remove Quantity', font=('Arial', 21, 'bold'), bg='#f7e1d7', fg='#370617')
        book_label.grid( pady=12)

        id_label = Label(self.dialog, text='Book ID : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        id_label.grid(row=1, column=0, padx=10, pady=12, sticky='w')

        id_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
        id_entry.grid(row=2, column=0, padx=13, pady=4, sticky='w') 
        self.admin.add_placeholder(id_entry, 'Enter Book ID')

        amt_label = Label(self.dialog, text='Quantity : ', font=('Arial', 18, 'bold'), bg='#f7e1d7', fg='#1B263B')
        amt_label.grid(row=3, column=0, padx=10, pady=14, sticky='w')

        amt_entry = Entry(self.dialog, bg='#d5bdaf', fg='black', width= 40, font=('Arial', 12, 'bold'))
        amt_entry.grid(row=4, column=0, padx=13, pady=1, sticky='w') 
        self.admin.add_placeholder(amt_entry, 'Enter Quantity to Remove')

        def save ():
            book_id = id_entry.get()
            amt_str = amt_entry.get()

            if book_id == 'Enter Book ID' or amt_str == 'Enter Quantity to Remove' or not book_id.isdigit() or not amt_str.replace("-", '').isnumeric():
                # self.dialog.destroy()
                messagebox.showerror('Error', 'Please Enter Valid Details!')

            else:
                amt = int(amt_str)
                if amt < 0:
                    # self.dialog.destroy()
                    messagebox.showerror('Error', 'Please enter positive quantity.')
                else:
                    database.remv_quantity(amt,book_id)
                    self.admin.refresh_books_tree()
                    self.dialog.destroy()
                    messagebox.showinfo('Success','Quantity Updated Successfully!')


        btn_1 = Button(self.dialog, text= 'Update Quantity', background='#1B263B', fg='#d5bdaf', font = ('Arial', 12, 'bold'),padx=10, pady=10, activebackground='#669bbc',command=save)
        btn_1.grid(pady=30)