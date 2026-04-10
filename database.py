import sqlite3
import re, os, qrcode
from PIL import Image, ImageDraw, ImageFont
from datetime import date, timedelta, datetime
# from tkcalendar import DateEntry

DB_NAME = "library.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                quant INTEGER
                )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS issued_books (
                issued_book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                stud_name TEXT,
                stud_enrol INTEGER,
                book_name TEXT,
                book_author TEXT,
                iss_date TEXT,
                iss_days INTEGER,
                due_date TEXT
                )""")
    
    
    cur.execute("""CREATE TABLE IF NOT EXISTS user_data (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL,
                enrollment INTEGER,
                password TEXT NOT NULL,
                role TEXT CHECK(role IN ('admin','student')) NOT NULL
                )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS issue_history(
                book_id INTEGER,
                enrol INTEGER,
                stud_name TEXT NOT NULL,
                book_name TEXT NOT NULL,
                book_author TEXT NOT NULL,
                issue_date TEXT,
                return_date TEXT,
                fine INTEGER
                )""")
    
    # cur.execute("DROP TABLE issue_history")
    
    conn.commit()
    conn.close()

def add_user(user_name, enrollment, password, role):
    conn = connect()
    cur = conn.cursor()

    enroll = int(enrollment)
    cur.execute("INSERT INTO user_data(user_name, enrollment, password, role) VALUES (?,?,?,?)",
                (user_name, enroll, password, role)
    )
    conn.commit()
    conn.close()

def get_user(user_name, role):

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT password, enrollment, user_id FROM user_data WHERE user_name = ? AND role = ? ", (user_name,role))
    result = cur.fetchone()
    conn.close()

    if result:
        return result 
    else:
        return None
    
def search_student(username, enrollment):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM user_data WHERE user_name = ? AND enrollment = ?",
                (username, enrollment))
    result = cur.fetchone()

    if result:
        return True
    else:
        return False 

def add_admin(user_name, password, role):
    conn = connect()
    cur = conn.cursor()

    enroll = None 
    cur.execute("INSERT INTO user_data(user_name, enrollment ,password, role) VALUES (?,?,?,?)",
                (user_name, enroll,password, role)
    )
    conn.commit()
    conn.close()


def get_admin(admin_name, role):

    
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT password FROM user_data WHERE user_name = ? AND role = ? ", (admin_name,role ))
    result = cur.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return None
    
def admin_exists():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM user_data WHERE role = 'admin'")
    exists = cur.fetchone() is not None

    conn.close()
    return exists


def get_book_details(book_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT title, author FROM books WHERE book_id = ? ", (book_id, ))
    data = cur.fetchone()
    conn.close()

    return data 

def add_book(title, author, quant):
    conn = connect()
    cur = conn.cursor()

    cur.execute("INSERT INTO books(title, author, quant) VALUES (?,?,?)",
                (title, author, quant)
    ) 
    conn.commit()
    book_id = cur.lastrowid
    conn.close()

    generate_qr(book_id, title)


def clean_book_name(text):
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = text.replace(' ', '_')

    return text

def generate_qr(book_id, title):
    os.makedirs("qrcodes", exist_ok=True)

    # 🔹 Clean title for safe file name
    def clean_book_name(name):
        return "".join(c for c in name if c.isalnum() or c in (" ", "_")).rstrip()

    safe_title = clean_book_name(title)

    qr_data = f"BOOK_{book_id}"
    file_name = f"BOOK_{book_id}_{safe_title}.png"
    file_path = os.path.join("qrcodes", file_name)

    # If already exists, skip
    if os.path.exists(file_path):
        return

    # 1️⃣ Generate QR
    qr = qrcode.make(qr_data).convert("RGB")

    # 2️⃣ Load Font
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()

    width, height = qr.size
    text = f"BOOK_{book_id} | {title}"

    # 3️⃣ Wrap Text Properly
    temp_img = Image.new("RGB", (width, height), "white")
    temp_draw = ImageDraw.Draw(temp_img)

    max_width = width - 20  # little margin
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if temp_draw.textlength(test_line, font=font) <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())

    # 4️⃣ Create Bigger Image
    line_height = font.size + 5
    new_height = height + (line_height * len(lines)) + 20

    new_img = Image.new("RGB", (width, new_height), "white")
    new_img.paste(qr, (0, 0))

    # 5️⃣ Draw Wrapped Text
    draw = ImageDraw.Draw(new_img)
    y_text = height + 10

    for line in lines:
        text_width = draw.textlength(line, font=font)
        text_x = (width - text_width) // 2
        draw.text((text_x, y_text), line, fill="black", font=font)
        y_text += line_height

    # 6️⃣ Save Final Image
    new_img.save(file_path)


def generate_qr_for_existing_books():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    cur.execute("SELECT book_id, title FROM books")
    books = cur.fetchall()

    conn.close()

    for book_id, title in books:
        generate_qr(book_id, title)


def get_books():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT book_id, title, author, quant FROM books")
    data = cur.fetchall()
    conn.close() 

    return data 

def add_quantity(amt, id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT quant FROM books WHERE book_id = ?", (id,))
    result = cur.fetchone()
    
    if result is None:
        conn.close()
        return False
    else:
        if amt <= 0:
            return "Negative quantity cannot be added."
        else:
            cur.execute("UPDATE books SET quant = quant + ?  WHERE book_id = ?",
                        (amt,id)
            )
            conn.commit()
        conn.close()

def remv_quantity(amt, id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT quant FROM books WHERE book_id = ?", (id,))
    result = cur.fetchone()
    
    if result is None:
        return "No book found with this ID"

    if amt <= 0:
        return "Please enter positive value."
    else:

        ans = result[0] - amt
        if ans < 0:
            return "Remove Quantity cannot be greater than available books quantity."
        else:
            cur.execute("UPDATE books SET quant = quant - ?  WHERE book_id = ?",
                        (amt,id)
            )
            conn.commit()
    conn.close()


def issue_book(book_id,stud_name,stud_enrol, book_name, book_author,iss_date,iss_days):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT quant FROM books WHERE book_id = ?", (book_id,))
    result = cur.fetchone()

    stud_enrol_int = int(stud_enrol)

    if result is None:
        return "No Book found with this ID."
    elif result[0] <= 0:
        return "Book not available."
    else:
        current_date = iss_date
        due_date = current_date + timedelta(days = int(iss_days))

        cur.execute("INSERT INTO issued_books (book_id,stud_name,stud_enrol, book_name, book_author,iss_date,iss_days, due_date) VALUES (?,?,?,?,?,?,?,?)",
                    (book_id,stud_name,stud_enrol_int, book_name, book_author,iss_date,iss_days,due_date)
        )

        cur.execute("UPDATE books SET quant = quant - 1 WHERE book_id = ?",
                    (book_id, )
        )
    conn.commit()
    conn.close()


def get_book_ids():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT book_id from books")
    result = cur.fetchall()
    conn.close()
    return result


def book_quantity(book_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT quant FROM books WHERE book_id = ?",
                (book_id, ))
    result = cur.fetchone()
    conn.close()

    return result


def return_book(book_id, stud_enrol, stud_name, book_name, book_author, fine):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM issued_books WHERE book_id = ? AND stud_enrol = ?", (book_id, stud_enrol))
    result = cur.fetchone()

    if result is None:
        conn.close()
        return False
    
    issued_date = get_issued_date(book_id, stud_name, stud_enrol)
    return_date = date.today()

    split_fine = fine.split(" ")
    fine_amount = int(split_fine[0])

    cur.execute("""INSERT INTO issue_history (book_id, enrol, stud_name, book_name, book_author, issue_date, return_date, fine) VALUES (?,?,?,?,?,?,?,?)""",
                (book_id,stud_enrol,stud_name,book_name,book_author,issued_date[0],return_date,fine_amount)
    )
    
    cur.execute("DELETE FROM issued_books WHERE book_id = ? AND stud_enrol = ?",
                (book_id,stud_enrol)
    )

    cur.execute("UPDATE books SET quant = quant + 1 WHERE book_id = ?",
                (book_id,)
    )

    conn.commit()
    conn.close()
    return True


def get_issued_date(book_id, stud_name, stud_enrol):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT iss_date FROM issued_books WHERE book_id = ? AND stud_name = ? and stud_enrol = ?",
                (book_id, stud_name, stud_enrol))
    data = cur.fetchone()
    conn.close()

    return data 

def get_issued_books():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT issued_book_id, book_id, stud_name, stud_enrol, iss_date, iss_days FROM issued_books")
    data = cur.fetchall()
    conn.close()

    return data

def issue_history(stud_enrol,stud_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""SELECT book_id, book_name, book_author, issue_date, return_date, fine FROM issue_history WHERE enrol = ? AND stud_name = ?""",
                (stud_enrol, stud_name)
    )

    result = cur.fetchall()
    conn.close()

    return result or []
    

