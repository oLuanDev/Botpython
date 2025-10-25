import tkinter as tk
from tkinter import messagebox
from bot import InstagramBot

class InstagramBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Account Creator")

        # Create and place labels and entry fields
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=0, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        self.fullname_label = tk.Label(root, text="Full Name:")
        self.fullname_label.grid(row=1, column=0, padx=10, pady=5)
        self.fullname_entry = tk.Entry(root)
        self.fullname_entry.grid(row=1, column=1, padx=10, pady=5)

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=2, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=2, column=1, padx=10, pady=5)

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Create and place the create account button
        self.create_button = tk.Button(root, text="Create Account", command=self.create_account)
        self.create_button.grid(row=4, column=0, columnspan=2, pady=10)

    def create_account(self):
        email = self.email_entry.get()
        fullname = self.fullname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not all([email, fullname, username, password]):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            bot = InstagramBot()
            bot.create_account(email, fullname, username, password)
            bot.close_browser()
            messagebox.showinfo("Success", "Account created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstagramBotGUI(root)
    root.mainloop()
