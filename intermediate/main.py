import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("300x200")
tk.Label(root, text="Hello World!", font=("Arial", 18)).pack(pady=20)
root.mainloop()
