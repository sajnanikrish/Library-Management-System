import database
from tkinter import *
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from collections import defaultdict
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Dashboard:
    def __init__(self, dashboard_frame):
        self.dashboard_frame = dashboard_frame
        self._set_frames()
        self._first_frame()
        self._second_frame()
        self._third_frame()
        self._fourth_frame()

    def _set_frames(self):
        self.first_frame = Frame(self.dashboard_frame, bg='#F5F0E6')
        self.first_frame.grid(row=0,column=0, padx=10, pady=10, sticky='nsew')
        # self.first_frame.grid_propagate(False)

        self.second_frame = Frame(self.dashboard_frame, bg='#F5F0E6')
        self.second_frame.grid(row=0,column=1, padx=10, pady=10, sticky='nsew')
        # self.second_frame.grid_propagate(False)

        self.third_frame = Frame(self.dashboard_frame, bg='#F5F0E6')
        self.third_frame.grid(row=1,column=0, padx=10, pady=10, sticky='nsew')
        # self.third_frame.grid_propagate(False)

        self.fourth_frame = Frame(self.dashboard_frame, bg='#F5F0E6')
        self.fourth_frame.grid(row=1,column=1, padx=10, pady=10, sticky='nsew')
        # self.fourth_frame.grid_propagate(False)

    def _first_frame(self):

        data = database.get_books()
        book_titles = 0
        for i in data:
            book_titles+=1

        quant_list = []
        for i,quant in enumerate(data):
            quant = quant[-1]
            quant_list.append(quant)

        total_books = sum(quant_list)
        issued_book_data = database.get_issued_books()
        issued_books = len(issued_book_data)
        avail_books = total_books - issued_books


        fig, ax = plt.subplots(figsize=(4,3))
        fig.patch.set_facecolor('#F5F0E6')
        ax.set_facecolor('#F5F0E6')
        fig.text(0.5,0.92,'Library Book Summary', ha='center', fontsize=12, weight='bold', family = 'Arial')
        fig.subplots_adjust(left=0,right=1,top=1,bottom=0)

        ax.set_title('Library Book Summary')
        

        ax.axis('off')

        ax.text(0.25, 0.7, f"{book_titles}", fontsize=25, ha='center')
        ax.text(0.25, 0.6, "Total Titles", ha='center', fontsize = 13)

        ax.text(0.75, 0.7, f"{total_books}", fontsize=25, ha='center',)
        ax.text(0.75, 0.6, "Total Books", ha='center',fontsize = 13)

        ax.text(0.25, 0.3, f"{issued_books}", fontsize=25, ha='center')
        ax.text(0.25, 0.2, "Issued Books", ha='center',fontsize = 13)

        ax.text(0.75, 0.3, f"{avail_books}", fontsize=25, ha='center')
        ax.text(0.75, 0.2, "Available Books", ha='center',fontsize = 13)

        for spine in ax.spines.values():
            spine.set_visible(False)

        canvas = FigureCanvasTkAgg(fig, master = self.first_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both',expand=True)

    def _second_frame(self):

        issued_data = database.get_issued_books()

        today = datetime.today()
        last_7_days = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(6, -1, -1)]

        count_dict = defaultdict(int)

        for record in issued_data:
            issue_date = record[4]  
            if issue_date in last_7_days:
                count_dict[issue_date] += 1

        
        labels = [datetime.strptime(d, "%Y-%m-%d").strftime("%a") for d in last_7_days]
        values = [count_dict[day] for day in last_7_days]
        

        fig, ax = plt.subplots(figsize=(4,3))

        ax.bar(labels,values, color="#4A7BA7")
        ax.set_title('Books issued in last 7 days', weight='bold', family = 'Arial')
        ax.title.set_color('#1B263B')
        fig.patch.set_facecolor('#F5F0E6')
        ax.set_facecolor('#F5F0E6')
        
        for i, v in enumerate(values):
            if v > 0:
                ax.text(i, v, str(v), ha='center')

        for spine in ax.spines.values():
            spine.set_visible(False)

        canvas = FigureCanvasTkAgg(fig, master=self.second_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both',expand=True)


    def _third_frame(self):

        data = database.get_popular_books()

        top5 = data[:5]
        labels = [i[1][1] for i in top5]
        values = [i[1][0] for i in top5]

        labels = labels[::-1]
        values = values[::-1]
        
        def split_title(title):
            words = title.split()
            if len(words) > 1:
                return words[0] + "\n" + " ".join(words[1:])
            return title

        labels = [split_title(t) for t in labels]
        
        fig, ax = plt.subplots(figsize=(5,3))
        fig.subplots_adjust(left=0.15)

        ax.barh(labels,values, color="#4A7BA7")
        ax.set_title('Top 5 Issued Books', family = 'Arial', weight='bold')
        ax.title.set_color('#1B263B')     
        fig.patch.set_facecolor('#F5F0E6')
        ax.set_facecolor('#F5F0E6')   

        for i, v in enumerate(values):
            ax.text(v, i, str(v), va='center')

        for spine in ax.spines.values():
            spine.set_visible(False)

        canvas = FigureCanvasTkAgg(fig, master=self.third_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both',expand=True)


    def _fourth_frame(self):
        data = database.get_popular_books()

        top5 = data[:5]
        others = data[5:]

        top_counts = sum([i[1][0] for i in top5])
        other_counts = sum([i[1][0] for i in others])

        fig, ax = plt.subplots(figsize=(4,3))

        labels = ['Top 5', 'Others']
        values = [top_counts, other_counts]

        ax.pie(values, labels=labels, autopct='%1.1f%%', colors=["#4A7BA7", "#A3C4BC"], startangle=90)

        ax.set_title("Top 5 vs Others", family = 'Arial', weight='bold')
        ax.title.set_color('#1B263B')
        fig.patch.set_facecolor('#F5F0E6')
        ax.set_facecolor('#F5F0E6')

        for spine in ax.spines.values():
            spine.set_visible(False)

        canvas = FigureCanvasTkAgg(fig, master=self.fourth_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both',expand=True)


