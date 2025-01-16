import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter import ttk
import SecondGUI

class FirstGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # Initialize the window in fullscreen mode
        self.attributes('-fullscreen', True)
        # Set the default size of the window
        self.geometry("900x600")
        # Set the minimum window size to prevent resizing below this limit
        self.minsize(900, 600)
        # Set the title of the window
        self.title("Welcome To Algo Trader")
        # Set the background color to white for a modern look
        self.config(bg="#ffffff")

        # Call method to create the user interface
        self.create_ui()

    def create_ui(self):
        # Create header, disclaimer, and footer sections
        self.make_header()
        self.make_disclaimer()
        self.make_footer()

    def make_header(self):
        # Create the header frame with a deep blue background
        header_frame = tk.Frame(self, bg="#1F4E79")
        header_frame.pack(fill="x", pady=5)

        # Add the main title label
        title = tk.Label(
            header_frame,
            text="Welcome To Algo Trader",
            font="Helvetica 26 bold",
            bg="#1F4E79",
            fg="white"
        )
        title.pack(pady=10)

        # Add the subtitle label
        subtitle = tk.Label(
            header_frame,
            text="Your Personal Stock Market Assistant",
            font="Helvetica 16 italic",
            bg="#1F4E79",
            fg="white"
        )
        subtitle.pack()

    def make_disclaimer(self):
        # Create a frame for the disclaimer with a light gray background and grooved border
        disclaimer_frame = tk.Frame(self, bg="#f9f9f9", bd=2, relief="groove")
        disclaimer_frame.pack(pady=20, fill="x", padx=15)

        # Disclaimer messages
        disclaimers = [
            "Investments in Stock Markets are subject to market risks as well as at your own risk.",
            "WE ARE NOT RESPONSIBLE FOR ANY LOSSES OR PROFITS DUE TO USAGE OF THIS SOFTWARE.",
            "Please Read All Scheme Related Documents Carefully."
        ]
        # Corresponding text colors
        colors = ["#333333", "#D32F2F", "#333333"]

        # Add each disclaimer message as a label
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

        # Call method to add terms and conditions section
        self.make_terms_and_conditions(disclaimer_frame)

    def make_terms_and_conditions(self, parent_frame):
        # Create a frame for terms and conditions
        terms_frame = tk.Frame(parent_frame, bg="#f9f9f9")
        terms_frame.pack(pady=20)

        def on_check():
            # Change text color to green if all checkboxes are checked, otherwise red
            chbox["fg"] = "green" if all(var.get() == 1 for var in self.cbVar) else "red"

        # Terms that the user must agree to
        terms = [
            "I agree to the Terms and Conditions",
            "I acknowledge that investments in stock markets involve risks",
            "I consent to the collection and use of my data according to the privacy policy",
            "I understand that the software is not responsible for any financial losses or damages",
            "I agree to comply with all applicable laws and regulations while using this software",
            "I acknowledge that this software is a tool for market analysis and not investment advice"
        ]
        # Important terms with bold styling
        large_terms = [
            "AGREEMENT TO TERMS OF SERVICE IS REQUIRED BEFORE USING THIS SOFTWARE.",
            "UNDERSTANDING RISKS: STOCK MARKET INVESTMENTS CAN BE HIGHLY VOLATILE AND RISKY."
        ]

        # Red text color for the regular terms
        colors = ["red"] * len(terms)
        
        self.cbVar = []
        
        # Add important terms as bold labels
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
        
        # Add checkboxes for each term
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

        # Add a submit button
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
        # Create footer frame with deep blue background
        footer_frame = tk.Frame(self, bg="#1F4E79")
        footer_frame.pack(side="bottom", fill="x", pady=5)

        # Add footer label with credits
        tk.Label(
            footer_frame,
            text="Crafted with precision by Vivek Sharma & Pranay Roakade",
            font="Helvetica 12",
            bg="#1F4E79",
            fg="white"
        ).pack(pady=5)

    def submission(self):
        # Show error message if any checkbox is unchecked
        if any(var.get() == 0 for var in self.cbVar):
            tkmsg.showerror(title="Warning", message="Please accept all the Terms and Conditions")
        else:
            # If all checkboxes are checked, close the current window and open SecondGUI
            self.destroy()
            second = SecondGUI.SecondGUI()
            second.mainloop()

if __name__ == "__main__":
    app = FirstGUI()
    app.mainloop()
