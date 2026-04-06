from tkinter import * 
from tkinter import font, messagebox
import student_gui, database
import cv2


class Student_Login:
    def __init__(self, parent):
        self.parent = parent
        self.parent.withdraw()

        self.window = Toplevel(parent)
        self.window.title('Student Login')
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.minsize(360,450)
        self.window.maxsize(360,450)
        self.window.config(bg= "#E4D6C3")

        self._center_window()
        self._set_ui()

    def on_close(self):
        self.window.destroy()
        self.parent.deiconify()   # show main window again

    
    def _center_window(self):

        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')


    def open_signup(self):
        Sign_Up(self.window)

    def open_app(self, parent, user_name):
        student_gui.Start_app(parent, user_name)

    def save(self):
        self.user_name = self.user_entry.get().strip()
        password_entry = self.pass_entry.get().strip()
        role = 'student'

        data = database.get_user(self.user_name, role)


        if data is None:
            messagebox.showerror('Error', 'No user found!')
            return
            
        pass_word = data[0]

        if pass_word == password_entry:
            self.window.destroy()
            self.open_app(self.parent, self.user_name)
            messagebox.showinfo('Success', 'Logged in Successfully!')
        else:
            messagebox.showwarning('Invalid', 'Incorrect Password!')

    def _set_ui(self):

        title_lbl = Label(self.window, text='Student Login', font=('Arial', 28, 'bold'), bg='#E4D6C3', fg='#1B263B')
        title_lbl.grid(row=0, column=0, padx= 55, pady=15)

        scan_btn = Button(self.window, text='Scan I-Card', font=('Arial', 17, 'bold'), fg='#E4D6C3', bg='#1B263B', padx=3, pady=1, activebackground='#669bbc' ,command=self.scan_details)
        scan_btn.grid(row= 1, column=0)  

        user_label = Label(self.window, text='Enter Username : ', font=('Arial', 15, 'bold'), bg='#E4D6C3', fg='#1B263B')
        user_label.grid(row=2, column=0, padx=10,pady=18, sticky='w')

        self.user_entry = Entry(self.window, width=37, bg= '#d5bdaf', fg='black', font=('Arial', 13, 'bold'))
        self.user_entry.grid(row=3, column=0, sticky='w', padx=15, pady=2) 

        pass_label = Label(self.window, text='Enter Password : ', bg='#E4D6C3', fg='#1B263B', font=('Arial', 15, 'bold'))
        pass_label.grid(row=4, column=0, sticky='w', padx=10, pady=18)

        self.pass_entry = Entry(self.window, width=37, bg= '#d5bdaf', fg='black', font=('Arial', 13, 'bold'), show='*')
        self.pass_entry.grid(row=5, column=0, sticky='w', padx=15, pady=2)

        login_btn = Button(self.window, text='Login', bg='#1B263B', fg='#E4D6C3', font=('Arial', 20, 'bold'), padx=25, activebackground='#669bbc', command= self.save)
        login_btn.grid(row=6, column=0, pady=10)

        link_font = font.Font(underline=TRUE, family='Arial', size=18, weight='bold')

        sign_label = Button(self.window, text='Sign Up', bg='#E4D6C3', fg= '#1B263B', font=link_font, cursor='hand2', command=self.open_signup, borderwidth=0, activebackground='#E4D6C3')
        sign_label.grid(row=7, column=0)

    def scan_details(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        detector = cv2.QRCodeDetector()

        while True:
            ret, frame = cap.read()
            data, bbox, _ = detector.detectAndDecode(frame)

            if data:

                if self.details(data):
                    self.open_app(self.window, self.user_name)
                    messagebox.showinfo('Success', 'Logged in Successfully!')
                    break   

            cv2.imshow("QR Scanner", frame)

            if cv2.waitKey(1) == 27:   
                break

        cap.release()
        cv2.destroyAllWindows()

    def details(self, data):
        data = data.strip()
        if ':' not in data:
            messagebox.showerror('Invalid!', 'Please Scan Valid Student QR!')
            return False
        
        split_data = data.split(':')

        if len(split_data) != 2:
            messagebox.showerror('Inavlid!', 'Please Scan Valid Student QR!')
            return False
        
        username = split_data[0].strip()
        enrollment = split_data[1].strip()

        self.user_name = username

        if not enrollment.isdigit():
            messagebox.showerror('Invalid!', 'Invalid Enrollment Number!')
            return False
        

        check = database.search_student(username, enrollment)

        if check == False:
            messagebox.showwarning('Invalid', 'Student Account Not Found!')
            return False
        elif check == True:
            return True




class Sign_Up:
    def __init__(self, parent):
        self.parent = parent
        self.parent.withdraw()

        self.window = Toplevel(parent)
        self.window.title('Library Management System')
        self.window.minsize(380,500)
        self.window.maxsize(380,500)
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

        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def _set_ui(self):

        heading_label = Label(self.window, text='Student SignUp',  font=('Arial', 28, 'bold'), bg='#E4D6C3', fg='#1B263B')
        heading_label.grid(row=0, column=0, pady=15, padx=50)

        scan_btn = Button(self.window, text='Scan Student Details', font=('Arial', 16, 'bold'), bg='#1B263B', fg='#E4D6C3', padx=10, pady=6, command=self.scan_details)
        scan_btn.grid(row=1, column=0)

        user_label = Label(self.window, text='Username : ', font=('Arial', 17, 'bold'), bg='#E4D6C3', fg='#1B263B')
        user_label.grid(row=2, column=0, padx=10,pady=18, sticky='w')

        self.user_entry = Entry(self.window, width=37, readonlybackground= '#d5bdaf', fg='black', font=('Arial', 13, 'bold'), state='readonly')
        self.user_entry.grid(row=3, column=0, sticky='w', padx=15, pady=2) 

        user_enrol = Label(self.window, text='Enrollment : ', font=('Arial', 17, 'bold'), bg='#E4D6C3', fg='#1B263B')
        user_enrol.grid(row=4, column=0, padx=10,pady=18, sticky='w')

        self.enrol_entry = Entry(self.window, width=37, readonlybackground= '#d5bdaf', fg='black', font=('Arial', 13, 'bold'), state='readonly')
        self.enrol_entry.grid(row=5, column=0, sticky='w', padx=15, pady=2)

        pass_label = Label(self.window, text='Create Password : ', bg='#E4D6C3', fg='#1B263B', font=('Arial', 17, 'bold'))
        pass_label.grid(row=6, column=0, sticky='w', padx=10, pady=18)

        self.pass_entry = Entry(self.window, width=37, bg= '#d5bdaf', fg='black', font=('Arial', 13, 'bold'))
        self.pass_entry.grid(row=7, column=0, sticky='w', padx=15, pady=2)

        create_btn = Button(self.window, text='Create Account', bg='#1B263B', fg='#E4D6C3', font=('Arial', 17, 'bold'), padx=18, activebackground='#669bbc', command=self.save)
        create_btn.grid(row=8, column=0, pady=25)
    
    def save(self):
        
        user_name = self.user_entry.get()
        password = self.pass_entry.get()
        enrollment = self.enrol_entry.get()
        role = 'student'

        database.add_user(user_name, enrollment,password,role)

        self.on_close()
        messagebox.showinfo('Success', 'Student Account Created Successfully!')

    def scan_details(self):

        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        detector = cv2.QRCodeDetector()

        while True:
            ret, frame = cap.read()
            data, bbox, _ = detector.detectAndDecode(frame)

            if data:

                if self.add_details(data):
                    break   

            cv2.imshow("QR Scanner", frame)

            if cv2.waitKey(1) == 27:   
                break

        cap.release()
        cv2.destroyAllWindows()

    def add_details(self, data):
        data = data.strip()
        if ':' not in data:
            messagebox.showerror('Invalid!', 'Please Scan Valid Student QR!')
            return False
        
        split_data = data.split(':')

        if len(split_data) != 2:
            messagebox.showerror('Inavlid!', 'Please Scan Valid Student QR!')
            return False
        
        student_name = split_data[0].strip()
        student_enroll = split_data[1].strip()

        if not student_enroll.isdigit():
            messagebox.showerror('Invalid!', 'Invalid Enrollment Number!')
            return False
        
        self.user_entry.config(state='normal')
        self.enrol_entry.config(state='normal')
        
        self.user_entry.delete(0, END)
        self.enrol_entry.delete(0, END)

        self.user_entry.insert(0,student_name)
        self.enrol_entry.insert(0,student_enroll)

        self.user_entry.config(state='readonly')
        self.enrol_entry.config(state='readonly')

        return True
        



        









# from tkinter import * 
# from tkinter import font
# import student_gui



# def start_app(parent):
#     parent.withdraw()

#     student_login = Toplevel(parent)

#     def on_close():
#         student_login.destroy()
#         parent.deiconify()   # show main window again

#     student_login.protocol("WM_DELETE_WINDOW", on_close)

#     student_login.minsize(360,400)
#     student_login.maxsize(360,400)
#     student_login.config(bg= "#E4D6C3")

#     student_login.update_idletasks()
#     width = student_login.winfo_width()
#     height = student_login.winfo_height()
    
#     x = (student_login.winfo_screenwidth() // 2) - (width // 2)
#     y = (student_login.winfo_screenheight() // 2) - (height // 2)
#     student_login.geometry(f'{width}x{height}+{x}+{y}')


#     def open_signup():
#         print('Sign Up')

#     def open_app(parent):
#         student_gui.start_app(parent)

#     title_lbl = Label(student_login, text='Student Login', font=('Arial', 28, 'bold'), bg='#E4D6C3', fg='#1B263B')
#     title_lbl.grid(row=0, column=0, padx= 55, pady=15)

#     user_label = Label(student_login, text='Enter Username : ', font=('Arial', 15, 'bold'), bg='#E4D6C3', fg='#1B263B')
#     user_label.grid(row=1, column=0, padx=10,pady=18, sticky='w')

#     user_entry = Entry(student_login, width=55, bg= '#d5bdaf', fg='black')
#     user_entry.grid(row=2, column=0, sticky='w', padx=15, pady=2) 

#     pass_label = Label(student_login, text='Enter Password : ', bg='#E4D6C3', fg='#1B263B', font=('Arial', 15, 'bold'))
#     pass_label.grid(row=3, column=0, sticky='w', padx=10, pady=18)

#     pass_entry = Entry(student_login, width=55, bg= '#d5bdaf', fg='black')
#     pass_entry.grid(row=4, column=0, sticky='w', padx=15, pady=2)

#     login_btn = Button(student_login, text='Login', bg='#1B263B', fg='#E4D6C3', font=('Arial', 20, 'bold'), padx=40, activebackground='#669bbc', command= lambda: open_app(student_login))
#     login_btn.grid(row=5, column=0, pady=20)

#     link_font = font.Font(underline=TRUE, family='Arial', size=18, weight='bold')

#     sign_label = Label(student_login, text='Sign Up', bg='#E4D6C3', fg= '#1B263B', font=link_font, cursor='hand2')
#     sign_label.grid(row=6, column=0)
#     sign_label.bind("<Button-1>", lambda e: open_signup())

