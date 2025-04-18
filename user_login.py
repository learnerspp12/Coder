import tkinter as tk

def main():
    root = tk.Tk()
    root.title("User View")
    root.geometry("600x800")


    # Username label and entry
    tk.Label(root, text="Username:").pack(pady=5)
    # Password label and entry
    tk.Label(root, text="Password:").pack(pady=5)
