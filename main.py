import tkinter as tk

root = tk.Tk()
root.title("Minha GUI")
root.geometry("1000x1000")

label = tk.Label(root, text="sim", font=("Arial", 12))
label.pack(expand=True)

root.mainloop()
