import tkinter as tk


def main():
    root = tk.Tk()
    root.title("User View")
    root.geometry("600x800")


    # Create a frame to center the elements
    frame = tk.Frame(root)
    frame.pack(expand=True)  # Center the frame both horizontally and vertically


    # Username label and entry
    tk.Label(frame, text="Username:").pack(pady=5)
    tk.Entry(frame).pack(pady=5)


    # Password label and entry
    tk.Label(frame, text="Password:").pack(pady=5)
    tk.Entry(frame, show="*").pack(pady=5)


    # Login button
    tk.Button(frame, text="Login").pack(pady=10)


    root.mainloop()


if __name__ == "__main__":
    main()
