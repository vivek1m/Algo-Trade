import tkinter as tk
import tkinter.messagebox as tkmsg
import math
from PIL import ImageTk, Image
import pandas as pd
from tkinter import PhotoImage, ttk
import os
import webbrowser
from googlesearch import search
import algo
import SeventhGUI

class FifthGUI(tk.Tk):
    def __init__(self, df, Amount, period, rf):
        print(Amount, rf, period)
        self.Amount = Amount
        self.period = period
        self.rf = rf

        super().__init__()
        self.df = df
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")  # Fullscreen mode
        self.minsize(850, 690)
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())
        self.title("Welcome To Algo Trader")
        
        # Ensure there's a valid stock price data to proceed
        try:
            if self.df.empty or len(self.df.columns) < 3:
                raise ValueError("The stock data format seems incorrect or empty.")
            # Assuming the stock price is in the 3rd-to-last column
            stock_price = self.df.iloc[0, -3]  
            self.no_stocks = math.floor(self.Amount / float(stock_price))
        except IndexError:
            tkmsg.showerror("Error", "The stock data format seems incorrect or empty.")
            self.destroy()
            return
        except ValueError as e:
            tkmsg.showerror("Error", str(e))
            self.destroy()
            return
        
        self.configure_grid()
        self.top()

    def configure_grid(self):
        # Configure the main window grid to expand evenly
        self.grid_rowconfigure(0, weight=1, minsize=100)
        self.grid_rowconfigure(1, weight=3, minsize=100)
        self.grid_columnconfigure(0, weight=1, minsize=100)

    def top(self):
        self.top_frame = tk.Frame(self, bg="indigo")
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Center the text within each label
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Font scaling based on screen size
        font_large = int(screen_width // 80)
        font_medium = int(screen_width // 100)
        
        # Title text
        tk.Label(self.top_frame, text="Name of the recommended Stock :", font=f"Georgia {font_medium} bold", fg="white", bg="indigo", padx=7, pady=7).grid(row=0, column=0, sticky="ew", columnspan=2)
        tk.Label(self.top_frame, text=self.df.iloc[0, 0], font=f"Calibri {font_medium} bold", fg="black", bg="lavender", padx=5, pady=5).grid(row=1, column=0, sticky="ew", columnspan=2)
        tk.Label(self.top_frame, text=f"Latest Stock Price as of {self.df.columns[-3]}:", font=f"Georgia {font_medium} bold", fg="white", bg="indigo", padx=7, pady=7).grid(row=2, column=0, sticky="ew", columnspan=2)
        tk.Label(self.top_frame, text=self.df.iloc[0, -3], font=f"Calibri {font_medium} bold", fg="black", bg="lavender", padx=5, pady=5).grid(row=3, column=0, sticky="ew", columnspan=2)
        tk.Label(self.top_frame, text="Number of Stocks that can be purchased by You:", font=f"Georgia {font_medium} bold", fg="white", bg="indigo", padx=7, pady=7).grid(row=4, column=0, sticky="ew", columnspan=2)
        tk.Label(self.top_frame, text=self.no_stocks, font=f"Calibri {font_medium} bold", fg="black", bg="lavender", padx=5, pady=5).grid(row=5, column=0, sticky="ew", columnspan=2)
        tk.Label(self.top_frame, text="For More Information about the stock, click below:", font=f"Georgia {font_medium} bold", fg="white", bg="indigo", padx=7, pady=7).grid(row=6, column=0, sticky="ew", columnspan=2)

        def searching():
            query = f"{self.df.iloc[0, 0]} yahoo finance"
            try:
                result = list(search(query, num_results=1, lang="en"))
                if result:
                    webbrowser.open(result[0])
                else:
                    tkmsg.showinfo("Info", "No search results found.")
            except Exception as e:
                tkmsg.showerror("Error", f"Error during search: {str(e)}")

        tk.Button(self.top_frame, text="Click Here", command=searching, font=f"Calibri {font_medium} bold", padx=5, pady=5, bg="lavender").grid(row=7, column=0, sticky="ew", columnspan=2)

        self.bottom(screen_width, screen_height)

    def bottom(self, screen_width, screen_height):
        # Using PIL to load the image instead of tk.PhotoImage for more flexibility
        try:
            self.img = Image.open("recommend.png")
            self.img = ImageTk.PhotoImage(self.img)
        except Exception as e:
            print(f"Error loading image: {str(e)}")
            self.img = None

        # Canvas adjusted to fit the window and center the image
        can = tk.Canvas(self, bg="indigo", height=screen_height // 2, width=screen_width)
        can.grid(row=1, column=0, pady=10, sticky="nsew")

        if self.img:
            can.create_image(screen_width // 2, screen_height // 4, image=self.img)  # Center the image on the canvas

        # Creating the next button with proper alignment
        font_button = int(screen_width // 100)
        def submit():
            self.destroy()
            seventh = SeventhGUI.SeventhGUI()
            seventh.mainloop()

        tk.Button(self, text="Next!", font=f"Georgia {font_button} bold", fg="darkred", bg="lightcoral", command=submit, height=1, width=10).grid(row=2, column=5, pady=2, sticky="ew")

if __name__ == "__main__":
    try:
        Amount = 10000
        period = 6
        rf = 5

        # Fetch stock data
        df = algo.algo(Amount, period, rf)

        if df.empty:
            raise ValueError("The stock data returned is empty.")

        # Initialize and run the GUI
        fifth = FifthGUI(df, Amount, period, rf)
        fifth.mainloop()

    except ValueError as e:
        tkmsg.showerror("Error", f"Error: {str(e)}")
    except Exception as e:
        tkmsg.showerror("Error", f"Error occurred: {str(e)}")
