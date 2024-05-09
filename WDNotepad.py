import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def save_file():
    file_location = asksaveasfilename(
        defaultextension="txt",
        filetypes=["Text files","*.txt",("Doc file","*.docx")]
        )
    if not file_location:
        return
    with open(file_location, "w") as file_ouput:
        text = text_edit.get(1.0, tk.END)
        file_ouput.write(text)

    root.title(f"WD note - {file_location}")



def open_file():
    file_location = askopenfilename(
        filetypes=[("Text file","*.txt"),("Doc file","*.docx")]
    )

    if not file_location:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root.title(f"WD note - {file_location}")




root = tk.Tk()
root.title(" WD note")
root.rowconfigure(0, minsize=800)
root.columnconfigure(1, minsize=800)


text_edit = tk.Text(root)
text_edit.grid(row=0,column=1, sticky="nsew")

frame_button = tk.Frame(root, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")

open_file_button = tk.Button(frame_button, text="Open file", command=open_file)
open_file_button.grid(row=0, column=0, padx=5, pady=5)

save_file_button = tk.Button(frame_button, text ="Save as", command=save_file)
save_file_button.grid(row=1, column=0, padx=5)



root.mainloop()