from tkinter import *
import cv2




def scan_student():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            break   # 🔥 stop loop after detection

        cv2.imshow("QR Scanner", frame)

        if cv2.waitKey(1) == 27:   # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()
    return data



def scan_book():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        data, bbox, _ = detector.detectAndDecode(frame)

        if data:

            # if add_detail_in_book(data):
            break    # 🔥 stop loop after detection
            

        cv2.imshow("QR Scanner", frame)

        if cv2.waitKey(1) == 27:   # ESC key
            break
          

    cap.release()
    cv2.destroyAllWindows()
    return data 









# def add_detail_in_student(data):
#     data = data.strip()
    # if ':' not in data:
    #     messagebox.showerror('Invalid!', 'Please Scan Valid Student QR!')
    #     return False
    
    # split_data = data.split(':')

    # if len(split_data) != 2:
    #     messagebox.showerror('Inavlid!', 'Please Scan Valid Student QR!')
    #     return False
    
    # student_name = split_data[0].strip()
    # student_enroll = split_data[1].strip()

    # if not student_enroll.isdigit():
    #     messagebox.showerror('Invalid!', 'Invalid Enrollment Number!')
    #     return False
    
    # # self.name_entry.delete(0, END)
    # # self.enroll_entry.delete(0, END)

    # # self.name_entry.insert(0,student_name)
    # # self.name_entry.config(fg='black')

    # # self.enroll_entry.insert(0,student_enroll)
    # # self.enroll_entry.config(fg='black')

    # return data


# def add_detail_in_book(data):

#     if not data.startswith('BOOK_'):
#         messagebox.showerror('Error', 'Wrong QR! Please Scan a Book QR.')
#         return False
    
#     split_data = data.split('_')

#     if len(split_data) != 2:
#         messagebox.showerror('Error', 'Invalid QR Format!')
#         return False

#     book_id = split_data[1]

#     if not book_id.isdigit():
#         messagebox.showerror('Error', 'Invalid Book ID!')
#         return False

#     book_detail = database.get_book_details(book_id)

#     if not book_detail:
#         messagebox.showerror('Error', 'Book Not Found With This Book-Id!')
#         return False
    

#     # self.book_entry.delete(0, END)
#     # self.author_entry.delete(0, END)
#     # self.id_entry.delete(0, END)


#     # self.book_entry.insert(0, book_detail[0])
#     # self.book_entry.config(fg='black')

#     # self.author_entry.insert(0, book_detail[1])
#     # self.author_entry.config(fg='black')

#     # self.id_entry.insert(0, book_id)
#     # self.id_entry.config(fg='black')
    
#     return True