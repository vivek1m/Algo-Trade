import tkinter as tk
import tkinter.messagebox as tkmsg
from PIL import Image, ImageTk
import algo
import Graph
import FifthGUI
import os
  
class ThirdGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.minsize(850, 600)
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())  
        self.title("Welcome To Algo Trader")
        self.make_title()

    def make_title(self):
        tk.Label(
            self,
            text="Please Enter the Following Details",
            font="CopperplateGothicBold 40 bold", 
            fg="white",
            bg="black",
        ).pack(side=tk.TOP, fill=tk.BOTH)
        self.create_frames()

    def create_frames(self):
        self.center_frame = tk.Frame(
            self, borderwidth=3, relief=tk.FLAT, bg="black"
        )
        self.center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.create_canvas()

    def create_canvas(self):
        image_path = "C:\\Users\\HP\\OneDrive\\Desktop\\Stock Market\\center.png"  
        if not os.path.exists(image_path):
            tkmsg.showerror("Image Error", "Background image not found!")
            self.quit()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        image = Image.open(image_path)
        image = image.resize((screen_width, screen_height), Image.LANCZOS)  
        self.bg_center = ImageTk.PhotoImage(image)

        self.canvas_center = tk.Canvas(
            self.center_frame,
            width=screen_width,
            height=screen_height,
            highlightthickness=0,
            bg="black",
        )
        self.canvas_center.pack(fill=tk.BOTH, expand=True)
        self.canvas_center.create_image(0, 0, image=self.bg_center, anchor="nw")

        self.create_buttons()

    def add_shadowed_text(self, x, y, text, font, fill, shadow_fill="black", shadow_offsets=None):
        if shadow_offsets is None:
            shadow_offsets = [(2, 2), (-2, 2), (2, -2), (-2, -2), (0, 2), (2, 0)]
        for offset_x, offset_y in shadow_offsets:
            self.canvas_center.create_text(x + offset_x, y + offset_y, text=text, font=font, fill=shadow_fill)
        self.canvas_center.create_text(x, y, text=text, font=font, fill=fill)

    def create_buttons(self):
        self.add_shadowed_text(
            self.winfo_screenwidth() // 2,
            self.winfo_screenheight() - 220,  
            text="!!  Make Sure You Enter Proper Details  !!\n",
            font="Georgia 20 bold underline",  
            fill="white",
        )

        def exception_handling():
            if self.amountval.get() == 0.0:
                tkmsg.showwarning(title="Enter Amount", message="Please Enter Amount")
                return
            if self.periodval.get() == 0:
                tkmsg.showwarning(title="Enter Period", message="Please Enter Time Period")
                return
            if self.rfval.get() == 0.0:
                tkmsg.showwarning(title="Enter Risk Factor", message="Please Enter Risk Factor")
                return

            try:
                float(self.amountval.get())
            except ValueError:
                tkmsg.showerror(title="Enter Amount", message="Please Enter Valid Amount")
                return

            try:
                int(self.periodval.get())
            except ValueError:
                tkmsg.showerror(title="Enter Period", message="Please Enter Valid Time Period")
                return

            if float(self.periodval.get()) > 60:
                tkmsg.showinfo(title="Invalid Period", message="Maximum period is 60 months")
                return

            try:
                float(self.rfval.get())
            except ValueError:
                tkmsg.showerror(title="Enter Risk Factor", message="Please Enter Valid Risk Factor")
                return

            if float(self.rfval.get()) > 100:
                tkmsg.showerror(title="Risk Factor Error", message="Risk Factor cannot be more than 100")
                return

            self.submit()

        b1 = tk.Button(
            self,
            text="Continue",
            font="Georgia 15",  
            command=exception_handling,
            bg="mistyrose",
            fg="black",
            height=1,
            activebackground="lawngreen",
            borderwidth=3,
            relief=tk.RAISED,
        )
        b1_canvas = self.canvas_center.create_window(self.winfo_screenwidth() // 2, self.winfo_screenheight() - 150, window=b1)  # Moved further up

        self.add_shadowed_text(self.winfo_screenwidth() // 2, 60, text="Enter the Amount in Rupees\n", font="Georgia 25 bold", fill="white")  # Increased font size
        self.add_shadowed_text(self.winfo_screenwidth() // 2, 100, text="(Amount is the total Capital you want to INVEST)", font="Georgia 15", fill="white")  # Increased vertical spacing
        self.add_shadowed_text(self.winfo_screenwidth() // 2, 200, text="Enter the Time Period in Months\n", font="Georgia 25 bold", fill="white")  # Increased font size
        self.add_shadowed_text(self.winfo_screenwidth() // 2, 240, text="(Time Period is the Duration for which you want to INVEST Your Money)", font="Georgia 15", fill="white")  # Increased vertical spacing
        self.add_shadowed_text(self.winfo_screenwidth() // 2, 350, text="Enter the Risk Factor in Percentage\n", font="Georgia 25 bold", fill="white")  # Increased font size
        self.add_shadowed_text(self.winfo_screenwidth() // 2, 390, text="(Risk Factor is the value on scale 0-100 indicating\n the Maximum loss you can bear on your investment)", font="Georgia 15", fill="white")  # Increased vertical spacing
        self.add_shadowed_text(self.winfo_screenwidth() // 2, self.winfo_screenheight() - 60, text="As of Current Available Data, Maximum Time Period Can Only Be 60 Months ", font="Georgia 15 bold", fill="white")  # Increased font size

        # Entry fields with larger size
        self.amountval = tk.DoubleVar()
        self.periodval = tk.IntVar()
        self.rfval = tk.DoubleVar()

        amountentry = tk.Entry(self, textvariable=self.amountval, relief=tk.FLAT, font="Georgia 15")  # Increased font size
        periodentry = tk.Entry(self, textvariable=self.periodval, relief=tk.FLAT, font="Georgia 15")  # Increased font size
        rfentry = tk.Entry(self, textvariable=self.rfval, relief=tk.FLAT, font="Georgia 15")  # Increased font size

        self.canvas_center.create_window(self.winfo_screenwidth() // 2, 130, window=amountentry)
        self.canvas_center.create_window(self.winfo_screenwidth() // 2, 280, window=periodentry)
        self.canvas_center.create_window(self.winfo_screenwidth() // 2, 440, window=rfentry)  # Moved the percentage input further down

    def submit(self):
        Amount = float(self.amountval.get())
        self.period = int(self.periodval.get())
        self.rf = float(self.rfval.get())
        try:
            d = algo.algo(Amount, self.period, self.rf)
            Graph.plotting(d)
            self.destroy()
            fifth = FifthGUI.FifthGUI(d, Amount, self.period, self.rf)
            fifth.mainloop()
        except Exception as e:
            tkmsg.showerror(
                title="No Stock Found",
                message="No suitable stock was found for the given set of data. Error: " + str(e),
            )

if __name__ == "__main__":
    third = ThirdGUI()
    third.mainloop()
