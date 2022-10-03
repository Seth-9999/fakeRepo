import tkinter as tk
 
 
def pprint():
  lab["text"] = "You clicked"
 
 
 
# ===== GUI ==== #
root = tk.Tk()
 
lab = tk.Label(root,
  text="Hello World!", font="Arial 36")
lab.grid(row=0, column=1)
 
button = tk.Button(root, text="Click", font="Arial 36")
button.grid(row=0, column=0)
button["command"] = pprint
 
print("This was added by that fake guy")
print("Ha ha.... this was added by the real guy so ha@!")
root.mainloop()
