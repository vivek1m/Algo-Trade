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
        self.config(bg="#e4f1fe")  # Light background color for a soft and professional look

        # Use a proper path for your icon
        self.iconbitmap(r"C:\Users\HP\Downloads\4288596analyticschartgrowthincreasingstocks-115760_115753.ico")

        self.make_title()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.attributes("-fullscreen", self.state)
        self.bind("<Escape>", self.end_fullscreen)  # Allow Escape to exit fullscreen
        self.bind("<F11>", self.toggle_fullscreen)  # Toggle fullscreen with F11
        self.after(100, self.update_layout)  # Wait for the window size to be set
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.attributes("-fullscreen", False)
        self.after(100, self.update_layout)  # Wait for the window size to be set
        return "break"

    def update_layout(self):
        # Ensure the window has non-zero dimensions before proceeding
        width = self.winfo_width()
        height = self.winfo_height()

        if width > 0 and height > 0:
            # Adjust background images to fullscreen
            self.bg_left = Image.open("left.png")
            self.bg_left = self.bg_left.resize((width // 2, height), Image.Resampling.LANCZOS)  # Resize to half the screen width
            self.bg_left = ImageTk.PhotoImage(self.bg_left)

            self.bg_right = Image.open("right.png")
            self.bg_right = self.bg_right.resize((width // 2, height), Image.Resampling.LANCZOS)  # Resize to half the screen width
            self.bg_right = ImageTk.PhotoImage(self.bg_right)

            self.canvas_left.config(width=width // 2, height=height)
            self.canvas_right.config(width=width // 2, height=height)

            # Adjust text and button positions based on window size
            self.canvas_left.delete("all")
            self.canvas_left.create_image(0, 0, image=self.bg_left, anchor="nw")
            self.canvas_left.create_text(width // 4, height // 6, text="Stock Recommendation Based\non Your Preferences", font="Helvetica 16 bold", fill="white", anchor="center")
            self.canvas_left.create_text(width // 4, height // 5, text="We help you choose the best stocks for your portfolio.", font="Helvetica 12 bold", fill="white", anchor="center")
            
            self.canvas_right.delete("all")
            self.canvas_right.create_image(0, 0, image=self.bg_right, anchor="nw")
            self.canvas_right.create_text(width // 4, height // 6, text="Analyze Your Stock Choice", font="Helvetica 16 bold", fill="white", anchor="center")
            self.canvas_right.create_text(width // 4, height // 5, text="We help analyze stocks using past performance data", font="Helvetica 12 bold", fill="white", anchor="center")

            # Re-create buttons only after layout is updated
            self.create_buttons()

    def make_title(self):
        # Title section with a professional look and updated background color
        title_frame = tk.Frame(self, bg="#2980b9", height=100)  # A fresh color for title
        title_frame.pack(fill=tk.X)
        tk.Label(title_frame, text="Choose a Functionality", font="Arial 24 bold", pady=30, fg="white", bg="#2980b9").pack(side=tk.TOP, fill=tk.BOTH)

        self.create_frames()

    def create_frames(self):
        # Create left and right frames with updated colors for aesthetics
        self.left = tk.Frame(self, borderwidth=2, relief=tk.FLAT, bg="#ecf0f1")
        self.left.pack(side=tk.LEFT, fill=tk.BOTH, padx=0, pady=0)

        self.right = tk.Frame(self, borderwidth=2, relief=tk.FLAT, bg="#ecf0f1")
        self.right.pack(side=tk.RIGHT, fill=tk.BOTH, padx=0, pady=0)

        self.canvas_left = tk.Canvas(self.left, bg="black", highlightthickness=0)
        self.canvas_left.pack(fill=tk.BOTH, expand=True)

        self.canvas_right = tk.Canvas(self.right, bg="black", highlightthickness=0)
        self.canvas_right.pack(fill=tk.BOTH, expand=True)

        self.create_buttons()  # Initial button creation during frame setup

    def create_buttons(self):
        # Left Button with centered text on the image (bold text)
        self.canvas_left.create_text(self.winfo_width() // 4, self.winfo_height() // 6, text="Stock Recommendation Based\non Your Preferences", font="Helvetica 16 bold", fill="white", anchor="center")
        self.canvas_left.create_text(self.winfo_width() // 4, self.winfo_height() // 5, text="We help you choose the best stocks for your portfolio.", font="Helvetica 12 bold", fill="white", anchor="center")

        def gui3():
            self.destroy()
            third = ThirdGUI.ThirdGUI()
            third.mainloop()

        # Button on the left side of the window
        b1 = tk.Button(self, text="Start Recommendation", font=("Helvetica", 12, "bold"), command=gui3, bg="#3498db", fg="white", height=2,
                       activebackground="#2980b9", borderwidth=3, relief=tk.RAISED, width=18)
        # Move button up slightly by reducing its Y-position
        b1_canvas = self.canvas_left.create_window(self.winfo_width() // 4, self.winfo_height() - 160, window=b1)  # Adjust button Y to move it up

        def gui4():
            self.destroy()
            Fourth = FourthGUI.FourthGUI()
            Fourth.mainloop()

        # Right Button with centered text on the image (bold text)
        self.canvas_right.create_text(self.winfo_width() // 4, self.winfo_height() // 6, text="Analyze Your Stock Choice", font="Helvetica 16 bold", fill="white", anchor="center")
        self.canvas_right.create_text(self.winfo_width() // 4, self.winfo_height() // 5, text="We help analyze stocks using past performance data", font="Helvetica 12 bold", fill="white", anchor="center")

        # Button on the right side of the window
        b2 = tk.Button(self, text="Continue", font=("Helvetica", 12, "bold"), command=gui4, bg="#3498db", fg="white", height=2,
                       activebackground="#2980b9", borderwidth=3, relief=tk.RAISED, width=18)
        # Move button up slightly by reducing its Y-position
        b2_canvas = self.canvas_right.create_window(self.winfo_width() // 4, self.winfo_height() - 160, window=b2)  # Adjust button Y to move it up

if __name__ == "__main__":
    app = SecondGUI()
    app.mainloop()