def get_current_issued_books(stud_enrol, stud_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT book_id,due_date FROM issued_books WHERE stud_enrol = ? AND stud_name = ?", 
                (stud_enrol,stud_name))
    result = cur.fetchall()
    conn.close()

    if result:
        return result
    else:
        return 0


def fine_paid_by_student(stud_name, stud_enrol):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT fine FROM issue_history WHERE stud_name = ? AND enrol = ?",
                (stud_name, stud_enrol))
    result = cur.fetchall()
    conn.close()

    if result:
        return result
    else:
        return 0


def calculate_fine(book_id, stud_name,stud_enroll): 
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT iss_date, iss_days FROM issued_books WHERE book_id = ? AND stud_name = ? AND stud_enrol = ?",
                (book_id, stud_name, stud_enroll))
    result = cur.fetchone()

    if result:

        issued_date = result[0]
        issued_days = result[1]

        days = (date.today() - date.fromisoformat(issued_date)).days

        if days > issued_days:
            conn.close()
            return days - issued_days
        else:
            conn.close()
            return False
        
    else:
        return None 

def books_issued_in_history(stud_enrol, stud_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT enrol,stud_name,book_name, book_author, issue_date, return_date FROM issue_history WHERE enrol = ? AND stud_name = ?", 
                (stud_enrol, stud_name))
    result = cur.fetchall()

    return result or []



