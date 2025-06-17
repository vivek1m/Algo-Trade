# this is first GUI
import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter import ttk
import SecondGUI
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser, simpledialog, font

class FirstGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.geometry("900x600")
        self.minsize(900, 600)
        self.title("Welcome To Algo Trader")
        self.config(bg="#ffffff")
        self.create_ui()

    def create_ui(self):
        self.make_header()
        self.make_disclaimer()
        self.make_footer()

    def make_header(self):
        header_frame = tk.Frame(self, bg="#1F4E79")
        header_frame.pack(fill="x", pady=5)

        title = tk.Label(
            header_frame,
            text="Welcome To Algo Trader",
            font="Helvetica 26 bold",
            bg="#1F4E79",
            fg="white"
        )
        title.pack(pady=10)

        subtitle = tk.Label(
            header_frame,
            text="Your Personal Stock Market Assistant",
            font="Helvetica 16 italic",
            bg="#1F4E79",
            fg="white"
        )
        subtitle.pack()

    def make_disclaimer(self):
        disclaimer_frame = tk.Frame(self, bg="#f9f9f9", bd=2, relief="groove")
        disclaimer_frame.pack(pady=20, fill="x", padx=15)

        disclaimers = [
            "Investments in Stock Markets are subject to market risks as well as at your own risk.",
            "WE ARE NOT RESPONSIBLE FOR ANY LOSSES OR PROFITS DUE TO USAGE OF THIS SOFTWARE.",
            "Please Read All Scheme Related Documents Carefully."
        ]
        colors = ["#333333", "#D32F2F", "#333333"]

        for i, text in enumerate(disclaimers):
            tk.Label(
                disclaimer_frame,
                text=text,
                font="Helvetica 14",
                bg="#f9f9f9",
                fg=colors[i],
                wraplength=850,
                justify="left"
            ).pack(anchor="w", padx=20, pady=5)

        self.make_terms_and_conditions(disclaimer_frame)

    def make_terms_and_conditions(self, parent_frame):
        terms_frame = tk.Frame(parent_frame, bg="#f9f9f9")
        terms_frame.pack(pady=20)

        def on_check():
            chbox["fg"] = "green" if all(var.get() == 1 for var in self.cbVar) else "red"

        terms = [
            "I agree to the Terms and Conditions",
            "I acknowledge that investments in stock markets involve risks",
            "I consent to the collection and use of my data according to the privacy policy",
            "I understand that the software is not responsible for any financial losses or damages",
            "I agree to comply with all applicable laws and regulations while using this software",
            "I acknowledge that this software is a tool for market analysis and not investment advice"
        ]
        large_terms = [
            "AGREEMENT TO TERMS OF SERVICE IS REQUIRED BEFORE USING THIS SOFTWARE.",
            "UNDERSTANDING RISKS: STOCK MARKET INVESTMENTS CAN BE HIGHLY VOLATILE AND RISKY."
        ]

        colors = ["red"] * len(terms)
        
        self.cbVar = []
        
        for term in large_terms:
            tk.Label(
                terms_frame,
                text=term,
                font="Helvetica 16 bold",
                bg="#f9f9f9",
                fg="blue",
                wraplength=850,
                justify="left"
            ).pack(anchor="w", padx=20, pady=10)
        
        for i, text in enumerate(terms):
            var = tk.IntVar()
            self.cbVar.append(var)
            chbox = tk.Checkbutton(
                terms_frame,
                variable=var,
                text=terms[i],
                command=on_check,
                fg=colors[i],
                bg="#f9f9f9",
                font="Helvetica 12"
            )
            chbox.pack(anchor="w", padx=20, pady=5)

        submit_button = tk.Button(
            terms_frame,
            text="Submit",
            font="Helvetica 14 bold",
            bg="#007ACC",
            fg="white",
            activebackground="#005f73",
            activeforeground="white",
            borderwidth=3,
            relief=tk.RAISED,
            padx=25,
            pady=10,
            command=self.submission
        )
        submit_button.pack(pady=15)

    def make_footer(self):
        footer_frame = tk.Frame(self, bg="#1F4E79")
        footer_frame.pack(side="bottom", fill="x", pady=5)

        tk.Label(
            footer_frame,
            text="Crafted with precision by Vivek Sharma & Pranay Roakade",
            font="Helvetica 12",
            bg="#1F4E79",
            fg="white"
        ).pack(pady=5)

    def submission(self):
        if any(var.get() == 0 for var in self.cbVar):
            tkmsg.showerror(title="Warning", message="Please accept all the Terms and Conditions")
        else:
            self.destroy()
            second = SecondGUI.SecondGUI()
            second.mainloop()

if __name__ == "__main__":
    app = FirstGUI()
    app.mainloop()
