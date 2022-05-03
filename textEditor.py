import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class main(object):
    def __init__(self):
        pass

    def openFile(self):
        filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        textEdit.delete("1.0", tk.END)
        with open(filepath, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
            textEdit.insert(tk.END, text)
        window.title(f"Simple Text Editor - {filepath}")

    def saveFile(self):
        filepath = asksaveasfilename( 
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, mode="w", encoding="utf-8") as output_file:
            text = textEdit.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"Simple Text Editor - {filepath}")

    def submitChanges(self):
        newColor = enterNewColor.get("text")
        fontColor = newColor

    def openNewWindow(self):
        newWindow = tk.Toplevel(window, bg=textEditColorBG)
        newWindow.title('Settings')
        newWindow.geometry('400x400')
        enterNewColorLabel = tk.Label(
            master=newWindow,
            text='New Text Edit BG color',
            bg=frmButtonsFrmBG,
            fg=fontColor
            )
        enterNewColor = tk.Entry(master=newWindow, width = 8)
        submitButton = tk.Button(
            master=newWindow,
            text='Submit',
            command=self.submitChanges,
            bg=frmButtonsColorBG,
            fg=fontColor
            )
        enterNewColorLabel.grid(row=0, column=0)
        enterNewColor.grid(row=0, column=1)
        submitButton.grid(row=1, column=0, sticky="w")

    def textEditor(self, window):
        newColor = '#ffffff'
        fontColor = '#00ff2a'
        textEditColorBG = '#3a495a'
        frmButtonsFrmBG = '#4d6075'
        frmButtonsColorBG = '#242224'

        window.title("Simple Text Editor")

        window.rowconfigure(0, minsize=800, weight=1)
        window.columnconfigure(1, minsize=800, weight=1)

        textEdit = tk.Text(window, bg=textEditColorBG, fg=fontColor, insertbackground=fontColor)
        frmButtons = tk.Frame(window, relief=tk.RAISED, bd=2, bg=frmButtonsFrmBG)
        btnOpen = tk.Button(frmButtons, text="Open", command=self.openFile, bg=frmButtonsColorBG, fg=fontColor)
        btnSave = tk.Button(frmButtons, text="Save As...", command=self.saveFile, bg=frmButtonsColorBG, fg=fontColor)
        btnSettings = tk.Button(frmButtons, text="Settings", command=self.openNewWindow, bg=frmButtonsColorBG, fg=fontColor)

        btnOpen.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btnSave.grid(row=1, column=0, sticky="ew", padx=5)
        btnSettings.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        frmButtons.grid(row=0, column=0, sticky="ns")
        textEdit.grid(row=0, column=1, sticky="nsew")


window = tk.Tk()
app = main()
app.textEditor(window)
window.mainloop()
