import tkinter as tk
import tkinter.messagebox as tkmsg
from PIL import Image, ImageTk
import os
import SecondGUI

class SeventhGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Welcome To Algo Trader")

        self.attributes("-fullscreen", True)
        
        self.canvas_center = None
        self.bg_center = None
        self.create_canvas()

    def create_canvas(self):
        try:
            img_path = "C:/Users/HP/OneDrive/Desktop/Stock Market/final.png"
            print(f"Loading image from: {img_path}")
            
            if os.path.exists(img_path):
                self.bg_image = Image.open(img_path)
            else:
                raise FileNotFoundError(f"Image file '{img_path}' not found.")
        except Exception as e:
            print(f"Error loading image: {e}")
            tkmsg.showerror("Error", f"Failed to load image: {e}")
            return
        
        self.canvas_center = tk.Canvas(self, width=850, height=600, highlightthickness=0)
        self.canvas_center.pack(fill=tk.BOTH, expand=True)

        self.update_background_image()

        self.after(100, self.text)

        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        """Update background image size when the window is resized."""
        self.update_background_image()

    def update_background_image(self):
        """Update the background image based on the current window size."""
        window_width = self.winfo_width()
        window_height = self.winfo_height()

        self.bg_resized = self.bg_image.resize((window_width, window_height), Image.LANCZOS)
        self.bg_center = ImageTk.PhotoImage(self.bg_resized)

        if self.bg_center:
            if not hasattr(self, 'bg_image_on_canvas'):
                self.canvas_center.create_image(0, 0, image=self.bg_center, anchor="nw")
                self.bg_image_on_canvas = True
            else:
                self.canvas_center.itemconfig(self.bg_image_on_canvas, image=self.bg_center)

    def text(self):
        if not hasattr(self, 'text_created'):
            self.canvas_center.create_text(self.winfo_width() // 2, self.winfo_height() // 6, text="THANK YOU FOR CHOOSING ALGO TRADERS\n", font="Georgia 17 bold", fill="white")
            self.canvas_center.create_text(self.winfo_width() // 2, self.winfo_height() // 4, text="Share your experience", font="Georgia 14 bold", fill="white")

            self.FeedBack = tk.StringVar()
            self.feedback_text = tk.Text(self, height=2, width=30, wrap=tk.WORD, font="Georgia 12")  
            self.canvas_center.create_window(self.winfo_width() // 2, self.winfo_height() // 3, window=self.feedback_text) 

            self.feedback_button()

            self.text_created = True

    def feedback_button(self):
        def msg():
            feedback = self.feedback_text.get("1.0", tk.END).strip()  
            if feedback != "":
                tkmsg.showinfo(title="Hope you enjoyed!", message="We will note your response!")
                with open("feedback.txt", "a") as text_file:
                    text_file.write(feedback + "\n")
                self.destroy()
            else:
                tkmsg.showinfo(title="Hope you enjoyed!", message="Please Enter your FeedBack!")

        b2 = tk.Button(self, text="SUBMIT", font="Georgia 8", command=msg, bg="mistyrose", fg="black", height=1, width=15, activebackground="lawngreen", borderwidth=3, relief=tk.RAISED)
        self.canvas_center.create_window(self.winfo_width() // 2, self.winfo_height() // 1.55, window=b2)  

        self.restart()

    def restart(self):
        self.canvas_center.create_rectangle(200, self.winfo_height() // 1.45, self.winfo_width() - 200, self.winfo_height() // 1.35, fill="lightyellow", outline="lightyellow")  # Full background

        self.canvas_center.create_text(self.winfo_width() // 2, self.winfo_height() // 1.4, text="Press the below button to Start Again", font="Georgia 14 bold", fill="black")

        def restarting():
            self.destroy()
            second = SecondGUI.SecondGUI()
            second.mainloop()

        b1 = tk.Button(self, text="Restart Again", font="Georgia 15", command=restarting, bg="mistyrose", fg="black", height=2, activebackground="lawngreen", borderwidth=4, relief=tk.RAISED)
        self.canvas_center.create_window(self.winfo_width() // 2, self.winfo_height() // 1.25, window=b1)  

        self.quit_button()

    def quit_button(self):
        def end():
            self.destroy()

        b1 = tk.Button(self, text="QUIT", font="Georgia 18", command=end, bg="mistyrose", fg="black", height=1, activebackground="lawngreen", borderwidth=3, relief=tk.RAISED, width=15)
        self.canvas_center.create_window(self.winfo_width() // 2, self.winfo_height() // 1.1, window=b1)  

if __name__ == "__main__":
    final = SeventhGUI()
    final.mainloop()
