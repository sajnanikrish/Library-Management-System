from tkinter import *
from tkinter import font, messagebox
import admin_gui
import database



class Admin_Login:
    def __init__(self, parent):
        self.parent = parent
        self.parent.withdraw()
        
        self.window = Toplevel(parent)
        self.window.title('Library Management System')
        self.window.minsize(360,400)
        self.window.maxsize(360,400)
        self.window.config(bg='#E4D6C3')

        self.window.protocol('WM_DELETE_WINDOW', self.on_close)
        self._set_ui()
        self._center_window()


    def on_close(self):
        self.window.destroy()
        self.parent.deiconify()
    

    def _center_window(self):

        self.window.update_idletasks()

        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        geom = '360x400'

        self.window.geometry(f"{geom}+{x}+{y}")


    def open_signup(self):
        Sign_Up(self.window)

    # def open_app(self):
    #     admin_gui.start_app(self.window)

    def save(self):
        admin_name = self.user_entry.get()
        password = self.pass_entry.get()
        role = 'admin'
        stored_password = database.get_admin(admin_name, role)

        if stored_password is None:
            messagebox.showerror("Error", "Admin not found") 

        elif stored_password == password:
            self.window.destroy()
            admin_gui.Start_app(self.parent)
        else:
            messagebox.showerror('Error', 'Incorrect Details!')


    def _set_ui(self):
        if database.admin_exists():
            state = 'disabled'
        else:
            state = 'normal'

        heading_label = Label(self.window, text='Admin Login',  font=('Arial', 28, 'bold'), bg='#E4D6C3', fg='#1B263B')
        heading_label.grid(row=0, column=0, pady=15, padx=60)

        user_label = Label(self.window, text='Enter Username : ', font=('Arial', 15, 'bold'), bg='#E4D6C3', fg='#1B263B')
        user_label.grid(row=1, column=0, padx=10,pady=18, sticky='w')

        self.user_entry = Entry(self.window, width=37, bg= '#d5bdaf', fg='black', font=('Arial', 13, 'bold'))
        self.user_entry.grid(row=2, column=0, sticky='w', padx=15, pady=2) 

        pass_label = Label(self.window, text='Enter Password : ', bg='#E4D6C3', fg='#1B263B', font=('Arial', 15, 'bold'))
        pass_label.grid(row=3, column=0, sticky='w', padx=10, pady=18)

        self.pass_entry = Entry(self.window, width=37, bg= '#d5bdaf', fg='black', font=('Arial', 13, 'bold'), show='*')
        self.pass_entry.grid(row=4, column=0, sticky='w', padx=15, pady=2)

        login_btn = Button(self.window, text='Login', bg='#1B263B', fg='#E4D6C3', font=('Arial', 20, 'bold'), padx=40, activebackground='#669bbc', command= self.save)
        login_btn.grid(row=5, column=0, pady=17)

        link_font = font.Font(underline=TRUE, family='Arial', size=18, weight='bold')

        self.sign_label = Button(self.window, text='Sign Up', bg='#E4D6C3', fg= '#1B263B', font=link_font, cursor='hand2', borderwidth=0, activebackground='#E4D6C3', command=self.open_signup, state=state)
        self.sign_label.grid(row=6, column=0)

        if database.admin_exists():
            self.sign_label.config(state='disabled')


class Sign_Up:
    def __init__(self, parent):
        self.parent = parent
        self.parent.withdraw()

        self.window = Toplevel(parent)
        self.window.title('Library Management System')
        self.window.minsize(360,400)
        self.window.maxsize(360,400)
        self.window.config(bg='#E4D6C3')

        self.window.protocol('WM_DELETE_WINDOW', self.on_close)
        self._set_ui()
        self._center_window()

    def on_close(self):
        self.window.destroy()
        self.parent.deiconify()

    def _center_window(self):

        self.window.update_idletasks()

        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        geom = '360x400'

        self.window.geometry(f"{geom}+{x}+{y}")

    def _set_ui(self):
        heading_label = Label(self.window, text='Admin SignUp',  font=('Arial', 28, 'bold'), bg='#E4D6C3', fg='#1B263B')
        heading_label.grid(row=0, column=0, pady=15, padx=50)

        user_label = Label(self.window, text='Enter Username : ', font=('Arial', 15, 'bold'), bg='#E4D6C3', fg='#1B263B')
        user_label.grid(row=1, column=0, padx=10,pady=18, sticky='w')

        self.user_entry = Entry(self.window, width=37, bg= '#d5bdaf', fg='black', font=('Arial', 13, 'bold'))
        self.user_entry.grid(row=2, column=0, sticky='w', padx=15, pady=2) 

        pass_label = Label(self.window, text='Enter Password : ', bg='#E4D6C3', fg='#1B263B', font=('Arial', 15, 'bold'))
        pass_label.grid(row=3, column=0, sticky='w', padx=10, pady=18)

        self.pass_entry = Entry(self.window, width=37, bg= '#d5bdaf', fg='black', font=('Arial', 13, 'bold'), show='*')
        self.pass_entry.grid(row=4, column=0, sticky='w', padx=15, pady=2)

        create_btn = Button(self.window, text='Create Account', bg='#1B263B', fg='#E4D6C3', font=('Arial', 17, 'bold'), padx=18, activebackground='#669bbc', command=self.save)
        create_btn.grid(row=5, column=0, pady=35)

    
    def save(self):
        if database.admin_exists():
            messagebox.showerror("Error", "Admin already exists!")
            return

        user_name = self.user_entry.get()
        password = self.pass_entry.get()
        role = 'admin'

        database.add_admin(user_name, password,role)

        self.window.destroy()
        messagebox.showinfo('Success', 'Account Created Successfully!')

        self.parent.deiconify()
        
    