import tkinter as tk
from tkinter.constants import ANCHOR
import tkinter.messagebox as tkmsg
from PIL import ImageTk, Image
import ThirdGUI
import FourthGUI
import os

class SecondGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.state = False
        self.toggle_fullscreen()
        self.config(bg="#e4f1fe")

        self.iconbitmap(r"C:\Users\HP\OneDrive\Desktop\Stock Market\4288596analyticschartgrowthincreasingstocks-115760_115753.ico")
        self.make_title()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.attributes("-fullscreen", self.state)
        self.bind("<Escape>", self.end_fullscreen)
        self.bind("<F11>", self.toggle_fullscreen)
        self.after(100, self.update_layout)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.attributes("-fullscreen", False)
        self.after(100, self.update_layout)
        return "break"

    def update_layout(self):
        width = self.winfo_width()
        height = self.winfo_height()

        if width > 0 and height > 0:
            self.bg_left = Image.open("left.png")
            self.bg_left = self.bg_left.resize((width // 2, height), Image.Resampling.LANCZOS)
            self.bg_left = ImageTk.PhotoImage(self.bg_left)

            self.bg_right = Image.open("right.png")
            self.bg_right = self.bg_right.resize((width // 2, height), Image.Resampling.LANCZOS)
            self.bg_right = ImageTk.PhotoImage(self.bg_right)

            self.canvas_left.config(width=width // 2, height=height)
            self.canvas_right.config(width=width // 2, height=height)

            self.canvas_left.delete("all")
            self.canvas_left.create_image(0, 0, image=self.bg_left, anchor="nw")
            self.canvas_left.create_text(width // 4, height // 6, text="Stock Recommendation Based\non Your Preferences", font="Helvetica 16 bold", fill="white", anchor="center")
            self.canvas_left.create_text(width // 4, height // 5, text="We help you choose the best stocks for your portfolio.", font="Helvetica 12 bold", fill="white", anchor="center")

            self.canvas_right.delete("all")
            self.canvas_right.create_image(0, 0, image=self.bg_right, anchor="nw")
            self.canvas_right.create_text(width // 4, height // 6, text="Analyze Your Stock Choice", font="Helvetica 16 bold", fill="white", anchor="center")
            self.canvas_right.create_text(width // 4, height // 5, text="We help analyze stocks using past performance data", font="Helvetica 12 bold", fill="white", anchor="center")

            self.create_buttons()

    def make_title(self):
        title_frame = tk.Frame(self, bg="#2980b9", height=100)
        title_frame.pack(fill=tk.X)
        tk.Label(title_frame, text="Choose a Functionality", font="Arial 24 bold", pady=30, fg="white", bg="#2980b9").pack(side=tk.TOP, fill=tk.BOTH)

        self.create_frames()

    def create_frames(self):
        self.left = tk.Frame(self, borderwidth=2, relief=tk.FLAT, bg="#ecf0f1")
        self.left.pack(side=tk.LEFT, fill=tk.BOTH, padx=0, pady=0)

        self.right = tk.Frame(self, borderwidth=2, relief=tk.FLAT, bg="#ecf0f1")
        self.right.pack(side=tk.RIGHT, fill=tk.BOTH, padx=0, pady=0)

        self.canvas_left = tk.Canvas(self.left, bg="black", highlightthickness=0)
        self.canvas_left.pack(fill=tk.BOTH, expand=True)

        self.canvas_right = tk.Canvas(self.right, bg="black", highlightthickness=0)
        self.canvas_right.pack(fill=tk.BOTH, expand=True)

        self.create_buttons()

    def create_buttons(self):
        self.canvas_left.create_text(self.winfo_width() // 4, self.winfo_height() // 6, text="Stock Recommendation Based\non Your Preferences", font="Helvetica 16 bold", fill="white", anchor="center")
        self.canvas_left.create_text(self.winfo_width() // 4, self.winfo_height() // 5, text="We help you choose the best stocks for your portfolio.", font="Helvetica 12 bold", fill="white", anchor="center")

        def gui3():
            self.destroy()
            third = ThirdGUI.ThirdGUI()
            third.mainloop()

        b1 = tk.Button(self, text="Start Recommendation", font=("Helvetica", 12, "bold"), command=gui3, bg="#3498db", fg="white", height=2, activebackground="#2980b9", borderwidth=3, relief=tk.RAISED, width=18)
        b1_canvas = self.canvas_left.create_window(self.winfo_width() // 4, self.winfo_height() - 160, window=b1)

        def gui4():
            self.destroy()
            Fourth = FourthGUI.FourthGUI()
            Fourth.mainloop()

        self.canvas_right.create_text(self.winfo_width() // 4, self.winfo_height() // 6, text="Analyze Your Stock Choice", font="Helvetica 16 bold", fill="white", anchor="center")
        self.canvas_right.create_text(self.winfo_width() // 4, self.winfo_height() // 5, text="We help analyze stocks using past performance data", font="Helvetica 12 bold", fill="white", anchor="center")

        b2 = tk.Button(self, text="Continue", font=("Helvetica", 12, "bold"), command=gui4, bg="#3498db", fg="white", height=2, activebackground="#2980b9", borderwidth=3, relief=tk.RAISED, width=18)
        b2_canvas = self.canvas_right.create_window(self.winfo_width() // 4, self.winfo_height() - 160, window=b2)

if __name__ == "__main__":
    app = SecondGUI()
    app.mainloop()
