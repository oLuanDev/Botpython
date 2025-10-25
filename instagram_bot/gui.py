import customtkinter
from tkinter import messagebox
from bot import InstagramBot

# Set the appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class InstagramBotGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Instagram Account Creator")
        self.geometry("400x380")

        # Create a frame for the widgets
        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Title Label
        self.title_label = customtkinter.CTkLabel(self.frame, text="Create Instagram Account", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.title_label.pack(pady=12, padx=10)

        # Entry fields
        self.email_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Email")
        self.email_entry.pack(pady=12, padx=10)

        self.fullname_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Full Name")
        self.fullname_entry.pack(pady=12, padx=10)

        self.username_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        # Create account button
        self.create_button = customtkinter.CTkButton(self.frame, text="Create Account", command=self.create_account)
        self.create_button.pack(pady=12, padx=10)

        # Disclaimer
        self.disclaimer_label = customtkinter.CTkLabel(self.frame, text="Note: Automating account creation is against Instagram's terms of service.\nThis bot is for educational purposes and may not succeed.", font=customtkinter.CTkFont(size=9), text_color="gray")
        self.disclaimer_label.pack(pady=(10, 0), padx=10)


    def create_account(self):
        email = self.email_entry.get()
        fullname = self.fullname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not all([email, fullname, username, password]):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            self.create_button.configure(state="disabled", text="Creating...")
            self.update_idletasks() # Update the GUI to show the change

            bot = InstagramBot()
            bot.create_account(email, fullname, username, password)
            bot.close_browser()

            messagebox.showinfo("Success", "Account created successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.create_button.configure(state="normal", text="Create Account")


if __name__ == "__main__":
    app = InstagramBotGUI()
    app.mainloop()
