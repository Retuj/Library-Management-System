import tkinter as tk
from tkinter import messagebox

# Main Application class
class LibrarySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x400")

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Library Management System", font=("Arial", 20)).pack(pady=20)

        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")  # Hides the password
        self.password_entry.pack()

        tk.Button(self.root, text="Login as Admin", command=self.admin_login).pack(pady=10)
        tk.Button(self.root, text="Login as User", command=self.user_login).pack()

    def clear_screen(self):
        # Clear the screen before switching views
        for widget in self.root.winfo_children():
            widget.destroy()

    def admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Example of basic validation
        if username == "admin" and password == "admin":
            self.admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials for Admin")

    def user_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Example of basic validation
        if username == "user" and password == "user":
            self.user_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials for User")

    def admin_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.root, text="Add Book", command=self.add_book).pack(pady=10)
        tk.Button(self.root, text="Update Book", command=self.update_book).pack(pady=10)
        tk.Button(self.root, text="Add Membership", command=self.add_membership).pack(pady=10)
        tk.Button(self.root, text="Update Membership", command=self.update_membership).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.create_login_screen).pack(pady=10)

    def user_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="User Dashboard", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.root, text="Search Book", command=self.search_book).pack(pady=10)
        tk.Button(self.root, text="Issue Book", command=self.issue_book).pack(pady=10)
        tk.Button(self.root, text="Return Book", command=self.return_book).pack(pady=10)
        tk.Button(self.root, text="Pay Fine", command=self.pay_fine).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.create_login_screen).pack(pady=10)

    # Placeholder methods for various functionalities
    def add_book(self):
        messagebox.showinfo("Add Book", "Add Book functionality")

    def update_book(self):
        messagebox.showinfo("Update Book", "Update Book functionality")

    def add_membership(self):
        messagebox.showinfo("Add Membership", "Add Membership functionality")

    def update_membership(self):
        messagebox.showinfo("Update Membership", "Update Membership functionality")

    def search_book(self):
        messagebox.showinfo("Search Book", "Search Book functionality")

    def issue_book(self):
        messagebox.showinfo("Issue Book", "Issue Book functionality")

    def return_book(self):
        messagebox.showinfo("Return Book", "Return Book functionality")

    def pay_fine(self):
        messagebox.showinfo("Pay Fine", "Pay Fine functionality")

# Running the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LibrarySystem(root)
    root.mainloop()