def student_book_issued(enrollment):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT issued_book_id,book_id,book_name,book_author,iss_date, due_date FROM issued_books WHERE stud_enrol = ?", 
                (enrollment, ))
    result = cur.fetchall()

    return result or []

def recent_activities(stud_enrol, stud_name):
    
    activities = []
    issued = student_book_issued(stud_enrol)
    issued_history = books_issued_in_history(stud_enrol,stud_name)
    history = issue_history(stud_enrol,stud_name)
    # print(history)
    # print(issued)

    if issued_history:
        issued.extend(issued_history)
        # print(issued)
    
   
    for i in issued:
        book_name = i[2]
        issue_date = i[4]

        activities.append((issue_date,f"Issued '{book_name}'"))

    for i in history:
        book_name = i[1]
        return_date = i[4]
        fine = i[-1]

        activities.append((return_date, f"Returned '{book_name}'"))

        if fine and fine > 0:
            activities.append((return_date, f"Fine Rs.{fine} for {book_name}"))

    def parse_date(d):
        try:
            return datetime.strptime(d, "%d-%m-%Y")
        except:
            try:
                return datetime.fromisoformat(d)
            except:
                return datetime.min

    if not activities:
        return None

    activities.sort(key=lambda x: parse_date(x[0]), reverse=True)
    # print(activities)
    recent = activities[:5]
    recents = [i[1] for i in recent]
    
    return recents
    

# recent_activities(240170117059, "KRISH GURMUKHDAS SAJNANI")


def search_book(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT title, author FROM books WHERE title LIKE ?",
                ('%'+value+'%', )) 
    

    result = cur.fetchall()
    conn.close()

    if result:
        return result
    else:
        return None 
    

# search_book('The')
    


# def get_return_dates(stud_enrol,stud_name):
#     conn = connect()
#     cur = conn.cursor()

#     cur.execute("SELECT return_date FROM ")