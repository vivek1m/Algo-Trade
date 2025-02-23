# this is the 4th GUI
import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import desired_plot
import SixthGUI

class FourthGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Full screen
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.configure(bg="#f5f5f5")  
        self.title("Welcome To Algo Trader")
        self.make_title()

    def make_title(self):
        tk.Label(self, text="Select the Desired Stock", font=("Arial", 30, "bold"), pady=0, padx=0,
                 fg="white", bg="#34495e").pack(side=tk.TOP, fill=tk.BOTH)
        self.create_frames()

    def create_frames(self):
        self.center_frame = tk.Frame(self, borderwidth=3, relief=tk.FLAT, height=self.winfo_screenheight(), width=self.winfo_screenwidth(), bg="#f5f5f5")
        self.center_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=0, pady=0)
        self.create_canvas()

    def create_canvas(self):
        image = Image.open("C:/Users/HP/OneDrive/Desktop/Stock Market/4.png")
        image = image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
        self.bg_center = ImageTk.PhotoImage(image)

        self.canvas_center = tk.Canvas(self.center_frame, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), highlightthickness=0, bg="white")
        self.canvas_center.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        self.canvas_center.create_image(0, 0, image=self.bg_center, anchor="nw")
        self.drop_down()

    def drop_down(self):
        df_original = pd.read_csv('C:/Users/HP/OneDrive/Desktop/Stock Market/Data.csv')
        df = df_original.copy(True)
        company_names = []

        for i in range(1, len(df)):
            company_names.append(df.iloc[i, 0])

        self.company = tk.StringVar()
        self.company.set("Name of the company")

        style = ttk.Style()
        style.configure("TCombobox",
                        font=("Arial", 16),
                        background="#ecf0f1",
                        foreground="#34495e",
                        selectbackground="#3498db",
                        selectforeground="white")

        combobox_company = ttk.Combobox(self, textvariable=self.company, values=company_names, state='readonly', height=30, width=50, style="TCombobox")
        combobox_company.pack(padx=20, pady=10)

        self.canvas_center.create_text(self.winfo_screenwidth() // 2, 120, text="Select the Stock of Your Choice", font=("Arial", 22, "bold"), fill="white")
        self.canvas_center.create_window(self.winfo_screenwidth() // 2, 170, window=combobox_company)

        self.canvas_center.create_text(self.winfo_screenwidth() // 4, 280, text="Select the Beginning Date", font=("Arial", 22, "bold"), fill="white")

        self.dates = []
        for i in range(1, len(df.columns)):
            self.dates.append(df.columns[i])

        self.begin_date = tk.StringVar()
        self.begin_date.set(df.columns[1])

        combobox_begin = ttk.Combobox(self, textvariable=self.begin_date, values=self.dates, state='readonly', height=30, width=50, style="TCombobox")
        combobox_begin.pack(padx=20, pady=10)
        self.canvas_center.create_window(self.winfo_screenwidth() // 4, 320, window=combobox_begin)

        self.canvas_center.create_text(3 * self.winfo_screenwidth() // 4, 280, text="Select the End Date", font=("Arial", 22, "bold"), fill="white")

        self.end_date = tk.StringVar()
        self.end_date.set(df.columns[-1])

        combobox_end = ttk.Combobox(self, textvariable=self.end_date, values=self.dates, state='readonly', height=30, width=50, style="TCombobox")
        combobox_end.pack(padx=20, pady=10)

        self.canvas_center.create_window(3 * self.winfo_screenwidth() // 4, 320, window=combobox_end)

        def exception_handling():
            begin_index = self.dates.index(self.begin_date.get())
            end_index = self.dates.index(self.end_date.get())
            if begin_index >= end_index:
                tkmsg.showerror(title="Invalid Response", message="Begin Date Needs To Be Before End Date")
            else:
                self.submit()

        b1 = tk.Button(self, text="Continue", font=("Arial", 24, "bold"), command=exception_handling, bg="#2ecc71", fg="white", height=1, width=15, activebackground="#27ae60", borderwidth=3, relief=tk.RAISED)
        
        self.canvas_center.create_window(self.winfo_screenwidth() // 2, 550, window=b1)  # Adjusted vertical position to 550px

    def submit(self):
        c = self.company.get()
        bd = self.begin_date.get()
        ed = self.end_date.get()
        desired_plot.desired_plot(c, bd, ed)
        self.destroy()

        sixth = SixthGUI.SixthGUI(c, bd, ed)
        sixth.mainloop()


if __name__ == "__main__":
    fourth = FourthGUI()
    fourth.mainloop()
# run me 
