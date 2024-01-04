# Requirements (pip install):
# - PySimpleGUI
# - pyperclip
# - pyinstaller

import PySimpleGUI as sg
import pyperclip
import re

layout = [
    [sg.Text("Paste in Alma date")],
    [sg.InputText()],
    [sg.Submit(), sg.Cancel()],
]

window = sg.Window("Alma > WRDS date converter", layout)

event, values = window.read()
window.close()

text_input = values[0]
wrds_date = re.sub(r"(\d{2})[/](\d{2})[/](\d{4})", r"\3-\2-\1", text_input)
pyperclip.copy(wrds_date)
# 30/06/2025


sg.popup("WRDS date (copied to clipboard)", wrds_date)

# Build Mac application:
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --windowed --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' wrds_date.py
