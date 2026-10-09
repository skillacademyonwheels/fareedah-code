from tkinter import Tk, Text, Frame, Button, END, RAISED
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "r", encoding="utf-8") as input_file:
        content = input_file.read()

    txt_edit.delete(1.0, END)
    txt_edit.insert(END, content)
    window.title(f"Codingal's Text Editor - {filepath}")


def save_file():
    """Save current text to a file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return

    with open(filepath, "w", encoding="utf-8") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)

    window.title(f"Codingal's Text Editor - {filepath}")


window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")

txt_edit = Text(window)
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
